# 新课标I卷摘要
新课标I卷覆盖的省份主要包括广东、福建、湖北、湖南、江苏、河北、山东、浙江、江西、安徽、河南，本次测试使用新课标I卷的语数外三门考卷。

# 评测
在评测过程中，模型的回答被随机命名为A、B、C、D、E、F、G提供给老师进行打分，在打分时依照以下标准打分
- 各科目的单选题、填空题和答案是否完全一致才得分；
- 数学中多选题按照正确选项个数比例给分，如果有错误选项则直接不给分；
- 主观题根据步骤正确性会提供步骤分；
- 作文题根据作文给分标准进行打分；
此外为了保证模型结果可复现，除了作文以外，所有的答案均由各个模型通过贪婪解码生成。

## 总分情况
参加考试的模型总分情况如下所示


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
      <td>阿里 千问2-72B</td>
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
      <td>阿里 千问2-57B</td>
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


## 语文

语文试卷各部分的得分如下所示
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th colspan="8"  style="text-align: center;">语文各题型得分情况</th> 
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>模型</td>
      <td>现代文阅读（满分35分）</td>
      <td>文言文阅读（满分22分）</td>
      <td>古诗文阅读（满分9分）</td>
      <td>名句默写（满分6分）</td>
      <td>语言文字运用（满分18分）</td>
      <td>作文（满分60分）</td>
      <td>总分（满分150）</td>
    </tr>
    <tr>
      <td>阿里 千问2-72B</td>
      <td>31</td>
      <td>19</td>
      <td>9</td>
      <td>6</td>
      <td>9</td>
      <td>50</td>
      <td>124</td>
    </tr>
    <tr>
      <td>上海人工智能实验室 书生·浦语-文曲星-20B</td>
      <td>30</td>
      <td>17</td>
      <td>6</td>
      <td>6</td>
      <td>7</td>
      <td>46</td>
      <td>112</td>
    </tr>
    <tr>
      <td>OpenAI GPT-4o</td>
      <td>32</td>
      <td>10</td>
      <td>8</td>
      <td>2</td>
      <td>9</td>
      <td>50.5</td>
      <td>111.5</td>
    </tr>
    <tr>
      <td>阿里 千问2-57B</td>
      <td>27</td>
      <td>12</td>
      <td>7</td>
      <td>6</td>
      <td>2</td>
      <td>45.5</td>
      <td>99.5</td>
    </tr>        
    <tr>
      <td>零一万物 Yi-1.5-34B</td>
      <td>28</td>
      <td>8</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>50</td>
      <td>97</td>
    </tr>
    <tr>
      <td>智谱 GLM4-9B</td>
      <td>21</td>
      <td>6</td>
      <td>8</td>
      <td>6</td>
      <td>4</td>
      <td>41</td>
      <td>86</td>
    </tr>
    <tr>
      <td>Mistral Mixtral 8x22B</td>
      <td>18</td>
      <td>3</td>
      <td>7</td>
      <td>2</td>
      <td>3</td>
      <td>44.5</td>
      <td>77.5</td>
    </tr>
  </tbody>
</table>

语文试卷中每个小题得分情况如下所示

<table border="1">
    <tr>
        <th rowspan="2">语文</th>
        <th rowspan="2">题号</th>
<th colspan="5">现代文阅读Ⅰ</th><th colspan="4">现代文阅读ⅠⅠ</th><th colspan="5">文言文阅读</th><th colspan="2">古诗文阅读</th><th colspan="1">名篇名句默写</th><th colspan="5">语言文字运用</th><th colspan="1">作文</th><th rowspan="2">总分</th></tr>
<tr><th>1.1</th><th>1.2</th><th>1.3</th><th>1.4</th><th>1.5</th><th>2.1</th><th>2.2</th><th>2.3</th><th>2.4</th><th>3.1</th><th>3.2</th><th>3.3</th><th>3.4</th><th>3.5</th><th>4.1</th><th>4.2</th><th>5.0</th><th>6.1</th><th>6.2</th><th>6.3</th><th>6.4</th><th>6.5</th><th>7.0</th></tr><tr><td>测试模型</td><td>分值</td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>6.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>6.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>8.0</td><td>5.0</td><td>3.0</td><td>6.0</td><td>6.0</td><td>5.0</td><td>2.0</td><td>4.0</td><td>4.0</td><td>3.0</td><td>60.0</td><td>150.0(100%)</td></tr><tr><td>阿里 千问2-72B</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>5.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>2.0</td><td>3.0</td><td>3.0</td><td>6.0</td><td>5.0</td><td>3.0</td><td>6.0</td><td>6.0</td><td>0.0</td><td>1.0</td><td>1.0</td><td>4.0</td><td>3.0</td><td>50.0</td><td>124.0(82.6%)</td></tr><tr><td>上海人工智能实验室 书生·浦语-文曲星-20B	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>5.0</td><td>3.0</td><td>0.0</td><td>3.0</td><td>7.0</td><td>4.0</td><td>3.0</td><td>3.0</td><td>6.0</td><td>0.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td>46.0</td><td>112.0(74.6%)</td></tr><tr><td>OpenAI GPT-4o	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>6.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>5.0</td><td>5.0</td><td>3.0</td><td>5.0</td><td>2.0</td><td>0.0</td><td>2.0</td><td>0.0</td><td>4.0</td><td>3.0</td><td>50.5</td><td>111.5(74.3%)</td></tr><tr><td>阿里 千问2-57B	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>5.0</td><td>2.0</td><td>0.0</td><td>3.0</td><td>5.0</td><td>2.0</td><td>3.0</td><td>4.0</td><td>6.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>45.5</td><td>99.5(66.3%)</td></tr><tr><td>零一万物 Yi-1.5-34B	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>5.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>4.0</td><td>2.0</td><td>0.0</td><td>0.0</td><td>4.0</td><td>2.0</td><td>3.0</td><td>2.0</td><td>2.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>2.0</td><td>2.0</td><td>50.0</td><td>97.0(64.7%)</td></tr><tr><td>智谱 GLM4-9B	</td><td></td><td>3.0</td><td>3.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>4.0</td><td>2.0</td><td>3.0</td><td>5.0</td><td>6.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>3.0</td><td>41.0</td><td>86.0(57.3%)</td></tr><tr><td>Mistral Mixtral 8x22B</td><td></td><td>0.0</td><td>3.0</td><td>0.0</td><td>1.0</td><td>6.0</td><td>3.0</td><td>0.0</td><td>2.0</td><td>3.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>2.0</td><td>1.0</td><td>3.0</td><td>4.0</td><td>2.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>3.0</td><td>44.5</td><td>77.5(51.7%)</td></tr></table>


## 数学

本次参与测试的模型均为大语言模型，题目的中图片会被丢弃，只有文字题干会输入到模型中（本次测试中，只有数学有2道带图题目）。其中数学的简答题部分不同阅卷老师差距非常大，最大的可达13分，造成这么大的分差的主要原因是由于大模型的回答相对比较凌乱，不一句句核对很容易被公式“欺骗”。阅卷老师会被它们看似合理的回答迷惑，甚至有的题目大模型本来过程已经错误了，但是最后竟然得出了正确的直线方程，导致有的老师会误以为模型正确回答了问题。每一道简答题我们都进行了复核，并根据步骤进行重新给分，最终复核基本都比阅卷老师评分更低。

数学试卷各部分的得分如下所示
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th colspan="6"  style="text-align: center;">数学各题型得分情况</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>模型</td>
      <td>单选择（满分40分）</td>
      <td>多选题（满分18分）</td>
      <td>填空题（满分15分）</td>
      <td>问答题（满分77分）</td>
      <td>总分（满分150）</td>
    </tr>
    <tr>
      <td>上海人工智能实验室 书生·浦语-文曲星-20B</td>
      <td>30</td>
      <td>9</td>
      <td>10</td>
      <td>26</td>
      <td>75</td>
    </tr>
    <tr>
      <td>OpenAI GPT-4o</td>
      <td>35</td>
      <td>6</td>
      <td>10</td>
      <td>22</td>
      <td>73</td>
    </tr>
    <tr>
      <td>阿里 千问2-72B</td>
      <td>30</td>
      <td>12</td>
      <td>10</td>
      <td>18</td>
      <td>70</td>
    </tr>
    <tr>
      <td>阿里千问2 57B</td>
      <td>35</td>
      <td>9</td>
      <td>5</td>
      <td>9</td>
      <td>58</td>
    </tr>
    <tr>
      <td>智谱 GLM4-9B</td>
      <td>30</td>
      <td>7</td>
      <td>0</td>
      <td>12</td>
      <td>49</td>
    </tr>
    <tr>
      <td>零一万物 Yi-1.5-34B</td>
      <td>20</td>
      <td>5</td>
      <td>0</td>
      <td>4</td>
      <td>29</td>
    </tr>
    <tr>
      <td>Mistral Mixtral 8x22B</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>21</td>
    </tr>
  </tbody>
</table>

各个具体的小题得分情况如下所示


<table border="1">
    <tr>
        <th rowspan="2">数学</th>
        <th rowspan="2">题号</th>
<th colspan="8">单选题</th><th colspan="3">多选题</th><th colspan="3">填空题</th><th colspan="5">简答题</th><th rowspan="2">总分</th></tr>
<tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th></tr><tr><td>测试模型</td><td>分值</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td><td>6</td><td>5</td><td>5</td><td>5</td><td>13</td><td>15</td><td>15</td><td>17</td><td>17</td><td>150(100%)</td></tr><tr><td>上海人工智能实验室 书生·浦语-文曲星-20B	</td><td></td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>3</td><td>6</td><td>0</td><td>5</td><td>5</td><td>9</td><td>9</td><td>1</td><td>6</td><td>1</td><td>75(50.0%)</td></tr><tr><td>OpenAI GPT-4o	</td><td></td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>0</td><td>6</td><td>5</td><td>5</td><td>0</td><td>6</td><td>7</td><td>5</td><td>3</td><td>1</td><td>73(48.7%)</td></tr><tr><td>阿里 千问2-72B</td><td></td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>6</td><td>6</td><td>5</td><td>5</td><td>0</td><td>7</td><td>7</td><td>0</td><td>3</td><td>1</td><td>70(46.7%)</td></tr><tr><td>阿里 千问2-57B	</td><td></td><td>5</td><td>5</td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>3</td><td>0</td><td>6</td><td>0</td><td>5</td><td>0</td><td>1</td><td>5</td><td>1</td><td>2</td><td>0</td><td>58(38.7%)</td></tr><tr><td>智谱 GLM4-9B	</td><td></td><td>5</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>3</td><td>4</td><td>0</td><td>0</td><td>0</td><td>1</td><td>7</td><td>2</td><td>1</td><td>1</td><td>49(32.7%)</td></tr><tr><td>零一万物 Yi-1.5-34B	</td><td></td><td>5</td><td>0</td><td>0</td><td>5</td><td>0</td><td>5</td><td>5</td><td>0</td><td>3</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>3</td><td>0</td><td>29(19.3%)</td></tr><tr><td>Mistral Mixtral 8x22B</td><td></td><td>5</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>6</td><td>0</td><td>0</td><td>5</td><td>0</td><td>21(14.0%)</td></tr></table>

## 英语
英语考试中的听力部分（分值30分）不纳入此次评测。

英语试卷各部分的得分如下所示

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th  colspan="7"  style="text-align: center;">英语各题型得分情况</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>模型</td>
      <td>阅读理解（满分37.5分）</td>
      <td>七选五（满分12.5分）</td>
      <td>完型填空（满分15分）</td>
      <td>语法填空（满分15分）</td>
      <td>作文（满分40分）</td>
      <td>总分（满分120）</td>
    </tr>
    <tr>
      <td>OpenAI GPT-4o</td>
      <td>37.5</td>
      <td>10</td>
      <td>14</td>
      <td>15</td>
      <td>35</td>
      <td>111.5</td>
    </tr>
    <tr>
      <td>阿里 千问2-72B</td>
      <td>35</td>
      <td>12.5</td>
      <td>14</td>
      <td>13.5</td>
      <td>34</td>
      <td>109</td>
    </tr>
    <tr>
      <td>上海人工智能实验室 书生·浦语-文曲星-20B</td>
      <td>37.5</td>
      <td>10</td>
      <td>15</td>
      <td>13.5</td>
      <td>32.5</td>
      <td>108.5</td>
    </tr>
    <tr>
      <td>零一万物 Yi-1.5-34B</td>
      <td>35</td>
      <td>10</td>
      <td>11</td>
      <td>13.5</td>
      <td>35</td>
      <td>104.5</td>
    </tr>
    <tr>
      <td>阿里千问2 57B</td>
      <td>35</td>
      <td>10</td>
      <td>9</td>
      <td>15</td>
      <td>27.5</td>
      <td>96.5</td>
    </tr>
    <tr>
      <td>Mistral Mixtral 8x22B</td>
      <td>37.5</td>
      <td>5</td>
      <td>2</td>
      <td>9</td>
      <td>33</td>
      <td>86.5</td>
    </tr>
    <tr>
      <td>智谱 GLM4-9B</td>
      <td>35</td>
      <td>0</td>
      <td>6</td>
      <td>6</td>
      <td>20</td>
      <td>67</td>
    </tr>
  </tbody>
</table>


各个具体的小题得分情况如下所示

<table border="1">
    <tr>
        <th rowspan="2">英语</th>
        <th rowspan="2">题号</th>
<th colspan="4">阅读理解</th><th colspan="1">7选5</th><th colspan="1">完形填空</th><th colspan="1">语法</th><th colspan="1">小作文</th><th colspan="1">大作文</th><th rowspan="2">总分</th></tr>
<tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr><tr><td>测试模型</td><td>分值</td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>12.5</td><td>15.0</td><td>15.0</td><td>15.0</td><td>25.0</td><td>120.0(100%)</td></tr><tr><td>OpenAI GPT-4o	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>10.0</td><td>14.0</td><td>15.0</td><td>12.0</td><td>23.0</td><td>111.5(92.9%)</td></tr><tr><td>阿里 千问2-72B</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>7.5</td><td>12.5</td><td>14.0</td><td>13.5</td><td>13.5</td><td>20.5</td><td>109.0(90.8%)</td></tr><tr><td>上海人工智能实验室 书生·浦语-文曲星-20B	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>10.0</td><td>15.0</td><td>13.5</td><td>12.5</td><td>20.0</td><td>108.5(90.4%)</td></tr><tr><td>零一万物 Yi-1.5-34B	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>7.5</td><td>10.0</td><td>11.0</td><td>13.5</td><td>13.0</td><td>22.0</td><td>104.5(87.1%)</td></tr><tr><td>阿里 千问2-57B	</td><td></td><td>7.5</td><td>10.0</td><td>7.5</td><td>10.0</td><td>10.0</td><td>9.0</td><td>15.0</td><td>12.0</td><td>15.5</td><td>96.5(80.4%)</td></tr><tr><td>Mistral Mixtral 8x22B</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>5.0</td><td>2.0</td><td>9.0</td><td>11.5</td><td>21.5</td><td>86.5(72.1%)</td></tr><tr><td>智谱 GLM4-9B	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>7.5</td><td>0.0</td><td>6.0</td><td>6.0</td><td>5.0</td><td>15.0</td><td>67.0(55.8%)</td></tr></table>

## 老师点评
在改完所有的科目之后，我们也邀请阅卷老师对7个大模型整体的表现进行了点评。

**语文老师点评**：   
大模型进行文言文翻译问题不大，但主观题大部分审题失败，读不懂题，对题目中某些代词的指向不太明确导致答非所问。大模型写作文都不太像高考作文更像问答题，虽然有针对性但缺乏修饰，人类考生都会使用举例论证、引用论证，习惯用名人名言和人物素材，但是大模型写作文时几乎都没用过。写一个暗喻的句子，大模型几乎全军覆没，本体喻体都搞错了，大模型似乎不懂得“暗喻”手法是什么，都写成了普通的“比喻”，也不懂得“本体”是什么。补写句子也不太能写对，看来对于与上下文语意的衔接、中文中的一些语言习惯(补写句子中后文出现了一个新的概念，如“睡眠质量”，那么补写的这个句子中应该要出现这个概念，否则后文突然提起就很突兀，衔接不紧密)，语言中的一些“潜台词”，大模型还不能完全明白。

**数学老师点评**：  
大模型做题总体感觉很机械，大部分通过穷举完成而非推理，例如第一个解答题，大模型都无法做出第二问，只能教条地选择了一个公式，没有基于像考生做题一样来分析，要得出这个结论，需要怎么根据已知去推理。此外，对于几何题，大模型更擅长解析几何题不擅长立体几何题，立体几何回答过程中会出现离谱的推理过程，大模型的公式记忆能力还可以，但是解题过程中无法做到灵活引用，有些题目从最初的解题思路来看是正确的，但是解题过程容易没有逻辑，导致评阅也比较困难。

**英语老师点评**：  
语言上无可挑剔，但是有的模型无法识别题目要求，如七选五识别为单选，四道题识别为五道题。感觉大模型的能力在续写这一题目上体现的最明显，首先是题干要求总字数150，几个大模型识别为每段150个词，总量就超过了300，其次是对原文的理解上有些大模型写出的剧情发展完全悖离出题人的初衷，还有甚者写出了“魔幻现实主义”的剧情，如借钱不收，出租车司机有德国银行内线等极不合理的电影情节。这就是大模型和真实考生的区别，考生普遍是语言能力弱，但是理解能力强，剧情构建基本合理；大模型是语言完美，表达却不符合人之常识和人之常情。
