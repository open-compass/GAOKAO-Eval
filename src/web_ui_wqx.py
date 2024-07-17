from argparse import ArgumentParser
import gradio as gr
import mdtex2html
import queue
import threading

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

try:
    from transformers.generation.streamers import BaseStreamer
except:  # noqa # pylint: disable=bare-except
    BaseStreamer = None

DEFAULT_MODEL_PATH = 'internlm/internlm2-wqx-20b'
stop_gen = False

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

    if args.cpu_only:
        device_map = "cpu"
    else:
        device_map = "auto"

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        device_map=device_map,
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


def stream_chat(
    model,
    tokenizer,
    query: str,
    max_new_tokens: int = 2048,
    do_sample: bool = True,
    temperature: float = 0.8,
    top_p: float = 0.8,
    **kwargs,
):
    
    if BaseStreamer is None:
        raise ModuleNotFoundError(
            "The version of `transformers` is too low. Please make sure "
            "that you have installed `transformers>=4.28.0`."
        )
    response_queue = queue.Queue(maxsize=20)

    class ChatStreamer(BaseStreamer):
        def __init__(self, tokenizer) -> None:
            super().__init__()
            self.tokenizer = tokenizer
            self.queue = response_queue
            self.query = query
            self.response = ""
            self.received_inputs = False
            self.queue.put((self.query, self.response))

        def put(self, value):
            if len(value.shape) > 1 and value.shape[0] > 1:
                raise ValueError("ChatStreamer only supports batch size 1")
            elif len(value.shape) > 1:
                value = value[0]

            if not self.received_inputs:
                # The first received value is input_ids, ignore here
                self.received_inputs = True
                return

            token = self.tokenizer.decode([value[-1]], skip_special_tokens=True)
            if token.strip() != "<|im_end|>":
                self.response = self.response + token
                response = (self.query, self.response)
                self.queue.put(response)

        def end(self):
            self.queue.put(None)

    def stream_producer():
        inputs = tokenizer([query], return_tensors="pt")
        inputs = {k: v.to(next(model.parameters()).device) for k, v in inputs.items() if torch.is_tensor(v)}
        eos_token_id = [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids(["<|im_end|>"])[0]]
        outputs = model.generate(
            **inputs,
            streamer=ChatStreamer(tokenizer=tokenizer),
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            eos_token_id=eos_token_id,
            **kwargs,
        )
        outputs = outputs[0].cpu().tolist()[len(inputs["input_ids"][0]) :]
        response = tokenizer.decode(outputs, skip_special_tokens=True)
        response = response.split("<|im_end|>")[0]
        return response, []

    def consumer():
        producer = threading.Thread(target=stream_producer)
        producer.start()
        while True:
            res = response_queue.get()
            if res is None:
                return
            yield res

    return consumer()


def launch_demo(args, model, tokenizer):

    def predict(input, chatbot):
        global stop_gen
        stop_gen = False
        chatbot.append((parse_text(input), ""))
        for query, response in stream_chat(model, tokenizer, input):
            if stop_gen:
                chatbot.clear()
                return chatbot
            chatbot[-1] = (parse_text(query), parse_text(response))
            yield chatbot

    def stop_generate():
        global stop_gen
        stop_gen = True

    def reset_user_input():
        return gr.update(value='')

    def reset_state():
        stop_generate()
        gc()
        return []

    with gr.Blocks() as demo:
        gr.Markdown("""\
<p align="center"><img src="https://raw.githubusercontent.com/InternLM/InternLM/main/assets/logo.svg" style="height: 80px"/><p>""")
        gr.Markdown("""<center><font size=8>InternLM2-WQX</center>""")
        gr.Markdown(
            """\
<center><font size=3>本WebUI基于InternLM2-WQX打造，是InternLM团队推出的文曲星系列模型。</center>""")
        gr.Markdown("""\
<center><font size=4>
InternLM2-WQX-20b <a href="https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-wqx-20b/summary">🤖 </a> | 
<a href="https://huggingface.co/internlm/internlm2-wqx-20b">🤗</a>&nbsp ｜ 
InternLM2-WQX-VL-20b <a href="https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-wqx-vl-20b/summary">🤖 </a> | 
<a href="https://huggingface.co/internlm/internlm2-wqx-vl-20b">🤗</a>&nbsp ｜ 
&nbsp<a href="https://github.com/InternLM/InternLM-WQX">💻 Github</a></center>""")

        chatbot = gr.Chatbot()
        with gr.Row():
            user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=10)
        with gr.Row():
            submit_btn = gr.Button("Submit（发送）", variant="primary")
            clear_btn = gr.Button("Stop（停止生成）", variant="stop")

        submit_btn.click(predict, [user_input, chatbot], [chatbot],
                         show_progress=True)
        submit_btn.click(reset_user_input, [], [user_input])

        clear_btn.click(reset_state, outputs=[chatbot], show_progress=True)

    demo.queue().launch(
        share=args.share,
        inbrowser=args.inbrowser,
        server_port=args.server_port,
        server_name=args.server_name,
    )


def main():
    args = get_args()

    model, tokenizer = load_model_tokenizer(args)

    launch_demo(args, model, tokenizer)


if __name__ == '__main__':
    main()
