import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM
import json

def get_args():
    parser = argparse.ArgumentParser(description="Run inference on a jsonl file with questions.")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the model checkpoint.")
    parser.add_argument("--source_file", default="data/question.jsonl", type=str,
                        help="Path to the jsonl file with questions.")
    parser.add_argument("--target_file", default="output/result.jsonl", type=str,
                        help="Path to the jsonl file with generations.")
    parser.add_argument("--max_len", type=int, default=2048)
    parser.add_argument("--repetition_penalty", type=float, default=1.0)
    parser.add_argument("--top_k", type=int, default=1)
    parser.add_argument("--top_p", type=float, default=0.8)
    parser.add_argument("--do_sample", type=bool, default=False)
    parser.add_argument("--temperature", type=float, default=0.0)

    args = parser.parse_args()
    return args

def load_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained(
        model_path, trust_remote_code=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",
        trust_remote_code=True,
    ).eval()
    return model, tokenizer

def model_interface(args):
    model, tokenizer = load_model(args.model_path)
    with open(args.target_file, "w") as writer:
        with open(args.source_file, "r") as reader:
            if args.target_file.endswith("jsonl"):
                lines = reader.readlines()
                data = [json.loads(line) for line in lines]
            else:
                data = json.load(reader)
        for question in data:
            print(question["prompt"])
            completion = model_gen(tokenizer, model, question["prompt"], args)
            question["completion"] = completion
            json_line = json.dumps(question, ensure_ascii=False)
            print("\n#######\nStandard answer:", question["answer"], 
                  "\n#######\nModel prediction result:", completion,
                  "\n#################\n")
            writer.write(json_line)
            writer.write("\n")
            

def model_gen(tokenizer, model, question, args):
    inputs = tokenizer(question, return_tensors="pt")

    device = next(model.parameters()).device
    input_ids = inputs["input_ids"].to(device)
    outputs = model.generate(
        input_ids,
        max_length=args.max_len,
        do_sample=args.do_sample,
        temperature=args.temperature,
        repetition_penalty=args.repetition_penalty,
        top_p=args.top_p,
        top_k=args.top_k
    )
    outputs = outputs[0].cpu().tolist()[len(inputs["input_ids"][0]):]
    response = tokenizer.decode(outputs, skip_special_tokens=True)
    return response

if __name__ == "__main__":
    args = get_args()
    model_interface(args)