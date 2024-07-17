# 高考测评结果
这个文件夹包括所有模型的推理代码、生成结果以及详细得分情况。

## 文件结构
评测结果的文件结构如下所示，文件夹的结构为 `试卷名`-`学科`-`模型输出展示的jupyter notebook文件`
```
results/
├────── README.md      # 测试说明
├────── 新课标卷/       # 每种高考卷类型创建一个文件夹
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
### 数学公式
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

### 题目图片

对于带有图片的多模态考题,题目中的图片是以 HTML 格式嵌入的，例如：

体育课上两位同学在室内羽毛球场进行羽毛球比赛，羽毛球在空中上升的运动轨迹如图中虚线所示，考虑空气阻力，羽毛球加速度方向示意图可能正确的是（ ）
- A: `<img alt="" height="59px" src="data/img/0_0.png" style="vertical-align:middle;" width="149px"/>`
- B: `<img alt="" height="57px" src="data/img/0_1.png" style="vertical-align:middle;" width="130px"/>`
- C: `<img alt="" height="65px" src="data/img/0_2.png" style="vertical-align:middle;" width="144px"/>`
- D: `<img alt="" height="56px" src="data/img/0_3.png" style="vertical-align:middle;" width="140px"/>`

脚本将会提取这些图片并将它们显示在一张合成图片中。在合成图片中，我们将对应的位置标记为 `<IMAGE i>`，并将问题中原有的图片替换为 `<IMAGE i>`。如下图所示:

体育课上两位同学在室内羽毛球场进行羽毛球比赛，羽毛球在空中上升的运动轨迹如图中虚线所示，考虑空气阻力，羽毛球加速度方向示意图可能正确的是（ ）

- A: `<IMAGE 0>` 
- B: `<IMAGE 1>` 
- C: `<IMAGE 2>` 
- D: `<IMAGE 3>`

<img src="https://ks-1302698447.cos.ap-shanghai.myqcloud.com/img/phymerge.png" alt="web_ui_wqx_2" style="zoom:100%;" />


```python
import urllib.request
import shutil
import re
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt


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
    pad = max(new_w // 4, 100)
    font = ImageFont.truetype("src/fonts/SimHei font.ttf", pad // 5)
    new_img = Image.new('RGB', (new_w + pad, new_h), 'white')
    draw = ImageDraw.Draw(new_img)
    curr_h = 10
    for idx, im in enumerate(imgs):
        w, h = im.size
        new_img.paste(im, (pad, curr_h))
        draw.text((0, curr_h + h // 2), f'<IMAGE {idx}>', font=font, fill='black')
        if idx + 1 < len(imgs):
            draw.line([(0, curr_h + h + 10), (new_w + pad, curr_h + h + 10)], fill='black', width=2)
        curr_h += h + 20
    # 展示处理后的图片
    plt.imshow(new_img)
    plt.title("Processed Image")
    plt.show()
    return new_img


sample = questions[0]  # 选择一个样本进行展示
question = sample['q_main']
mid_prompt = question

pattern_img_tag = re.compile(r'<img alt=.*?"/>')
pattern_src = re.compile(r'src=".*?"')

imgs = pattern_img_tag.findall(mid_prompt)
im_list = []
if len(imgs) == 0:
    img = None
else:
    for i, img in enumerate(imgs):
        mid_prompt = mid_prompt.replace(img, f'<IMAGE {i}> ', 1)
        img = pattern_src.findall(img)[0].split('"')[1]
        if img.startswith("data/img/"):  # 本地路径
            shutil.copy(img, f"data/img_cache/sample_{i}.png")
        else:  # URL
            urllib.request.urlretrieve(img, f"data/img_cache/sample_{i}.png")
        im_list.append(f"data/img_cache/sample_{i}.png")
# 处理和展示图片
processed_img = img_process(im_list)
```



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

