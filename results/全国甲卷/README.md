# 全国甲卷摘要
全国甲卷覆盖的省份包括四川、内蒙古、陕西、青海、宁夏五个省份，本次测试使用全国甲卷的全套各科试题进行测试（除政治试题；政治试题尚未公开）。具体题目可以在 [高考直通车](https://easylearn.baidu.com/gaokao/content/list?tabKey=question) 查看。
# 评测
在评测过程中，模型的回答被随机命名为A、B、C、D、E、F、G提供给老师进行打分，在打分时依照以下标准打分
- 语数外三科均丢弃图片使用纯文本推理（与新课标卷保持一致）
- 各科目的单选题、填空题和答案是否完全一致才得分；
- 数学中多选题按照正确选项个数比例给分，如果有错误选项则直接不给分；
- 主观题根据步骤正确性会提供步骤分；
- 作文题根据作文给分标准进行打分；
- 带有图片的文综理综的题目由该系列模型中的多模态模型进行打分，其中Mixtral等模型因为仅有纯文本版本，所以采用不看图的分数。Qwen2模型由于只开源了QwenVL-7B版本，因此Qwen多模态模型的结果可能与模型的真实实力存在一定差距；
- 由于QwenVL-7B作答结果过差，为尽量体现Qwen系列的真实水平，我们同时评测Qwen2-72B文本模型对全国甲卷物理、化学、地理的多模态题目进行作答。
此外为了保证模型结果可复现，除了作文以外，所有的答案均由各个模型通过贪婪解码生成。

## 总分情况
参加考试的模型总分情况如下所示

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: center;">
      <th colspan="13" style="text-align: center;">全国甲卷得分情况(按照理科总分排序)</th>
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
      <td>InternLM-WQX-20B+VL-20B</td>
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

题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。


## 语文
语文试卷各部分的得分如下所示
<table border="1"> <tr style="text-align: center;"> <th colspan="8" style="text-align: center;">语文各题型得分情况</th> </tr> <tr style="text-align: center;"> <td>模型</td> <td>现代文阅读（满分36分）</td> <td>文言文阅读（满分19分）</td> <td>古诗文阅读（满分9分）</td> <td>名篇名句默写（满分6分）</td> <td>语言文字运用（满分20分）</td> <td>作文（满分60分）</td> <td>总分（满分150）</td> </tr> <tr style="text-align: center;"> <td>Qwen2-72B</td> <td>35</td> <td>19</td> <td>9</td> <td>2</td> <td>15</td> <td>48</td> <td>128</td> </tr> <tr style="text-align: center;"> <td>GPT-4o</td> <td>29</td> <td>19</td> <td>8</td> <td>4</td> <td>14</td> <td>48</td> <td>122</td> </tr> <tr style="text-align: center;"> <td>书生·浦语-文曲星-20B</td> <td>26</td> <td>14</td> <td>7</td> <td>6</td> <td>15</td> <td>43</td> <td>111</td> </tr> <tr style="text-align: center;"> <td>Yi-1.5-34B+VL-34B</td> <td>28</td> <td>12</td> <td>7</td> <td>0</td> <td>16</td> <td>46</td> <td>109</td> </tr> <tr style="text-align: center;"> <td>GLM4-9B+4v-9B</td> <td>24</td> <td>13</td> <td>8</td> <td>2</td> <td>15</td> <td>46</td> <td>108</td> </tr> <tr style="text-align: center;"> <td>Qwen2-57B</td> <td>27</td> <td>14</td> <td>7</td> <td>2</td> <td>14</td> <td>44</td> <td>108</td> </tr> <tr style="text-align: center;"> <td>Mixtral 8x22B</td> <td>24</td> <td>0</td> <td>7</td> <td>0</td> <td>14</td> <td>47</td> <td>92</td> </tr> </table>
语文试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">语文</th>
        <th rowspan="2">题号</th>
<th colspan="3">现代文阅读Ⅰ</th><th colspan="3">现代文阅读ⅠI</th><th colspan="3">现代文阅读Ⅲ</th><th colspan="4">文言文阅读</th><th colspan="2">古诗文阅读</th><th colspan="1">名篇名句默写</th><th colspan="4">语言文字运用Ⅰ</th><th colspan="1">语言文字运用ⅠI</th><th colspan="1">作文</th><th rowspan="2">总分</th></tr>
<tr style="text-align: center;"><th>1.1</th><th>1.2</th><th>1.3</th><th>2.1</th><th>2.2</th><th>2.3</th><th>3.1</th><th>3.2</th><th>3.3</th><th>4.1</th><th>4.2</th><th>4.3</th><th>4.4</th><th>5.1</th><th>5.2</th><th>6</th><th>7.1</th><th>7.2</th><th>7.3</th><th>7.4</th><th>7.5</th><th>8</th></tr><tr style="text-align: center;"><td>测试模型</td><td>分值</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>6</td><td>3</td><td>6</td><td>6</td><td>3</td><td>3</td><td>3</td><td>10</td><td>3</td><td>6</td><td>6</td><td>3</td><td>4</td><td>3</td><td>4</td><td>6</td><td>60</td><td>150	(100%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td></td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>6</td><td>3</td><td>6</td><td>6</td><td>3</td><td>3</td><td>3</td><td>10</td><td>3</td><td>6</td><td>2</td><td>3</td><td>4</td><td>0</td><td>2</td><td>6</td><td>48</td><td>128	(85.3%)</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td></td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>4</td><td>0</td><td>5</td><td>6</td><td>3</td><td>3</td><td>3</td><td>10</td><td>3</td><td>5</td><td>4</td><td>3</td><td>2</td><td>0</td><td>4</td><td>5</td><td>48</td><td>122	(81.3%)</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B</td><td></td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>4</td><td>0</td><td>3</td><td>5</td><td>3</td><td>3</td><td>0</td><td>8</td><td>3</td><td>4</td><td>6</td><td>3</td><td>4</td><td>0</td><td>4</td><td>4</td><td>43</td><td>111	(74%)</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B</td><td></td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>0</td><td>5</td><td>5</td><td>1</td><td>3</td><td>0</td><td>8</td><td>3</td><td>4</td><td>0</td><td>3</td><td>4</td><td>3</td><td>0</td><td>6</td><td>46</td><td>109	(72.7%)</td></tr><tr style="text-align: center;"><td>GLM4-9B</td><td></td><td>3</td><td>3</td><td>3</td><td>0</td><td>2</td><td>4</td><td>0</td><td>3</td><td>6</td><td>2</td><td>3</td><td>0</td><td>8</td><td>3</td><td>5</td><td>2</td><td>3</td><td>4</td><td>0</td><td>4</td><td>4</td><td>46</td><td>108	(72%)</td></tr><tr style="text-align: center;"><td>Qwen2-57B</td><td></td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td><td>2</td><td>5</td><td>3</td><td>0</td><td>3</td><td>8</td><td>3</td><td>4</td><td>2</td><td>3</td><td>4</td><td>0</td><td>2</td><td>5</td><td>44</td><td>108	(72%)</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>2</td><td>0</td><td>3</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>4</td><td>0</td><td>3</td><td>3</td><td>3</td><td>0</td><td>5</td><td>47</td><td>92	(61.3%)</td></tr></table>

## 数学(文)
数学(文)试卷各部分的得分如下所示
<table border="1">
<tr style="text-align: center;">
    <th colspan="6" style="text-align: center;">数学(文)各题型得分情况</th>
</tr>
<tr style="text-align: center;">
    <td>模型</td>
<td>单选题（满分60分）</td><td>填空题（满分20分）</td><td>简答题（满分60分）</td><td>选考题-简答题（满分20分）</td><td>总分（满分150）</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td>50</td><td>15</td><td>20</td><td>14</td><td>95</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td>40</td><td>15</td><td>24</td><td>10</td><td>89</td></tr><tr style="text-align: center;"><td>GLM4-9B</td><td>35</td><td>10</td><td>27</td><td>3</td><td>75</td></tr><tr style="text-align: center;"><td>Qwen2-57B</td><td>40</td><td>10</td><td>18</td><td>9</td><td>75</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B</td><td>30</td><td>15</td><td>26</td><td>0</td><td>71</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B</td><td>25</td><td>5</td><td>31</td><td>6</td><td>65</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td>30</td><td>5</td><td>15</td><td>3</td><td>53</td></tr></table>数学(文)试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">数学(文)</th>
        <th rowspan="2">题号</th>
<th colspan="12">单选题</th><th colspan="4">填空题</th><th colspan="5">简答题</th><th colspan="2">选考题-简答题</th><th rowspan="2">总分</th></tr>
<tr style="text-align: center;"><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th><th>21</th><th>22</th><th>23</th></tr><tr style="text-align: center;"><td>测试模型</td><td>分值</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>12</td><td>12</td><td>12</td><td>12</td><td>12</td><td>10</td><td>10</td><td>150	(100%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td></td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>9</td><td>0</td><td>9</td><td>2</td><td>10</td><td>4</td><td>95	(63.3%)</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td></td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>1</td><td>10</td><td>0</td><td>8</td><td>5</td><td>10</td><td>0</td><td>89	(59.3%)</td></tr><tr style="text-align: center;"><td>GLM4-9B</td><td></td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td><td>10</td><td>2</td><td>7</td><td>8</td><td>0</td><td>3</td><td>75	(50%)</td></tr><tr style="text-align: center;"><td>Qwen2-57B</td><td></td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>5</td><td>0</td><td>5</td><td>5</td><td>0</td><td>0</td><td>2</td><td>9</td><td>3</td><td>2</td><td>2</td><td>7</td><td>2</td><td>75	(50%)</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B</td><td></td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td><td>5</td><td>0</td><td>5</td><td>5</td><td>0</td><td>5</td><td>2</td><td>10</td><td>0</td><td>8</td><td>6</td><td>0</td><td>0</td><td>71	(47.3%)</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B</td><td></td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>4</td><td>9</td><td>0</td><td>12</td><td>6</td><td>4</td><td>2</td><td>65	(43.3%)</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>9</td><td>0</td><td>4</td><td>2</td><td>0</td><td>3</td><td>53	(35.3%)</td></tr></table>题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。




## 数学(理)
数学(理)试卷各部分的得分如下所示
<table border="1">
<tr style="text-align: center;">
    <th colspan="6" style="text-align: center;">数学(理)各题型得分情况</th>
</tr>
<tr style="text-align: center;">
    <td>模型</td>
<td>单选题（满分60分）</td><td>填空题（满分20分）</td><td>简答题（满分60分）</td><td>选考题-简答题（满分20分）</td><td>总分（满分150）</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td>50</td><td>10</td><td>19</td><td>15</td><td>89</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td>35</td><td>15</td><td>27</td><td>12</td><td>84</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B</td><td>35</td><td>5</td><td>38</td><td>0</td><td>78</td></tr><tr style="text-align: center;"><td>GLM4-9B</td><td>35</td><td>5</td><td>28</td><td>3</td><td>71</td></tr><tr style="text-align: center;"><td>Qwen2-57B</td><td>40</td><td>5</td><td>13</td><td>13</td><td>65</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td>30</td><td>0</td><td>21</td><td>12</td><td>58</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B</td><td>20</td><td>0</td><td>17</td><td>2</td><td>39</td></tr></table>数学(理)试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">数学(理)</th>
        <th rowspan="2">题号</th>
<th colspan="12">单选题</th><th colspan="4">填空题</th><th colspan="5">简答题</th><th colspan="2">选考题-简答题</th><th rowspan="2">总分</th></tr>
<tr style="text-align: center;"><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th><th>21</th><th>22</th><th>23</th></tr><tr style="text-align: center;"><td>测试模型</td><td>分值</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>12</td><td>12</td><td>12</td><td>12</td><td>12</td><td>10</td><td>10</td><td>150	(100%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td></td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>0</td><td>4</td><td>7</td><td>0</td><td>4</td><td>4</td><td>10</td><td>5</td><td>89	(59.3%)</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td></td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>10</td><td>2</td><td>0</td><td>5</td><td>10</td><td>7</td><td>5</td><td>84	(56%)</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B</td><td></td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td><td>5</td><td>0</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>10</td><td>6</td><td>4</td><td>8</td><td>10</td><td>0</td><td>0</td><td>78	(52%)</td></tr><tr style="text-align: center;"><td>GLM4-9B</td><td></td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>4</td><td>7</td><td>0</td><td>12</td><td>5</td><td>0</td><td>3</td><td>71	(47.3%)</td></tr><tr style="text-align: center;"><td>Qwen2-57B</td><td></td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td><td>6</td><td>0</td><td>0</td><td>2</td><td>5</td><td>7</td><td>6</td><td>65	(43.3%)</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>5</td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>6</td><td>9</td><td>0</td><td>2</td><td>4</td><td>5</td><td>7</td><td>58	(38.7%)</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B</td><td></td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>6</td><td>1</td><td>0</td><td>6</td><td>4</td><td>2</td><td>0</td><td>39	(26%)</td></tr></table>题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。

## 英语
英语试卷各部分的得分如下所示
<table border="1"> <tr style="text-align: center;"> <th colspan="8" style="text-align: center;">英语各题型得分情况</th> </tr> <tr style="text-align: center;"> <td>模型</td> <td>阅读理解（满分30分）</td> <td>7选5（满分10分）</td> <td>完形填空（满分30分）</td> <td>语法补全（满分15分）</td> <td>写作（满分35分）</td> <td>听力（满分30分）</td> <td>总分（满分150）</td> </tr> <tr style="text-align: center;"> <td>GPT-4o</td> <td>30</td> <td>10</td> <td>28.5</td> <td>15</td> <td>29</td> <td>30</td> <td>142.5</td> </tr> <tr style="text-align: center;"> <td>Mixtral 8x22B</td> <td>30</td> <td>10</td> <td>30</td> <td>15</td> <td>27</td> <td>30</td> <td>142</td> </tr> <tr style="text-align: center;"> <td>Qwen2-72B</td> <td>30</td> <td>10</td> <td>30</td> <td>15</td> <td>26</td> <td>30</td> <td>141</td> </tr> <tr style="text-align: center;"> <td>书生·浦语-文曲星-20B</td> <td>30</td> <td>10</td> <td>28.5</td> <td>15</td> <td>27.5</td> <td>30</td> <td>141</td> </tr> <tr style="text-align: center;"> <td>Qwen2-57B</td> <td>28</td> <td>10</td> <td>30</td> <td>15</td> <td>28</td> <td>30</td> <td>141</td> </tr> <tr style="text-align: center;"> <td>GLM4-9B</td> <td>26</td> <td>0</td> <td>21</td> <td>12</td> <td>21.5</td> <td>30</td> <td>110.5</td> </tr> <tr style="text-align: center;"> <td>Yi-1.5-34B</td> <td>24</td> <td>8</td> <td>16.5</td> <td>13.5</td> <td>15.5</td> <td>30</td> <td>107.5</td> </tr> </table>

英语试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">英语</th>
        <th rowspan="2">题号</th>
        <th colspan="1">阅读理解A</th>
        <th colspan="1">阅读理解B</th>
        <th colspan="1">阅读理解C</th>
        <th colspan="1">阅读理解D</th>
        <th colspan="1">7选5</th>
        <th colspan="1">完形填空</th>
        <th colspan="1">语法补全</th>
        <th colspan="1">写作-短文改错</th>
        <th colspan="1">写作-书面表达</th>
        <th colspan="1">听力</th>
        <th rowspan="2">总分</th>
    </tr>
    <tr style="text-align: center;">
        <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th>
    </tr>
    <tr style="text-align: center;">
        <td>测试模型</td><td>分值</td><td>6</td><td>8</td><td>8</td><td>8</td><td>10</td><td>30</td><td>15</td><td>10</td><td>25</td><td>30</td><td>150 (100%)</td>
    </tr>
    <tr style="text-align: center;"><td>GPT-4o</td><td></td><td>6</td><td>8</td><td>8</td><td>8</td><td>10</td><td>28.5</td><td>15</td><td>8</td><td>21</td><td>30</td><td>142.5 (95%)</td></tr>
    <tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>6</td><td>8</td><td>8</td><td>8</td><td>10</td><td>30</td><td>15</td><td>8</td><td>19</td><td>30</td><td>142 (94.7%)</td></tr>
    <tr style="text-align: center;"><td>Qwen2-72B</td><td></td><td>6</td><td>8</td><td>8</td><td>8</td><td>10</td><td>30</td><td>15</td><td>8</td><td>18</td><td>30</td><td>141 (94%)</td></tr>
    <tr style="text-align: center;"><td>书生·浦语-文曲星-20B</td><td></td><td>6</td><td>8</td><td>8</td><td>8</td><td>10</td><td>28.5</td><td>15</td><td>9</td><td>18.5</td><td>30</td><td>141 (94%)</td></tr>
    <tr style="text-align: center;"><td>Qwen2-57B</td><td></td><td>6</td><td>8</td><td>6</td><td>8</td><td>10</td><td>30</td><td>15</td><td>9</td><td>19</td><td>30</td><td>141 (94%)</td></tr>
    <tr style="text-align: center;"><td>GLM4-9B</td><td></td><td>6</td><td>8</td><td>6</td><td>6</td><td>0</td><td>21</td><td>12</td><td>6</td><td>15.5</td><td>30</td><td>110.5 (73.7%)</td></tr>
    <tr style="text-align: center;"><td>Yi-1.5-34B</td><td></td><td>4</td><td>8</td><td>6</td><td>6</td><td>8</td><td>16.5</td><td>13.5</td><td>5</td><td>10.5</td><td>30</td><td>107.5 (71.7%)</td></tr>
</table>




## 物理
物理试卷各部分的得分如下所示
<table border="1">
<tr style="text-align: center;">
    <th colspan="7" style="text-align: center;">物理各题型得分情况</th>
</tr>
<tr style="text-align: center;">
    <td>模型</td>
<td>单选题（满分48分）</td><td>填空题（满分15分）</td><td>简答题（满分32分）</td><td>选考题-选择题（满分10分）</td><td>选考题（满分20分）</td><td>总分（满分110）</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td>27</td><td>1</td><td>9</td><td>1</td><td>0</td><td>38</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td>18</td><td>1</td><td>9</td><td>0</td><td>4</td><td>32</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td>15</td><td>5</td><td>10</td><td>1</td><td>0</td><td>31</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td>24</td><td>1</td><td>4</td><td>1</td><td>0</td><td>30</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td>18</td><td>2</td><td>6</td><td>2</td><td>1</td><td>29</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td>12</td><td>2</td><td>8</td><td>0</td><td>0</td><td>22</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td>9</td><td>0</td><td>6</td><td>0</td><td>0</td><td>15</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td>0</td><td>2</td><td>4</td><td>0</td><td>0</td><td>6</td></tr></table>物理试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">物理</th>
        <th rowspan="2">题号</th>
<th colspan="8">单选题</th><th colspan="2">填空题</th><th colspan="2">简答题</th><th colspan="2">选考题-选择题</th><th colspan="2">选考题</th><th rowspan="2">总分</th><th rowspan="2">带图题总分</th><th rowspan="2">不带图题总分</th></tr>
<tr style="text-align: center;"><th>1</th><th>2*</th><th>3</th><th>4*</th><th>5*</th><th>6*</th><th>7*</th><th>8*</th><th>9*</th><th>10*</th><th>11</th><th>12*</th><th>13.1</th><th>13.2</th><th>14.1</th><th>14.2</th></tr><tr style="text-align: center;"><td>测试模型</td><td>分值</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>5</td><td>10</td><td>12</td><td>20</td><td>5</td><td>10</td><td>5</td><td>10</td><td>110	(100%)</td><td>71	(65%)</td><td>39	(35%)</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>0</td><td>6</td><td>6</td><td>6</td><td>6</td><td>3</td><td>0</td><td>0</td><td>1</td><td>0</td><td>4</td><td>5</td><td>0</td><td>0</td><td>1</td><td>0</td><td>38	(34.5%)</td><td>27	(38%)</td><td>11	(28.2%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td></td><td>6</td><td>0</td><td>6</td><td>0</td><td>0</td><td>3</td><td>3</td><td>0</td><td>1</td><td>0</td><td>6</td><td>3</td><td>1</td><td>1</td><td>0</td><td>4</td><td>33	(30%)</td><td>10	(14.1%)</td><td>23	(61.5%)</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td></td><td>6</td><td>0</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>3</td><td>2</td><td>7</td><td>3</td><td>1</td><td>0</td><td>0</td><td>0</td><td>31	(28.2%)</td><td>11	(15.5%)</td><td>20	(51.3%)</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td></td><td>6</td><td>0</td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>6</td><td>1</td><td>0</td><td>4</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>30	(27.3%)</td><td>13	(18.3%)</td><td>17	(43.6%)</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td></td><td>6</td><td>0</td><td>6</td><td>0</td><td>0</td><td>3</td><td>0</td><td>3</td><td>0</td><td>2</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0</td><td>0</td><td>29	(26.4%)</td><td>10	(14.1%)</td><td>19	(48.7%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td></td><td>6</td><td>0</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>22	(20%)</td><td>2	(2.8%)</td><td>20	(51.3%)</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>3</td><td>3</td><td>0</td><td>0</td><td>4</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>15	(13.6%)</td><td>11	(15.5%)</td><td>4	(10.3%)</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>6	(5.5%)</td><td>2	(2.8%)</td><td>4	(10.3%)</td></tr></table>题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。
## 化学
化学试卷各部分的得分如下所示
<table border="1">
<tr style="text-align: center;">
    <th colspan="5" style="text-align: center;">化学各题型得分情况</th>
</tr>
<tr style="text-align: center;">
    <td>模型</td>
<td>单选题（满分42分）</td><td>填空题（满分43分）</td><td>选考题-填空题（满分30分）</td><td>总分（满分100）</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td>30</td><td>15</td><td>10</td><td>52</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td>24</td><td>13</td><td>13</td><td>48</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td>24</td><td>15</td><td>7</td><td>44</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td>24</td><td>13</td><td>4</td><td>40</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td>24</td><td>8</td><td>7</td><td>39</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td>12</td><td>14</td><td>8</td><td>34</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td>12</td><td>7</td><td>5</td><td>22</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td>12</td><td>7</td><td>5</td><td>22</td></tr></table>化学试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">化学</th>
        <th rowspan="2">题号</th>
<th colspan="7">单选题</th><th colspan="3">填空题</th><th colspan="2">选考题-填空题</th><th rowspan="2">总分</th><th rowspan="2">带图题总分</th><th rowspan="2">不带图题总分</th></tr>
<tr style="text-align: center;"><th>1</th><th>2</th><th>3*</th><th>4*</th><th>5</th><th>6*</th><th>7*</th><th>8*</th><th>9*</th><th>10*</th><th>11*</th><th>12*</th></tr><tr style="text-align: center;"><td>测试模型</td><td>分值</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>14</td><td>14</td><td>15</td><td>15</td><td>15</td><td>100	(100%)</td><td>82	(82%)</td><td>18	(18%)</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>6</td><td>6</td><td>0</td><td>4</td><td>8</td><td>3</td><td>7</td><td>3</td><td>52	(52%)</td><td>37	(45.1%)</td><td>15	(100%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>0</td><td>6</td><td>0</td><td>3</td><td>8</td><td>2</td><td>11</td><td>2</td><td>48	(48%)</td><td>38	(46.3%)</td><td>10	(66.7%)</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>6</td><td>0</td><td>0</td><td>5</td><td>7</td><td>3</td><td>5</td><td>2</td><td>44	(44%)</td><td>28	(34.1%)</td><td>16	(100%)</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>0</td><td>6</td><td>0</td><td>3</td><td>5</td><td>5</td><td>3</td><td>1</td><td>40	(40%)</td><td>29	(35.4%)</td><td>11	(66.7%)</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>0</td><td>6</td><td>0</td><td>2</td><td>2</td><td>4</td><td>7</td><td>0</td><td>39	(39%)</td><td>27	(32.9%)</td><td>12	(66.7%)</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td></td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>6</td><td>5</td><td>3</td><td>8</td><td>0</td><td>34	(34%)</td><td>22	(26.8%)</td><td>12	(66.7%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td></td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>3</td><td>2</td><td>3</td><td>2</td><td>22	(22%)</td><td>12	(14.6%)</td><td>10	(66.7%)</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td></td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>3</td><td>2</td><td>3</td><td>2</td><td>22	(22%)</td><td>12	(14.6%)</td><td>10	(66.7%)</td></tr></table>题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。

## 生物

生物试卷各部分的得分如下所示

<table border="1">
<tr style="text-align: center;">
    <th colspan="5" style="text-align: center;">生物各题型得分情况</th>
</tr>
<tr style="text-align: center;">
    <td>模型</td>
<td>单选题（满分36分）</td><td>填空题（满分39分）</td><td>选考题-填空题（满分30分）</td><td>总分（满分90）</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td>30</td><td>27</td><td>23</td><td>72</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td>30</td><td>10.5</td><td>26</td><td>55.5</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td>24</td><td>16</td><td>19</td><td>55</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td>18</td><td>21</td><td>24</td><td>54</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td>18</td><td>17</td><td>15</td><td>50</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td>18</td><td>21</td><td>21</td><td>50</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td>18</td><td>11</td><td>15</td><td>44</td></tr></table>生物试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">生物</th>
        <th rowspan="2">题号</th>
<th colspan="6">单选题</th><th colspan="4">填空题</th><th colspan="2">选考题-填空题</th><th rowspan="2">总分</th><th rowspan="2">带图题总分</th><th rowspan="2">不带图题总分</th></tr>
<tr style="text-align: center;"><th>1</th><th>2</th><th>3</th><th>4*</th><th>5</th><th>6*</th><th>7</th><th>8*</th><th>9*</th><th>10</th><th>11</th><th>12*</th></tr><tr style="text-align: center;"><td>测试模型</td><td>分值</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>10</td><td>10</td><td>9</td><td>10</td><td>15</td><td>15</td><td>90	(100%)</td><td>31	(34%)</td><td>59	(66%)</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td></td><td>6</td><td>6</td><td>6</td><td>6</td><td>0</td><td>6</td><td>8</td><td>4</td><td>5</td><td>10</td><td>15</td><td>8</td><td>72	(80%)</td><td>29	(93.5%)</td><td>43	(86.4%)</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td></td><td>6</td><td>6</td><td>6</td><td>6</td><td>0</td><td>6</td><td>4</td><td>4.5</td><td>2</td><td>0</td><td>15</td><td>11</td><td>55.5	(61.7%)</td><td>29.5	(95.2%)</td><td>26	(62.7%)</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>0</td><td>6</td><td>4</td><td>3</td><td>3</td><td>6</td><td>15</td><td>4</td><td>55	(61.1%)</td><td>16	(51.6%)</td><td>39	(72.9%)</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>0</td><td>6</td><td>6</td><td>0</td><td>0</td><td>6</td><td>6</td><td>4</td><td>5</td><td>6</td><td>15</td><td>9</td><td>54	(60%)</td><td>24	(77.4%)</td><td>30	(66.1%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>8</td><td>3</td><td>0</td><td>6</td><td>15</td><td>0</td><td>50	(55.6%)</td><td>3	(9.7%)</td><td>47	(79.7%)</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>4</td><td>8</td><td>5</td><td>4</td><td>11</td><td>10</td><td>50	(55.6%)</td><td>23	(74.2%)</td><td>27	(62.7%)</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td></td><td>6</td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>4</td><td>3</td><td>0</td><td>4</td><td>15</td><td>0</td><td>44	(48.9%)</td><td>3	(9.7%)</td><td>41	(69.5%)</td></tr></table>题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。

## 历史
历史试卷各部分的得分如下所示
<table border="1">
<tr style="text-align: center;">
    <th colspan="4" style="text-align: center;">历史各题型得分情况</th>
</tr>
<tr style="text-align: center;">
    <td>模型</td>
<td>单选题（满分48分）</td><td>简答题（满分52分）</td><td>总分（满分100）</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td>36</td><td>46</td><td>82</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td>40</td><td>37</td><td>77</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td>40</td><td>36</td><td>76</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td>36</td><td>38</td><td>74</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td>32</td><td>39</td><td>71</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td>20</td><td>34</td><td>54</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td>20</td><td>33</td><td>53</td></tr></table>历史试卷中每个小题得分情况如下所示
<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">历史</th>
        <th rowspan="2">题号</th>
<th colspan="12">单选题</th><th colspan="3">简答题</th><th rowspan="2">总分</th><th rowspan="2">带图题总分</th><th rowspan="2">不带图题总分</th></tr>
<tr style="text-align: center;"><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14*</th><th>15</th></tr><tr style="text-align: center;"><td>测试模型</td><td>分值</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>25</td><td>12</td><td>15</td><td>100	(100%)</td><td>12	(12%)</td><td>88	(88%)</td></tr><tr style="text-align: center;"><td>GPT-4o</td><td></td><td>4</td><td>0</td><td>0</td><td>0</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>23</td><td>10</td><td>13</td><td>82	(82%)</td><td>10	(83.3%)</td><td>72	(81.8%)</td></tr><tr style="text-align: center;"><td>Qwen2-57B+VL-7B</td><td></td><td>4</td><td>4</td><td>0</td><td>0</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>21</td><td>4</td><td>12</td><td>77	(77%)</td><td>4	(33.3%)</td><td>73	(83%)</td></tr><tr style="text-align: center;"><td>书生·浦语-文曲星-20B+VL-20B</td><td></td><td>4</td><td>0</td><td>0</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>17</td><td>8</td><td>11</td><td>76	(76%)</td><td>8	(66.7%)</td><td>68	(77.3%)</td></tr><tr style="text-align: center;"><td>Mixtral 8x22B</td><td></td><td>0</td><td>4</td><td>4</td><td>0</td><td>4</td><td>4</td><td>0</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>22</td><td>7</td><td>9</td><td>74	(74%)</td><td>7	(58.3%)</td><td>67	(76.1%)</td></tr><tr style="text-align: center;"><td>Qwen2-72B+VL-7B</td><td></td><td>4</td><td>0</td><td>4</td><td>0</td><td>4</td><td>4</td><td>0</td><td>4</td><td>4</td><td>0</td><td>4</td><td>4</td><td>21</td><td>4</td><td>14</td><td>71	(71%)</td><td>4	(33.3%)</td><td>67	(76.1%)</td></tr><tr style="text-align: center;"><td>GLM4-9B+4v-9B</td><td></td><td>4</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td><td>4</td><td>4</td><td>17</td><td>4</td><td>13</td><td>54	(54%)</td><td>4	(33.3%)</td><td>50	(56.8%)</td></tr><tr style="text-align: center;"><td>Yi-1.5-34B+VL-34B</td><td></td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>4</td><td>0</td><td>4</td><td>0</td><td>4</td><td>20</td><td>4</td><td>9</td><td>53	(53%)</td><td>4	(33.3%)</td><td>49	(55.7%)</td></tr></table>题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。



## 地理

地理试卷各部分的得分如下所示
<table border="1">
<tr style="text-align: center;">
    <th colspan="5" style="text-align: center;">地理各题型得分情况</th>
</tr>
<tr style="text-align: center;">
    <td>模型</td>
    <td>单选题（满分44分）</td>
    <td>简答题（满分46分）</td>
    <td>选考题-简答题（满分10分）</td>
    <td>总分（满分100）</td>
</tr>
<tr style="text-align: center;">
    <td>Qwen2-72B</td>
    <td>40</td>
    <td>31</td>
    <td>10</td>
    <td>81</td>
</tr>
<tr style="text-align: center;">
    <td>Mixtral 8x22B</td>
    <td>36</td>
    <td>30</td>
    <td>8</td>
    <td>74</td>
</tr>
<tr style="text-align: center;">
    <td>GPT-4o</td>
    <td>32</td>
    <td>24</td>
    <td>10</td>
    <td>66</td>
</tr>
<tr style="text-align: center;">
    <td>书生·浦语-文曲星-20B+VL-20B</td>
    <td>24</td>
    <td>36</td>
    <td>4</td>
    <td>64</td>
</tr>
<tr style="text-align: center;">
    <td>GLM4-9B+4v-9B</td>
    <td>24</td>
    <td>28</td>
    <td>10</td>
    <td>62</td>
</tr>
<tr style="text-align: center;">
    <td>Yi-1.5-34B+VL-34B</td>
    <td>28</td>
    <td>16</td>
    <td>10</td>
    <td>54</td>
</tr>
<tr style="text-align: center;">
    <td>Qwen2-72B+VL-7B</td>
    <td>24</td>
    <td>0</td>
    <td>10</td>
    <td>34</td>
</tr>
<tr style="text-align: center;">
    <td>Qwen2-57B+VL-7B</td>
    <td>16</td>
    <td>0</td>
    <td>14</td>
    <td>30</td>
</tr>
</table>

地理试卷中每个小题得分情况如下所示

<table border="1">
    <tr style="text-align: center;">
        <th rowspan="2">地理</th>
        <th rowspan="2">题号</th>
        <th colspan="11">单选题</th>
        <th colspan="8">简答题</th>
        <th colspan="2">选考题-简答题</th>
        <th rowspan="2">总分</th>
        <th rowspan="2">带图题总分</th>
        <th rowspan="2">不带图题总分</th>
    </tr>
    <tr style="text-align: center;">
        <th>1*</th><th>2*</th><th>3*</th><th>4</th><th>5</th><th>6*</th>
        <th>7*</th><th>8*</th><th>9*</th><th>10*</th><th>11*</th>
        <th>12.1*</th><th>12.2*</th><th>12.3*</th><th>12.4*</th>
        <th>13.1*</th><th>13.2*</th><th>13.3*</th><th>13.4*</th>
        <th>14</th><th>15</th>
    </tr>
    <tr style="text-align: center;">
        <td>测试模型</td><td>分值</td>
        <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
        <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
        <td>6</td><td>6</td><td>6</td><td>6</td><td>6</td>
        <td>4</td><td>8</td><td>4</td><td>10</td><td>10</td>
        <td>100 (100%)</td><td>82 (82%)</td><td>18 (100%)</td>
    </tr>
    <tr style="text-align: center;">
        <td>Qwen2-72B</td><td></td>
        <td>4</td><td>4</td><td>0</td><td>4</td><td>4</td><td>4</td>
        <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
        <td>6</td><td>2</td><td>6</td><td>6</td><td>1</td>
        <td>2</td><td>4</td><td>4</td><td>10</td><td>10</td>
        <td>81 (81%)</td><td>63 (76.8%)</td><td>18 (100%)</td>
    </tr>
    <tr style="text-align: center;">
        <td>Mixtral 8x22B</td><td></td>
        <td>4</td><td>4</td><td>0</td><td>4</td><td>0</td><td>4</td>
        <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
        <td>6</td><td>2</td><td>2</td><td>6</td><td>6</td>
        <td>0</td><td>4</td><td>4</td><td>5</td><td>8</td>
        <td>74 (74%)</td><td>62 (75.6%)</td><td>12 (66.7%)</td>
    </tr>
    <tr style="text-align: center;">
        <td>GPT-4o</td><td></td>
        <td>0</td><td>4</td><td>0</td><td>4</td><td>4</td><td>4</td>
        <td>0</td><td>4</td><td>4</td><td>4</td><td>4</td>
        <td>0</td><td>2</td><td>4</td><td>6</td><td>0</td>
        <td>4</td><td>4</td><td>4</td><td>10</td><td>10</td>
        <td>66 (66%)</td><td>48 (58.5%)</td><td>18 (100%)</td>
    </tr>
    <tr style="text-align: center;">
      <td>书生·浦语-文曲星-20B+VL-20B</td><td></td>
      <td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
      <td>4</td><td>2</td><td>6</td><td>6</td><td>6</td>
      <td>4</td><td>4</td><td>4</td><td>0</td><td>4</td>
      <td>64 (64%)</td><td>56 (68.3%)</td><td>8 (42.1%)</td>
    </tr>
    <tr style="text-align: center;">
        <td>GLM4-9B+4v-9B</td><td></td>
        <td>4</td><td>4</td><td>0</td><td>4</td><td>0</td><td>0</td>
        <td>4</td><td>4</td><td>4</td><td>0</td><td>0</td>
        <td>4</td><td>2</td><td>6</td><td>6</td><td>2</td>
        <td>4</td><td>2</td><td>2</td><td>10</td><td>10</td>
        <td>62 (62%)</td><td>48 (58.5%)</td><td>14 (77.8%)</td>
    </tr>
    <tr style="text-align: center;">
        <td>Yi-1.5-34B+VL-34B</td><td></td>
        <td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td>
        <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
        <td>4</td><td>2</td><td>4</td><td>6</td><td>0</td>
        <td>0</td><td>0</td><td>0</td><td>10</td><td>10</td>
        <td>54 (54%)</td><td>44 (53.7%)</td><td>10 (55.6%)</td>
    </tr>
    <tr style="text-align: center;">
        <td>Qwen2-72B+VL-7B</td><td></td>
        <td>0</td><td>0</td><td>0</td><td>4</td><td>4</td><td>0</td>
        <td>4</td><td>4</td><td>0</td><td>4</td><td>4</td>
        <td>0</td><td>0</td><td>0</td><td>0</td><td>0</td>
        <td>0</td><td>0</td><td>0</td><td>10</td><td>10</td>
        <td>34 (34%)</td><td>16 (19.5%)</td><td>18 (100%)</td>
    </tr>
    <tr style="text-align: center;">
        <td>Qwen2-57B+VL-7B</td><td></td>
        <td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td>
        <td>4</td><td>4</td><td>0</td><td>4</td><td>4</td>
        <td>0</td><td>0</td><td>0</td><td>0</td><td>0</td>
        <td>0</td><td>0</td><td>0</td><td>10</td><td>10</td>
        <td>30 (30%)</td><td>16 (19.5%)</td><td>14 (77.8%)</td>
    </tr>
</table>
题号带星号（*）的表示题目包含图片，如果模型名称中含有“+VL”的字样表明，涉及到图片的题目会使用相应的多模态版本模型进行推理；如果没有“+VL”的字样，则只进行不看图的纯文本推理。




## 老师整体点评
在改完所有的科目之后，我们告知了以上试卷的回答由大模型生成，然后我们邀请阅卷老师对7个大模型整体的表现进行了点评。

**语文老师点评**：   
大模型进行文言文翻译问题不大，但主观题大部分审题失败，读不懂题，对题目中某些代词的指向不太明确导致答非所问。大模型写作文都不太像高考作文更像问答题，虽然有针对性但缺乏修饰，人类考生都会使用举例论证、引用论证，习惯用名人名言和人物素材，但是大模型写作文时几乎都没用过。写一个暗喻的句子，大模型几乎全军覆没，本体喻体都搞错了，大模型似乎不懂得“暗喻”手法是什么，都写成了普通的“比喻”，也不懂得“本体”是什么。补写句子也不太能写对，看来对于与上下文语意的衔接、中文中的一些语言习惯(补写句子中后文出现了一个新的概念，如“睡眠质量”，那么补写的这个句子中应该要出现这个概念，否则后文突然提起就很突兀，衔接不紧密)，语言中的一些“潜台词”，大模型还不能完全明白。

**文科数学老师点评**：  
客观题大多数题目分析正确，一小部分题分析的过程的结果与题目选项不一致，仍能得出与题目选项不一致的选项。主观题大部分做不到第二问，并且回答内容以分析为主，过程有些简易。并且在解答过程中出现错误，会重复此项代码；如17题，大部分都能求出an，后面写的内容跟真人写的完全不同；18题，大部分计算K方列式正确，计算结果错误；19题，部分题目解答过程中自己编造已知条件，缺少具体的书写内容；后面几何题，能从图上看出解答过程中明显的垂直平行问题，几乎是非常离谱的推理过程；后面不等式证明，自己增加已知条件，并通过自己的已知条件进行证明。整体主观题缺少逻辑思维。

**理科数学老师点评**：  
大模型做题总体感觉很机械，大部分题目都无法通过正常的推理过程得出。例如填空题第一题，大模型都只能进行到少部分过程而达到一个结果，并不能够像考生做题一样进行全面分析，列出完整的计算过程达到正确结果。此外，对于几何题，大模型对于平面几何题的证明过程过于离谱，对于立体几何的计算并非会同考生一样利用正常的计算方法求解。大模型的基础公式记忆能力较为优秀，但无法做到灵活使用。此外有些题目结果正确，但过程逻辑差不符合正规计算，导致阅卷比较困难。

**英语老师点评**：  
在完成情况上，大模型基本上可以完成题目要求。但是也不可避免会出现问题，首先是在题目过长的情况下，可能会无法识别出问题，导致未作答的现象发生。其次是部分试卷没有按照题目要求作答，比如在完成作文时，没有按照要求写明题目和首句；以及在完成改错时，没有写明错误的地方，而是直接呈现修改好的文章。再者是在批阅时，也看到了大模型对于题目的解析，题目的解析与正常考生的解答思路不太一致，语言充满套话，格式过于规范化，大模型的制作过于明显。

**政治老师点评**：  
大模型整体选择题做的正确率不高，简答题答题太机械，尤其是第一个简答题，人大主体这道题答的最差，没有一个模型写到了书本知识点。不会结合书本知识点，离开书本理论知识点在机械重复材料话。其次是不能够审清楚题目，这是所有模型试卷的共性，不知道题目设问的角度是需要进一步分析的，比如问的是什么题型？是意义类的，原因类的，还是措施类的，答题不够规范。最后部分题目得分较好就是机械类的回答知识点，比如辩证思维这道题目，得分较好，因为这种题目本身就是知识点范围较小，在考试中也是属于送分题。

**历史老师点评**：  
试卷特点：注重材料分析，立足课本,注重考察能力，贯穿了“试题在书外，答案在材料中”的思想，强调对重大事件、线索的识记和历史现象对应的结论的理解，重视对学科主干知识和基本能力进行考查，属于识记层次的内容占50%左右,属于理解加识记层面的同样也占50%左右。
知识覆盖面广,包括课本上一些细节问题的考察十分详细
答题存在问题：
基础知识掌握的较好，但缺乏对有效信息的分析能力，对题目的理解较差，不能灵活的运用所学知识解决相关问题，答题习惯和方式上急需提高，语言表达能力依旧较差,口语化严重。

(1)模型答题对题目的理解较差，阅读理解能力还有待提高，尤其是不会从材料中提取有效信息作为试题的答案，难以抓住考察重点。

(2)答题格式较差，简答题写成小作文，没有分条答题的习惯。

(3)对于书本上的基础知识掌握不牢，记忆不准确。

(4)做题的思路不清晰，没有紧扣材料分析。会写一些无关紧要的信息
15题和17题答的较好，分数普遍都很高，小作文较差，不认真读题，要先回答问题之后才进行论述，不能鲜明的表明自己的观点，格式问题很大，字数不够或者太多。

**地理老师点评**：  
大模型在答题过程中展现了对地理知识的全面覆盖，从自然地理到人文地理，从地理现象到地理规律，都能有所涉及。尤其在基础知识点的考察上较为出色，然而，在涉及一些深入分析或推理的问题中，存在一定的偏差和遗漏，所以模型在面对非常规、开放性较强的问题时，其表现较差。

**物理老师点评**：  
大模型总体感觉比较机械，很多都无法识别到题目的意思，有些选择题即使选项对了，但是分析也是错误的。并且在一些读数的问题上尤为容易出错，给出的答案与正确答案相差较大。一些大题步骤冗杂，并且没有逻辑，常常出现将本次的结论带入到推理出本次结论的证据中，如此循环，没有道理。并且在步骤的规范上也有所欠缺，常常出现跳步的现象
整份卷好几道题都因为没有给到具体数据而只写分析过程不求解，但高中物理中用字母表达结果是最常见的体型。
选择题有不选答案的情况。
实验读数部分全都是假设未知数，没有具体数值。这些都是学生做题不会出现的低级错误。

**化学老师点评**：  
综合成绩来看，大模型准确率较低。在选择题目上，有题目识别不全面的问题，后四道逻辑性较强的题目无法正确作答；填空题现象作答精准猜中得分点的很少，方程式书写基本上没有准确率，且存在乱码现象，没有逻辑思维能力，综合有机、无机元素等逻辑较强题目，不能准确作答。

**生物老师点评**：  
大模型客观选择题带有图形的题型基本错误，部分单选题识别成了多选题，主观题部分对于基因型数量等需要计算的部分答案容易出错，不能完全理解题干意思，对带有图的题型错误率更高，部分题目答案出现乱码，不能举出题目所需的多个项。
