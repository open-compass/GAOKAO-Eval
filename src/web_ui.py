from argparse import ArgumentParser
from threading import Thread

import gradio as gr
import mdtex2html

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, TextIteratorStreamer

DEFAULT_MODEL_PATH = 'internlm/internlm2-wqx-20b'

def get_args():
    parser = ArgumentParser()
    parser.add_argument("-m", "--model_path", type=str, default=DEFAULT_MODEL_PATH,
                        help="Model name or path, default to %(default)r")
    parser.add_argument("--cpu_only", action="store_true", help="Run demo with CPU only")

    parser.add_argument("--share", action="store_true", default=False,
                        help="Create a publicly shareable link for the interface.")
    parser.add_argument("--inbrowser", action="store_true", default=False,
                        help="Automatically launch the interface in a new tab on the default browser.")
    parser.add_argument("--server_port", type=int, default=7860,
                        help="Demo server port.")
    parser.add_argument("--server_name", type=str, default="127.0.0.1",
                        help="Demo server name.")

    args = parser.parse_args()
    return args


def load_model_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_path, trust_remote_code=True, resume_download=True,
    )
    config = AutoConfig.from_pretrained(
        args.model_path, trust_remote_code=True
    )

    if args.cpu_only:
        device_map = "cpu"
    else:
        device_map = "auto"
        if config.model_type == "chatglm":
            # for glm-4-9b-chat
            device_map = "cuda"

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        device_map=device_map,
        trust_remote_code=True,
        resume_download=True,
    ).eval()

    return model, tokenizer, config


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


def chat_stream(model, tokenizer, query, config):
    terminators = [tokenizer.eos_token_id]
    if config.model_type == "llama":
        # for Yi-1.5-34B-Chat
        terminators += [
            tokenizer.convert_tokens_to_ids("<|eot_id|>"),
            tokenizer.convert_tokens_to_ids("<|im_end|>")
        ]

    if config.model_type == "internlm2":
        # for internlm2-wqx-20b
        conversation = [query]
        inputs = tokenizer(conversation, return_tensors="pt")["input_ids"]
    else:
        conversation = [{'role': 'user', 'content': query}]
        inputs = tokenizer.apply_chat_template(
            conversation,
            add_generation_prompt=True,
            return_tensors='pt',
        )

    inputs = inputs.to(model.device)
    streamer = TextIteratorStreamer(tokenizer=tokenizer, skip_prompt=True, timeout=60.0, skip_special_tokens=True)
    generation_kwargs = dict(
        input_ids=inputs,
        streamer=streamer,
        max_length=512,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.8,
        top_p=0.8,
    )
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    for new_text in streamer:
        yield new_text


def launch_demo(args, model, tokenizer, config):

    def predict(query, chatbot):
        chatbot.append((parse_text(query), ""))
        response = ""
        for new_text in chat_stream(model, tokenizer, query, config):
            response += new_text
            chatbot[-1] = (parse_text(query), parse_text(response))

            yield chatbot

    def reset_user_input():
        return gr.update(value='')

    def reset_state(chatbot):
        chatbot.clear()
        gc()
        return []

    with gr.Blocks() as demo:
        gr.Markdown("""<center><font size=8>GaoKao-eval 文本推理</center>""")

        chatbot = gr.Chatbot(label=args.model_path, elem_classes="control-height")
        with gr.Row():
            user_input = gr.Textbox(lines=2, label='Input')
        with gr.Row():
            submit_btn = gr.Button("Submit（发送）", variant="primary")
            clear_btn = gr.Button("Clear History（清除历史）", variant="stop")

        submit_btn.click(predict, [user_input, chatbot], [chatbot],
                         show_progress=True)
        submit_btn.click(reset_user_input, [], [user_input])

        clear_btn.click(reset_state, [chatbot], [chatbot], show_progress=True)

    demo.queue().launch(
        share=args.share,
        inbrowser=args.inbrowser,
        server_port=args.server_port,
        server_name=args.server_name,
    )


def main():
    args = get_args()

    model, tokenizer, config = load_model_tokenizer(args)

    launch_demo(args, model, tokenizer, config)


if __name__ == '__main__':
    main()
