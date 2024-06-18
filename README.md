# GAOKAO-Eval

<div align="center">

<img src="https://raw.githubusercontent.com/InternLM/InternLM/main/assets/logo.svg" width="200"/>
  <div> </div>
  <div align="center">
    <b><font size="5">GAOKAO-Eval</font></b>
  </div>
</div>

# 介绍
高考作为中国最权威的考试之一，覆盖各种学科和题型，旨在综合评估考生的能力。因此可以作为一个极佳的大模型评测，我们选取了在2024年6月6日之前发布的开源模型和当前最先进的大模型GPT-4o在2024年的高考试卷上进行全面的评测。与过去只测试客观题的评测不同，本测试涵盖了高考的各种题型，包括选择题、解答题、阅读题以及作文等，所有主观题均邀请在职高中老师进行评分，以期能够比较全面地评判当前大模型的能力。

因此，GAOKAO-Eval有以下四个特点：
- **全卷考试**：进行全卷的评分，而不是只考虑单一题型
- **考前开源**：评测覆盖的开源模型均为高考前开源的模型，排除泄题的可能性
- **老师打分**：邀请有高考阅卷经验的老师打分，确保评分和高考尽量一致
- **完全公开**：生成答案的代码、模型答卷、评分结果完全开源

> **正如高考分数存在误差，评测也无法做到绝对公平，因此测评中的分数只是一个参考值，为了尽量客观，每个题目我们都邀请了至少三位老师评阅取均分，我们对分差较大的题目还进行了再次审核。**

> **特别值得注意的是，大模型犯错误的方式和人类考生有差异，从实践上来看阅卷老师们不完全适应给大模型评分，因此存在有题目误判的可能。**

> **此外，我们也注意到，不同的高考试卷对大模型存在较大的分数随机性，因此不同省市的分数或排名可能出现明显变化。**



# 高考试卷类型

随着高考的改革，2024年全国高考试卷共有六种类型，
| 试卷类型 | 使用省市  |
|--------------------------------------|---|
|             新课标I卷                         | 广东、福建、湖北、湖南、江苏、河北、山东、浙江、江西、安徽、河南  |
|             新课标II卷                |  辽宁、重庆、海南、山西、新疆、广西、贵州、黑龙江、甘肃、吉林、云南、西藏 |
|            全国甲卷    |  四川、内蒙古、宁夏、陕西、青海 |
|          北京卷                            |  北京市 |
|           上海卷                           | 上海市  |
|            天津卷                     |  天津市 |

其中北京卷、上海卷、天津卷、全国甲卷涵盖所有学科，使用新课标I卷、新课标II卷的省市使用对应的语数外试卷，大部分省市非语数外的科目自主命题。在GAOKAO-Eval中，我们主要测试新课标I卷、上海市的语数外三门课程，全国甲卷、北京卷所有的课程。

高考模式方面，现行体系主要分为三大类：
- **“3+1+2”新模式**，已被23个省份广泛采纳，此模式围绕语文、数学、外语三大基础学科构建，要求学生在物理与历史中择其一作为首选科目，并从剩余四科（思想政治、地理、化学、生物）中自由选择两科。
- **“3+3”模式**，目前有6个省份采用，在此框架下，学生在完成语、数、外必修后，可从包括思想政治至生物在内的六科中（浙江省额外包含技术科目），自由组合三科作为选修。
- 余下的5个省份依旧沿用**全国甲卷**的文理分科体系，保持了传统分类下的学术评估路径。

# 成绩

1. 新课标I卷（语、数、外）

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th colspan="5"  style="text-align: center;">语数外得分情况</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>模型</td>
      <td>语文(满分150)</td>
      <td>数学（满分150）</td>
      <td>英语（满分120）</td>
      <td>总分（满分420）</td>
    </tr>
    <tr>
      <td>阿里巴巴 千问2-72B</td>
      <td>124</td>
      <td>70</td>
      <td>109</td>
      <td>303</td>
    </tr>
    <tr>
      <td>OpenAI GPT-4o</td>
      <td>111.5</td>
      <td>73</td>
      <td>111.5</td>
      <td>296</td>
    </tr>
    <tr>
      <td>上海人工智能实验室 书生·浦语-文曲星-20B</td>
      <td>112</td>
      <td>75</td>
      <td>108.5</td>
      <td>295.5</td>
    </tr>
    <tr>
      <td>阿里巴巴 千问2-57B</td>
      <td>99.5</td>
      <td>58</td>
      <td>96.5</td>
      <td>254</td>
    </tr>
    <tr>
      <td>零一万物 Yi-1.5-34B</td>
      <td>97</td>
      <td>29</td>
      <td>104.5</td>
      <td>230.5</td>
    </tr>
    <tr>
      <td>智谱 GLM4-9B</td>
      <td>86</td>
      <td>49</td>
      <td>67</td>
      <td>202</td>
    </tr>
    <tr>
      <td>Mistral Mixtral 8x22B</td>
      <td>77.5</td>
      <td>21</td>
      <td>86.5</td>
      <td>185</td>
    </tr>
  </tbody>
</table>

各个模型具体的详细得分情况、模型输出，请参阅[新课标I卷结果](./results/新课标I卷/README.md)。

> 在打分前，老师们并未被告知答案由大模型生成，但由于有的模型会存在完全不理解题意导致乱答、重复生成、回答更像解析而非解答的问题，老师们在阅卷过程中基本都会和我们确认这些情况是否是正常情况，我们会要求老师将离谱的错误直接视为答题错误，解析类型的回答以是否包含正确解题过程作为唯一准则。此外，一些老师提出，由于全部回答没有卷面，所以在作文的评判上会存在1~2分的误差。


# 模型
我们选择来自于阿里巴巴、零一万物、智谱AI、上海人工智能实验室、Mistral和OpenAI的大模型进行评测。

高考题目中存在大量的带图的题目，大语言模型只回答不带图的题目（少部分情况例外），多模态大模型对所有题目进行作答。开源模型中我们只选择在2024年6月6日之前开源的模型，同时选取了目前最强大的大模型GPT-4o作为参考。参与评测大模型的情况如下表所示

|                                   | 所属组织名         | 模型类型 | 模型简介                                                             | 权重上传时间 | 模型链接                                                     |
|-----------------------------------|--------------------|----------|----------------------------------------------------------------------|--------------|--------------------------------------------------------------|
| 上海人工智能实验室 书生·浦语-文曲星-20B | 上海人工智能实验室 |     语言模型     | 上海人工智能实验室推出的文曲星系列基础模型                           | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/internlm/internlm2-wqx-20b)            |
| 上海人工智能实验室 书生·浦语-文曲星-20B-VL | 上海人工智能实验室 |     多模态模型     | 上海人工智能实验室推出的文曲星系列多模态基础模型                           | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/internlm/internlm2-wqx-vl-20b)            |
| 阿里巴巴 千问2-72B                    | 阿里巴巴           |  语言模型  | 由阿里巴巴公司发布的Qwen2系列最大的对话模型。                        | 2024.05.28   | [🤗HuggingFace](https://huggingface.co/Qwen/Qwen2-72B-Instruct)               |
| 阿里巴巴 千问2-57B                     | 阿里巴巴           |     语言模型     | 由阿里巴巴公司发布的Qwen2系列MoE对话模型。                           | 2024.05.22   | [🤗HuggingFace](https://huggingface.co/Qwen/Qwen2-57B-A14B)                   |
| 阿里巴巴 千问VL                     | 阿里巴巴           |     多模态模型     | 由阿里巴巴公司发布的多模态对话模型。                           | 2023.09.25   | [🤗HuggingFace](https://huggingface.co/Qwen/Qwen-VL-Chat)                   |
| 零一万物 Yi-1.5-34B               | 零一万物           |   语言模型       | 由零一万物公司发布Yi 1.5系列最大的模型。                             | 2024.05.12   | [🤗HuggingFace](https://huggingface.co/01-ai/Yi-1.5-34B-Chat)                 |
| 零一万物 Yi-VL-34B               | 零一万物           |   多模态模型       | 由零一万物公司发布多模态大模型。                             | 2024.01.19   | [🤗HuggingFace](https://huggingface.co/01-ai/Yi-VL-34B)                 |
| 智谱 GLM4-9B                      | 智谱AI             |       语言模型   | GLM-4-9B 是智谱 AI 推出的最新一代预训练模型 GLM-4 系列中的开源版本。 | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/THUDM/glm-4-9b-chat)                   |
| 智谱 GLM-4v-9B                      | 智谱AI             |      多模态模型   | GLM-4-9B 是智谱 AI 推出的最新一代预训练模型 GLM-4 系列中的多模态模型。 | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/THUDM/glm-4-9b-chat)                   |
| Mistral Mixtral 8x22B             | Mistral（法国）    |     语言模型     | Mixtral模型为法国AI创业公司Mistral现开源的最强大的对话模型           | 2024.04.17   | [🤗HuggingFace](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) |
| OpenAI GPT-4o                     | OpenAI（美国）     |      多模态模型    | OpenAI公司发布的最强大的大模型，目前也是世界上最领先的大模型         | 2024.05.13   | https://openai.com/index/hello-gpt-4o/                       |

# 文件结构
该项目的文件结构如下所示：
```
├── README.md
├── results/
│   ├── README.md
│   └── 新课标I卷/      # 每种高考卷类型创建一个文件夹
│       ├── README.md  # 对应高考卷的分数汇总
│       ├── 数学/       # 语言模型答题情况的jupyter notebook展示
│       │   ├── 新课标Ⅰ数学_Mixtral-8x22B-Instruct-v0.1.ipynb
│       │   └──...
│       ├── 英语/
│       └── 语文/
└── src/               # 模型推理脚本与交互代码
    ├── infer_internlm.py    
    └── infer_chat.py
```

# 最新进展
- **[2024.06.15]** 完成6个开源模型新课标I卷语、数、外三科评测，点击[新课标I卷结果](./results/新课标I卷/README.md)查看详情

# 路线图

考题结果补充
- [x] 新课标I卷语数外
   - [x] 大语言模型测试
- [ ] 上海卷语数外
   - [ ] 大语言模型测试
- [ ] 全国甲卷全科
   - [ ] 大语言模型测试
   - [ ] 多模态模型测试
- [ ] 北京卷全科
   - [ ] 大语言模型测试
   - [ ] 多模态模型测试

功能补充
- [ ] 交互代码

# 致谢
我们由衷感谢所有参与此次项目高中阅卷老师们，大模型的输出存在各种各样的问题，老师们怀着极大的耐心认真批改，感谢他们做出的努力。



```
@misc{internlm_gaokao,
  author       = {InternLM Team},
  title        = {GAOKAO-Eval: A Comprehensive GAOKAO Evaluation},
  year         = {2024},
  howpublished = {\url{https://github.com/open-compass/GAOKAO-Eval}},
  note         = {Accessed: 2024-06-05}
}
```
