import os
from argparse import ArgumentParser
import gradio as gr
import mdtex2html
import requests
from PIL import Image
from io import BytesIO
import re
import torch
import queue
import threading
try:
    from transformers.generation.streamers import BaseStreamer
except:  # noqa # pylint: disable=bare-except
    BaseStreamer = None
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer, AutoModel
from infer_wqx_vl import process_query_and_image, HD_transform


DEFAULT_VL_CKPT_PATH = 'internlm/internlm2-wqx-vl-20b'

def _get_args():
    parser = ArgumentParser()
    parser.add_argument("-m", "--vl_checkpoint_path", type=str, default=DEFAULT_VL_CKPT_PATH,
                        help="Checkpoint name or path, default to %(default)r")
    parser.add_argument("--share", action="store_true", default=False,
                        help="Create a publicly shareable link for the interface.")
    parser.add_argument("--inbrowser", action="store_true", default=False,
                        help="Automatically launch the interface in a new tab on the default browser.")
    parser.add_argument("--server-port", type=int, default=10086,
                        help="Demo server port.")
    parser.add_argument("--server-name", type=str, default="0.0.0.0",
                        help="Demo server name.")
    parser.add_argument("--cache_dir", default="data/img_cache", type=str,
                        help="Directory to save image cache.")

    args = parser.parse_args()
    return args


def load_vl_model_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.vl_checkpoint_path, trust_remote_code=True, resume_download=True,
    )

    model = AutoModel.from_pretrained(
        args.vl_checkpoint_path, torch_dtype=torch.bfloat16, trust_remote_code=True, resume_download=True
    ).cuda().eval()
    model.cuda().half()
    model.tokenizer = tokenizer

    return model, tokenizer


def load_model_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True, resume_download=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        trust_remote_code=True,
        resume_download=True,
    ).eval()

    return model, tokenizer


def postprocess(self, y):
    """Override Chatbot.postprocess"""
    if y is None:
        return []
    for i, (message, response) in enumerate(y):
        y[i] = (
            None if message is None else mdtex2html.convert((message)),
            None if response is None else mdtex2html.convert(response),
        )
    return y


gr.Chatbot.postprocess = postprocess


def parse_text(text):
    """copy from https://github.com/GaiZhenbiao/ChuanhuChatGPT/"""
    lines = text.split("\n")
    lines = [line for line in lines if line != ""]
    count = 0
    for i, line in enumerate(lines):
        if "```" in line:
            count += 1
            items = line.split('`')
            if count % 2 == 1:
                lines[i] = f'<pre><code class="language-{items[-1]}">'
            else:
                lines[i] = f'<br></code></pre>'
        else:
            if i > 0:
                if count % 2 == 1:
                    line = line.replace("`", "\`")
                    line = line.replace("<", "&lt;")
                    line = line.replace(">", "&gt;")
                    line = line.replace(" ", "&nbsp;")
                    line = line.replace("*", "&ast;")
                    line = line.replace("_", "&lowbar;")
                    line = line.replace("-", "&#45;")
                    line = line.replace(".", "&#46;")
                    line = line.replace("!", "&#33;")
                    line = line.replace("(", "&#40;")
                    line = line.replace(")", "&#41;")
                    line = line.replace("$", "&#36;")
                lines[i] = "<br>" + line
    text = "".join(lines)
    return text


def gc():
    import gc
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

def launch_demo(args, model):

    def predict(input, image_path, chatbot):

        if image_path is not None:
            input += '<IMAGE>'
        if input == '' and image_path is None:
            return [(input, "文本与图片为空！请重试。")]
        chatbot.append((parse_text(input), ""))

        query = input

        if os.path.exists(image_path):
            image = Image.open(image_path)
        else:
            response = requests.get(image_path)
            image = Image.open(BytesIO(response.content))
        with torch.cuda.amp.autocast():
            embeds, im_mask = process_query_and_image(query, image, model, HD_transform)

            outputs = model.generate(inputs_embeds=embeds, im_mask=im_mask,
                                        temperature=0.0, max_new_tokens=256, num_beams=1,
                                        do_sample=False, repetition_penalty=1.0)
            output_token = outputs[0]
            output_text = model.tokenizer.decode(output_token, add_special_tokens=False)
        print(output_text,chatbot)
        output_text=output_text.replace("<s>", "").replace("</s>", "")

        chatbot[-1] = (parse_text(query), parse_text(output_text))
        return chatbot

    def stop_generate():
        global stop_gen
        stop_gen = True

    def reset_user_input():
        return gr.update(value='')

    def reset_state():
        stop_generate()
        gc()
        return None, []
    
    examples = [
        [r"体育课上两位同学在室内羽毛球场进行羽毛球比赛，羽毛球在空中上升的运动轨迹如图中虚线所示，考虑空气阻力，羽毛球加速度方向示意图可能正确的是（\u3000\u3000） \nA:<IMAGE 0> \nB: <IMAGE 1> \nC:<IMAGE 2> \nD:<IMAGE 3> ,对图片进行描述然后再回答", "https://ks-1302698447.cos.ap-shanghai.myqcloud.com/img/phymerge.png"]
    ]

    with gr.Blocks() as demo:
        gr.Markdown("""<center><font size=8>GaoKao eval多模态推理</center>""")

        chatbot = gr.Chatbot()
        with gr.Row():
            user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=10)
            image_path = gr.Image(type="filepath", label="Image Prompt", value=None)
        with gr.Row():
            submit_btn = gr.Button("Submit（发送）", variant="primary")


        submit_btn.click(predict, [user_input, image_path, chatbot], [chatbot],
                         show_progress=True)
        submit_btn.click(reset_user_input, [], [user_input])

        image_path.clear(reset_state, outputs=[image_path, chatbot], show_progress=True)
        
        gr.Examples(examples=examples, inputs=[user_input, image_path])


    demo.queue().launch(
        share=args.share,
        inbrowser=args.inbrowser,
        server_port=args.server_port,
        server_name=args.server_name,
    )


def main():
    args = _get_args()

    model_vl, _ = load_vl_model_tokenizer(args)

    launch_demo(args, model_vl)


if __name__ == '__main__':
    main()
