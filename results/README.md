# 高考测评结果
这个文件夹包括所有模型的推理代码、生成结果以及详细得分情况。

## 文件结构
评测结果的文件结构如下所示，文件夹的结构为 `试卷名`-`学科`-`模型输出展示的jupyter notebook文件`
```
results/
├────── README.md      # 测试说明
├────── 新课标I卷/       # 每种高考卷类型创建一个文件夹
│       ├── README.md   # 对应高考卷的分数汇总
│       ├── 数学/       # 各种模型的生成结果
│       │   ├── 新课标Ⅰ数学_Mixtral-8x22B-Instruct-v0.1.ipynb
│       │   ├── 新课标Ⅰ数学_Qwen2-57B-A14B-Instruct.ipynb
│       │   ├── 新课标Ⅰ数学_Qwen2-72B-Instruct.ipynb
│       │   ├── 新课标Ⅰ数学_Yi-1.5-34B-Chat.ipynb
│       │   ├── 新课标Ⅰ数学_glm-4-9b-chat.ipynb
│       │   ├── 新课标Ⅰ数学_gpt-4o.ipynb
│       │   └── 新课标Ⅰ数学_internlm2-wqx-20b.ipynb
│       ├── 英语/
│       └── 语文/
└────── 全国甲卷/      每种高考卷类型创建一个文件夹
```

## 题目示例
将题目输入到大模型中之前，我们会将输入转换为文本形式，如果是数学题这种有公式的情况，我们会使用 Latex 的格式进行表示，例如下图的题目

![image](https://github.com/OpenMOSS/CoLLiE/assets/65400838/2ad7393b-a93b-4ebf-a5d6-a81d5f9e4162)
> 不过我们在处理数学大题的时候出现了点小披露，没有添加小题序号，模型看到的内容就如上图所示没有小题的标识，但在实际评测过程中我们发现大部分模型是能够意识到这是三个不同的小问。

会转换为以下内容作为模型输入:
```latex
已知函数 $f(x)=\ln \frac{x}{2-x}+a x+b(x-1)^3$.
若 $b=0$, 且 $f^{\prime}(x) \geqslant 0$, 求 $a$ 的最小值.
证明: 曲线 $y=f(x)$ 是中心对称图形.
若 $f(x)>-2$, 当且仅当 $1<x<2$, 求 $b$ 的取值范围.
```

在推理时，每个模型的`max_new_token`都被设置为了`2048`，并且除语文、英语作文以外都使用`贪婪解码`策略。


## Jupyter Notebook 记录过程

为了保证答题过程的可复现性，本项目使用Jupyter Notebook记录了每个模型的答题情况。在每个Notebook中，通过对比模型输出和标准答案，展示了模型的答题能力。以下是Notebook的基本结构和每个单元格（cell）的功能说明：

### Notebook 结构

- **Cell 1**：使用Markdown记录试卷信息、题目标答和模型输出，并对模型输出进行详细解析，方便用户查看模型的解题思路和结果。
- **Cell 2**：包含加载模型和相关库的脚本，并初始化模型以便后续推理使用。
- **Cell 3**：进行模型推理，打印解题记录，包括模型的输出和标准答案的对比，便于评估模型的表现。


### Notebook 内容示例

#### Cell 1: 试卷信息和解析

在这一单元格中，使用Markdown格式记录试卷信息、题目标答和模型输出，并对模型输出进行详细解析，以便浏览和理解。

```markdown
# 试卷名：新课标卷Ⅰ 高考真题 【数学】学科

## 题目编号：1
## 题目标答
因为$  A = \left\{ x | - \sqrt [ 3 ] { 5 } < x < \sqrt [ 3 ] { 5 } \right\} $ ， 又$  \sqrt [ 3 ] { 5 } < \sqrt [ 3 ] { 8 } = 2$  ，故$ A\cap B=\{-1,0\}$ ． 故选$ \text{A}$ ．

## 模型输出

...

------
```

#### Cell 2: 模型加载脚本

加载所需的模型和相关库，并进行初始化。为保证公平性，除作文外所有的预测推理均为**贪婪**生成。`max_length`设置为`2048`，仅有少部分生成结果因为重复生成导致被截断。

```python
import re
import json

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda")

model_path = "path-to-model"
gen_kwargs = {"max_length": 2048, "do_sample": False}

tokenizer = AutoTokenizer.from_pretrained(
    model_path, trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype=torch.float16,
).eval().to(device)
```

#### Cell 3: 模型推理并记录解题过程

进行模型推理，并打印解题记录，包括模型的输出和标准答案的对比。

```python
subject, paper_type = "数学", "新课标卷Ⅰ"
file_name = f"../data/{paper_type}/{subject}.jsonl"

questions = []

print(f"试卷名：{paper_type} 高考真题 【{subject}】学科")

with open(file_name, "r") as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        has_img, question = False, data['prompt']

        if '<img' in question:
            has_img = True
            question = re.sub(r'<img[^>]*?/>', "", question)

        inputs = tokenizer.apply_chat_template(
            [{"role": "user", "content": question}],
            add_generation_prompt=True,
            tokenize=True,
            return_tensors="pt",
            return_dict=True
        )
        inputs = inputs.to(device)

        with torch.no_grad():
            outputs = model.generate(**inputs, **gen_kwargs)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
            
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        if i == 0:
            print("*" * 35)
        else:
            print("*" * 15)

        print("题目编号：" + str(i+1) + ("（含图片）" if has_img else ""))
        print("题目标答：" + data["answer"])
        print("模型输出：" + response)
            
        questions.append({
            "id": str(i+1),
            "question": question,
            "answer": data["answer"],
            "output": response,
            "has_img": has_img
        })
```

