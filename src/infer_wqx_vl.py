from PIL import Image
from io import BytesIO
import numpy as np
import requests
import torchvision.transforms as transforms
from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM
import torch
import argparse
import urllib
from PIL import Image, ImageDraw, ImageFont
from typing import TypedDict, List
import json
import os
import re

def get_args():
    parser = argparse.ArgumentParser(description="Run inference on a jsonl file with questions.")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the model checkpoint.")
    parser.add_argument("--source_file", default="data/question.jsonl", type=str,
                        help="Path to the jsonl file with questions.")
    parser.add_argument("--target_file", default="output/result.jsonl", type=str,
                        help="Path to the jsonl file with generations.")
    parser.add_argument("--cache_dir", default="src/input/img", type=str,
                    help="Path to the cache directory for downloaded images.")
    parser.add_argument("--max_len", type=int, default=2048)
    parser.add_argument("--repetition_penalty", type=float, default=1.1)
    parser.add_argument("--top_k", type=int, default=1)
    parser.add_argument("--top_p", type=float, default=0.8)
    parser.add_argument("--do_sample", type=bool, default=False)
    parser.add_argument("--temperature", type=float, default=0.0)

    args = parser.parse_args()
    return args


def img_process(im_list):
    imgs = []
    for p in im_list:
        try:
            imgs.append(Image.open(p))
        except:
            return -1
    new_w = 0
    new_h = 0
    for im in imgs:
        w, h = im.size
        new_w = max(new_w, w)
        new_h += h + 20
    new_w += 20
    new_h += 20
    # new_w = max(512, new_w)
    # new_h = max(512, new_h)
    pad = max(new_w // 4, 100)
    font = ImageFont.truetype("src/fonts/SimHei font.ttf", pad // 5)
    new_img = Image.new('RGB', (new_w + pad, new_h), 'white')
    draw = ImageDraw.Draw(new_img)
    curr_h = 10
    for idx, im in enumerate(imgs):
        w, h = im.size
        if im.mode == 'RGBA':
            # 创建一个白色背景的图像
            background = Image.new('RGB', im.size, (255, 255, 255))
            background.paste(im, mask=im.split()[3])  # 使用透明度通道作为掩码
            im = background
        new_img.paste(im, (pad, curr_h))
        draw.text((0, curr_h + h // 2), f'<IMAGE {idx}>', font=font, fill='black')
        if idx + 1 < len(imgs):
            draw.line([(0, curr_h + h + 10), (new_w + pad, curr_h + h + 10)], fill='black', width=2)
        curr_h += h + 20
    return new_img

def padding_336(b):
    width, height = b.size
    tar = int(np.ceil(height / 560) * 560)
    top_padding = int((tar - height) / 2)
    bottom_padding = tar - height - top_padding
    left_padding = 0
    right_padding = 0
    b = transforms.functional.pad(b, [left_padding, top_padding, right_padding, bottom_padding], fill=[255, 255, 255])

    return b


def HD_transform(img, hd_num=25):
    width, height = img.size
    trans = False
    if width < height:
        img = img.transpose(Image.TRANSPOSE)
        trans = True
        width, height = img.size
    ratio = (width / height)
    scale = 1
    while scale * np.ceil(scale / ratio) <= hd_num:
        scale += 1
    scale -= 1
    new_w = int(scale * 560)
    new_h = int(new_w / ratio)

    img = transforms.functional.resize(img, [new_h, new_w], )
    img = padding_336(img)
    width, height = img.size
    if trans:
        img = img.transpose(Image.TRANSPOSE)

    return img

def process_query_and_image(query, image, model, HD_transform):
    def process_image(img):
        img = img.convert("RGB")
        img = HD_transform(img, hd_num=4)
        img = model.vis_processor(img).unsqueeze(0).cuda().half()
        return model.encode_img(img)

    embeds = []
    im_mask = []
    images_loc = [0]

    for i, pts in enumerate(images_loc + [len(query)]):
        subtext = query[0:pts]
        text_embeds = model.encode_text(subtext, add_special_tokens=True)
        embeds.append(text_embeds)
        im_mask.append(torch.zeros(text_embeds.shape[:2]).cuda())

        if i == 0:
            image_embeds = process_image(image)
            embeds.append(image_embeds)
            im_mask.append(torch.ones(image_embeds.shape[:2]).cuda())

    embeds = torch.cat(embeds, dim=1)
    im_mask = torch.cat(im_mask, dim=1).bool()

    return embeds, im_mask

def load_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_path, torch_dtype=torch.bfloat16, trust_remote_code=True).cuda().eval()
    model.cuda().half()
    model.tokenizer = tokenizer
    return model, tokenizer

def model_interface(args):
    model, tokenizer = load_model(args.model_path)
    
    pattern = r'<img .*?"/>'
    mm_question_pattern = re.compile(pattern)
    pattern = r'src=".*?"'
    img_pattern =re.compile(pattern)
    cache_dir = args.cache_dir
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir, exist_ok=True)
    
    
    with open(args.target_file, "w") as writer:
        with open(args.source_file, "r") as reader:
            if args.target_file.endswith("jsonl"):
                lines = reader.readlines()
                data = [json.loads(line) for line in lines]
            else:
                data = json.load(reader)
        for idx, question in enumerate(data):
            has_img, prompt = False, question['prompt']
            if '<img' in prompt:
                has_img = True
                imgs = mm_question_pattern.findall(prompt)
                im_list = []
                for i, img in enumerate(imgs):
                    prompt = prompt.replace(img, f'<IMAGE {i}> ', 1)
                    img = img_pattern.findall(img)
                    assert len(img) == 1
                    img = img[0].split('"')[1]
                    cache_path = f"{cache_dir}/{idx}_{i}.png"
                    urllib.request.urlretrieve(img,cache_path)
                    im_list.append(cache_path)
                img = img_process(im_list)
        
                with torch.cuda.amp.autocast():
                    response = model_gen(model, prompt, img, 
                                        hd_num=4, 
                                        max_len=args.max_len,
                                        temperature=args.temperature,
                                        repetition_penalty=args.repetition_penalty, num_beams=1)
                if idx == 0:
                    print("*" * 35)
                else:
                    print("*" * 15)

                print("题目编号：" + str(idx + 1) + ("（含图片）" if has_img else ""))
                print("题目标答：" + question["answer"])
                print(f"模型输出：" + response)

                result={
                    "id": str(idx + 1),
                    "question": question['prompt'],
                    "answer": question["answer"],
                    "output": response,
                    "has_img": has_img
                }
                json_line = json.dumps(result, ensure_ascii=False)
                writer.write(json_line)
                writer.write("\n")
            

def model_gen(model, text, images, need_bos=True, hd_num=4, max_len=256,
              temperature=1.0,
              repetition_penalty=1.0,
              num_beams=1,
              **kwargs):
    pt1 = 0
    embeds = []
    im_mask = []
    if images is None:
        images = []
        images_loc = []
    else:
        images = [images]
        images_loc = [0]
    for i, pts in enumerate(images_loc + [len(text)]):
        subtext = text[pt1:pts]
        if need_bos or len(subtext) > 0:
            text_embeds = model.encode_text(subtext, add_special_tokens=need_bos)
            embeds.append(text_embeds)
            im_mask.append(torch.zeros(text_embeds.shape[:2]).cuda())
            need_bos = False
        if i < len(images):
            try:
                image = Image.open(images[i]).convert('RGB')
            except:
                image = images[i].convert('RGB')

            image = HD_transform(image, hd_num=hd_num)
            # print (image.size)
            # plt.imshow(image)
            # plt.show()
            image = model.vis_processor(image).unsqueeze(0).cuda()
            image_embeds = model.encode_img(image)
            embeds.append(image_embeds)
            im_mask.append(torch.ones(image_embeds.shape[:2]).cuda())
        pt1 = pts
    embeds = torch.cat(embeds, dim=1)
    im_mask = torch.cat(im_mask, dim=1)
    im_mask = im_mask.bool()

    outputs = model.generate(inputs_embeds=embeds, im_mask=im_mask,
                                temperature=temperature, max_new_tokens=max_len, num_beams=num_beams,
                                do_sample=False, repetition_penalty=repetition_penalty)

    output_token = outputs[0]
    if output_token[0] == 0 or output_token[0] == 1:
        output_token = output_token[1:]
    output_text = model.tokenizer.decode(output_token, add_special_tokens=False)
    output_text = output_text.split('[UNUSED_TOKEN_145]')[0].strip()
    return output_text


if __name__ == "__main__":
    args = get_args()
    model_interface(args)


