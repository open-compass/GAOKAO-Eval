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
- **全卷考试**：进行全卷评分，而不只针对单一题型，且包括带图的高考题
- **考前开源**：评测覆盖的开源模型均为今年高考前开源的模型，排除泄题的可能性
- **老师打分**：邀请有高考阅卷经验的老师打分，确保评分和高考尽量一致
- **完全公开**：生成答案的代码、模型答卷、评分结果完全开源

> **正如高考分数存在误差，评测也无法做到绝对公平，因此测评中的分数只是一个参考值，为了尽量客观，每个题目我们都邀请了至少三位老师评阅取均分，我们对存在阅卷分差的部分均进行了再次校准。**

> **特别值得注意的是，大模型犯错误的方式和人类考生有差异，从实践上来看阅卷老师们不完全适应给大模型评分，因此存在有题目误判的可能。**

> **此外，我们也注意到，不同的高考试卷对大模型存在较大的分数随机性，因此不同省市的分数或排名可能出现明显变化。**

> **注意，这个测评仅能评估大型语言模型在高考题目上的表现，不能全面评估模型的能力，因此高考分数的排名不能体现模型使用体验的好坏或者能力的高低。**



# 试卷类型

随着高考的改革，2024年全国高考试卷共有六种类型，其中北京卷、上海卷、天津卷、全国甲卷涵盖所有学科，使用新课标I卷、新课标II卷的省市使用对应的语数外试卷，大部分省市非语数外的科目自主命题。在GAOKAO-Eval中，我们测试新课标卷和全国甲卷所有的已公开试卷。
| 试卷类型 | 使用省市  |
|--------------------------------------|---|
|             新课标I卷                         | 广东、福建、湖北、湖南、江苏、河北、山东、浙江、江西、安徽、河南  |
|             新课标II卷                |  辽宁、重庆、海南、山西、新疆、广西、贵州、黑龙江、甘肃、吉林、云南、西藏 |
| 新课标卷 | 山西、河南、云南、西藏、新疆 |
|            全国甲卷    |  四川、内蒙古、宁夏、陕西、青海 |
|          北京卷                            |  北京市 |
|           上海卷                           | 上海市  |
|            天津卷                     |  天津市 |


高考模式方面，现行体系主要分为三大类：
- **“3+1+2”新模式**，已被23个省份广泛采纳，此模式围绕语文、数学、外语三大基础学科构建，要求学生在物理与历史中择其一作为首选科目，并从剩余四科（思想政治、地理、化学、生物）中自由选择两科。
- **“3+3”模式**，目前有6个省份采用，在此框架下，学生在完成语、数、外必修后，可从包括思想政治至生物在内的六科中（浙江省额外包含技术科目），自由组合三科作为选修。
- 余下的5个省份依旧沿用**全国甲卷**的文理分科体系，保持了传统分类下的学术评估路径。

# 成绩

## 1. 新课标卷
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: center;">
      <th colspan="13" style="text-align: center;">新课标&dagger;得分情况(按照理科总分排序)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <td>模型</td>
      <td>研发机构</td>
      <td>语文</td>
      <td>数学</td>
      <td>英语</td>
      <td>物理</td>
      <td>化学</td>
      <td>生物</td>
      <td>历史</td>
      <td>地理</td>
      <td>政治</td>
      <td>理科总分</td>
      <td>文科总分</td>
    </tr>
    <tr style="text-align: center;">
      <td>InternLM-WQX+VL-20B</td>
      <td>上海人工智能实验室 & 商汤科技 联合研发</td>
      <td>112</td>
      <td>74</td>
      <td>138.5</td>
      <td>39</td>
      <td>48</td>
      <td>57</td>
      <td>82</td>
      <td>58</td>
      <td>67</td>
      <td>468.5</td>
      <td>531.5</td>
    </tr>
      <tr style="text-align: center;">
      <td>GPT-4o</td>
      <td>OpenAI（美国）</td>
      <td>111.5</td>
      <td>73</td>
      <td>141.5</td>
      <td>36</td>
      <td>40</td>
      <td>65</td>
      <td>88</td>
      <td>59</td>
      <td>58</td>
      <td>467</td>
      <td>531</td>
    </tr>
    <tr style="text-align: center;">
      <td>Qwen2-72B纯文本</td>
      <td>阿里巴巴</td>
      <td>124</td>
      <td>68</td>
      <td>139</td>
      <td>42</td>
      <td>44</td>
      <td>48</td>
      <td>85</td>
      <td>70</td>
      <td>60</td>
      <td>465</td>
      <td>546</td>
    </tr>
    <tr style="text-align: center;">
      <td>Qwen2-72B+VL-7B</td>
      <td>阿里巴巴</td>
      <td>124</td>
      <td>68</td>
      <td>139</td>
      <td>19</td>
      <td>6</td>
      <td>48</td>
      <td>85</td>
      <td>4</td>
      <td>60</td>
      <td>404</td>
      <td>480</td>
    </tr>
    <tr style="text-align: center;">
      <td>Yi-34B+VL-34B</td>
      <td>零一万物</td>
      <td>97</td>
      <td>31</td>
      <td>134.5</td>
      <td>21</td>
      <td>37</td>
      <td>49</td>
      <td>48</td>
      <td>41</td>
      <td>51</td>
      <td>369.5</td>
      <td>402.5</td>
    </tr>
    <tr style="text-align: center;">
      <td>Qwen2-57B+VL-7B</td>
      <td>阿里巴巴</td>
      <td>99.5</td>
      <td>58</td>
      <td>126.5</td>
      <td>7</td>
      <td>6</td>
      <td>51</td>
      <td>73</td>
      <td>4</td>
      <td>62</td>
      <td>348</td>
      <td>423</td>
    </tr>
    <tr style="text-align: center;">
      <td>GLM4-9B+VL-9B</td>
      <td>智谱 AI</td>
      <td>86</td>
      <td>48</td>
      <td>97</td>
      <td>18</td>
      <td>27</td>
      <td>67</td>
      <td>80</td>
      <td>62</td>
      <td>48</td>
      <td>343</</td>
      <td>421</td>
    </tr>
    <tr style="text-align: center;">
      <td>Mixtral 8x22B</td>
      <td>Mistral</td>
      <td>77.5</td>
      <td>21</td>
      <td>116.5</td>
      <td>25</td>
      <td>35</td>
      <td>46</td>
      <td>54</td>
      <td>56</td>
      <td>38</td>
      <td>321</td>
      <td>363</td>
    </tr>
  </tbody>
</table>

&dagger;表示测评使用的是新课标I卷语数外+新课标卷文理综

如果模型名称中含有“+VL”的字样，表明涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。

各个模型具体的详细得分情况、模型输出，请参阅[新课标卷结果](./results/新课标/README.md)。

## 2. 全国甲卷

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: center;">
      <th colspan="13"  style="text-align: center;">全国甲卷得分情况(按照理科总分排序)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="text-align: center;">
      <td>模型</td>
      <td>研发机构</td>
      <td>语文</td>
      <td>英语</td>
      <td>数学（理）</td>
      <td>物理</td>
      <td>化学</td>
      <td>生物</td>
      <td>数学（文）</td>
      <td>历史</td>
      <td>地理</td>
      <td>理科总分</td>
      <td>文科总分(缺政治)</td>
    </tr>
    <tr style="text-align: center;">
      <td>Qwen2-72B纯文本</td>
      <td>阿里巴巴</td>
      <td>128</td>
      <td>141</td>
      <td>89</td>
      <td>32</td>
      <td>48</td>
      <td>50</td>
      <td>95</td>
      <td>71</td>
      <td>81</td>
      <td>488</td>
      <td>516</td>
    </tr>
    <tr style="text-align: center;">
      <td>GPT-4o</td>
      <td>OpenAI（美国）</td>
      <td>122</td>
      <td>142.5</td>
      <td>84</td>
      <td>31</td>
      <td>34</td>
      <td>72</td>
      <td>89</td>
      <td>82</td>
      <td>66</td>
      <td>485.5</td>
      <td>501.5</td>
    </tr>
    <tr style="text-align: center;">
      <td>InternLM-WQX+VL-20B</td>
      <td>上海人工智能实验室 & 商汤科技 联合研发</td>
      <td>111</td>
      <td>141</td>
      <td>78</td>
      <td>30</td>
      <td>52</td>
      <td>50</td>
      <td>71</td>
      <td>76</td>
      <td>64</td>
      <td>462</td>
      <td>463</td>
    </tr>
    <tr style="text-align: center;">
      <td>Qwen2-72B+VL-7B</td>
      <td>阿里巴巴</td>
      <td>128</td>
      <td>141</td>
      <td>89</td>
      <td>22</td>
      <td>22</td>
      <td>50</td>
      <td>95</td>
      <td>71</td>
      <td>34</td>
      <td>452</td>
      <td>469</td>
    </tr>
    <tr style="text-align: center;">
      <td>Mixtral 8x22B</td>
      <td>Mistral</td>
      <td>92</td>
      <td>142</td>
      <td>58</td>
      <td>38</td>
      <td>39</td>
      <td>54</td>
      <td>53</td>
      <td>74</td>
      <td>74</td>
      <td>423</td>
      <td>435</td>
    </tr>
    <tr style="text-align: center;">
      <td>GLM4-9B+VL-9B</td>
      <td>智谱 AI</td>
      <td>108</td>
      <td>110.5</td>
      <td>71</td>
      <td>29</td>
      <td>44</td>
      <td>55</td>
      <td>75</td>
      <td>54</td>
      <td>62</td>
      <td>417.5</td>
      <td>409.5</td>
    </tr>
    <tr style="text-align: center;">
      <td>Qwen2-57B+VL-7B</td>
      <td>阿里巴巴</td>
      <td>108</td>
      <td>141</td>
      <td>65</td>
      <td>6</td>
      <td>22</td>
      <td>44</td>
      <td>75</td>
      <td>77</td>
      <td>30</td>
      <td>386</td>
      <td>431</td>
    </tr>
    <tr style="text-align: center;">
      <td>Yi-34B+VL-34B</td>
      <td>零一万物</td>
      <td>109</td>
      <td>107.5</td>
      <td>39</td>
      <td>15</td>
      <td>40</td>
      <td>55.5</td>
      <td>65</td>
      <td>53</td>
      <td>54</td>
      <td>366</td>
      <td>388.5</td>
    </tr>
  </tbody>
</table>
如果模型名称中含有“+VL”的字样，表明涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。

各个模型具体的详细得分情况、模型输出，请参阅[全国甲卷结果](./results/全国甲卷/README.md)。

> 在打分前，老师们并未被告知答案由大模型生成，但由于有的模型会存在完全不理解题意导致乱答、重复生成、回答更像解析而非解答的问题，老师们在阅卷过程中基本都会和我们确认这些情况是否是正常情况，我们会要求老师将离谱的错误直接视为答题错误，解析类型的回答以是否包含正确解题过程作为唯一准则。此外，一些老师提出，由于全部回答没有卷面，所以在作文的评判上会存在1~2分的误差。


# 模型
我们选择来自于阿里巴巴、零一万物、智谱AI、上海人工智能实验室、Mistral和OpenAI的大模型进行评测。

高考题目中存在大量的带图的题目，大语言模型只回答不带图的题目（少部分情况例外），多模态大模型对所有题目进行作答。开源模型中我们只选择在2024年6月6日之前开源的模型，同时选取了目前最强大的大模型GPT-4o作为参考。参与评测大模型的情况如下表所示

|                                   | 研发机构         | 模型类型 | 模型简介                                                             | 权重上传时间 | 模型链接                                                     |
|-----------------------------------|--------------------|----------|----------------------------------------------------------------------|--------------|--------------------------------------------------------------|
| 书生·浦语-文曲星-20B | 上海人工智能实验室 & 商汤科技联合研发 |     语言模型     | 上海人工智能实验室联合商汤科技推出的文曲星系列基础模型。                           | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/internlm/internlm2-wqx-20b)            |
| 书生·浦语-文曲星-20B-VL | 上海人工智能实验室 & 商汤科技联合研发 |     多模态模型     | 上海人工智能实验室联合商汤科技推出的文曲星系列多模态基础模型。                           | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/internlm/internlm2-wqx-vl-20b)            |
| Qwen2-72B                    | 阿里巴巴           |  语言模型  | 由阿里巴巴公司发布的Qwen2系列最大的对话模型。                        | 2024.05.28   | [🤗HuggingFace](https://huggingface.co/Qwen/Qwen2-72B-Instruct)               |
| Qwen2-57B                     | 阿里巴巴           |     语言模型     | 由阿里巴巴公司发布的Qwen2系列MoE对话模型。                           | 2024.05.04   | [🤗HuggingFace](https://huggingface.co/Qwen/Qwen2-57B-A14B-Instruct)                   |
| QwenVL-7B                     | 阿里巴巴           |     多模态模型     | 由阿里巴巴公司发布的多模态对话模型。                           | 2023.09.25   | [🤗HuggingFace](https://huggingface.co/Qwen/Qwen-VL-Chat)                   |
| Yi-1.5-34B               | 零一万物           |   语言模型       | 由零一万物公司发布Yi 1.5系列最大的模型。                             | 2024.05.12   | [🤗HuggingFace](https://huggingface.co/01-ai/Yi-1.5-34B-Chat)                 |
| Yi-VL-34B               | 零一万物           |   多模态模型       | 由零一万物公司发布多模态大模型。                             | 2024.01.19   | [🤗HuggingFace](https://huggingface.co/01-ai/Yi-VL-34B)                 |
| GLM4-9B                      | 智谱AI             |       语言模型   | GLM-4-9B 是智谱 AI 推出的最新一代预训练模型 GLM-4 系列中的开源版本。 | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/THUDM/glm-4-9b-chat)                   |
| GLM-4v-9B                      | 智谱AI             |      多模态模型   | GLM-4-9B 是智谱 AI 推出的最新一代预训练模型 GLM-4 系列中的多模态模型。 | 2024.06.04   | [🤗HuggingFace](https://huggingface.co/THUDM/glm-4-9b-chat)                   |
| Mixtral 8x22B             | Mistral（法国）    |     语言模型     | Mixtral模型为法国AI创业公司Mistral现开源的最强大的对话模型           | 2024.04.17   | [🤗HuggingFace](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) |
| GPT-4o                     | OpenAI（美国）     |      多模态模型    | OpenAI公司发布的最强大的大模型，目前也是世界上最领先的大模型         | 2024.05.13   | https://openai.com/index/hello-gpt-4o/                       |

# 文件结构
本项目的文件结构如下所示：
```
├── README.md
├── results/
│   ├── README.md
│   └── 新课标/      # 每种高考卷类型创建一个文件夹
│   │   ├── README.md  # 对应高考卷的分数汇总
│   │   ├── 数学/       # 语言模型答题情况的jupyter notebook展示
│   │   │   ├── 新课标Ⅰ数学_Mixtral-8x22B-Instruct-v0.1.ipynb
│   │   │   └──...
│   │   ├── 英语/
│   │   ├── 语文/
│   │   ├── 化学/
│   │   └── ...
│   └── 全国甲卷/
│       ├── README.md
│       ├── 文综数学/
│   │   │   ├── 全国甲卷文综数学_Mixtral-8x22B-Instruct-v0.1.ipynb
│   │   │   └──...
│       └── ...
└── src/               # 模型推理脚本与交互代码
    ├── infer_chat.py.py    
    ├── infer_wqx_vl.py    
    ├── infer_wqx.py   
    ├── web_ui.py 
    ├── web_ui_wqx.py 
    └── web_ui_vl.py
```

# 题目评测
本次评测中的语数外三科中的题目图片均被丢弃，只有文字题干会输入到模型中（新课标I卷语、数、外三科考试中，仅数学包含2道带图题目，且对题目理解和作答影响不大），英语考试中的听力部分（分值30分）在统计总分时所有模型默认均满分。对于文综理综题目，我们将其中带有图片的题目使用该系列模型中的开源多模态模型进行作答，而不含图片的纯文本题目则由纯文本模型作答。所有模型使用的生成参数、提示词、输出结果以及得分情况均开源在本仓库中。

## 多模态题目评测
由于Mixtral系列仅有语言模型，所以仅使用语言模型进行多模态题目的作答。同时由于QwenVL-7B作答结果过差，新课标卷地理仅能取得4分，为尽量体现Qwen系列的真实水平，我们同时评测Qwen2-72B文本模型对新课标卷与全国甲卷的物理、化学、地理的多模态题目进行作答。

多模态题目处理方法参考 [多模态题目图片处理](./results/README.md#题目图片)

# 最新进展
- **[2024.07.17]** 完成6个开源模型全国甲卷除了政治外的语数外文综理综八科评测，点击[全国甲卷结果](./results/全国甲卷/README.md)查看详情
- **[2024.07.17]** 完成6个开源模型新课标卷文综理综六科评测，点击[新课标卷结果](./results/新课标/README.md)查看详情；修正新课标Ⅰ卷数学第10题的评测；新增Gradio调用脚本
- **[2024.06.15]** 完成6个开源模型新课标I卷语、数、外三科评测，点击[新课标卷结果](./results/新课标/README.md)查看详情


# 路线图

考题结果补充
- [x] 新课标I卷语数外和新课标卷文综理综
   - [x] 大语言模型测试
   - [x] 多模态模型测试
- [x] 全国甲卷全科
   - [x] 大语言模型测试
   - [x] 多模态模型测试

功能补充
- [x] 交互代码

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
