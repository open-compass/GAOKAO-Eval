# 新课标I卷摘要
新课标I卷覆盖的省份主要包括广东、福建、湖北、湖南、江苏、河北、山东、浙江、江西、安徽、河南，本次测试使用新课标I卷的语数外三门考卷。具体题目可以在 [高考直通车](https://easylearn.baidu.com/gaokao/content/list?tabKey=question) 查看。

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

根据当前测评的三门考卷的汇总分数看，斩获前三名的模型分别是：阿里巴巴 千问2-72B、OpenAI GPT-4o和上海人工智能实验室书生·浦语-文曲星-20B，它们的总分是303、296、295.5，对应得分率分别是72.1%、70.5%和70.4%。
分学科而言，
- 英语最简单，参加考试的大模型平均可以获得97分（满分120分），GPT-4o甚至获得了111.5的高分；
- 数学是“噩梦”，尽管有的大模型可以在8个单选题中做对7个，但如果评测考虑简答题，没有任何一个大模型能够及格。数学考得最好的模型来自于上海人工智能实验室，其高考数学分数为75分（满分150），也只能获得50%的高考数学分数

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

值得欣慰的是，国内模型在语文上相较于GPT-4o存在优势。从各类题目来看，模型在现代文阅读、古诗文阅读、名句默写和作文上有着高于70%的平均得分率；而在古诗文阅读和语言文字运用上却分别仅有不足50%和30%的得分率。特别是在语言文字运用中，许多大模型不能很好理解并遵循题目的要求，其中所有模型都不理解“借喻”手法，以及不能满足15个字的字数要求。在作文写作中，大模型的作文都有着较为明显的文字特征，例如比较喜欢使用“首先”、“其次”、“然后”这些词语作为段落的开始。

语文试卷中每个小题得分情况如下所示

<table border="1">
    <tr>
        <th rowspan="2">语文</th>
        <th rowspan="2">题号</th>
<th colspan="5">现代文阅读Ⅰ</th><th colspan="4">现代文阅读ⅠⅠ</th><th colspan="5">文言文阅读</th><th colspan="2">古诗文阅读</th><th colspan="1">名篇名句默写</th><th colspan="5">语言文字运用</th><th colspan="1">作文</th><th rowspan="2">总分</th></tr>
<tr><th>1.1</th><th>1.2</th><th>1.3</th><th>1.4</th><th>1.5</th><th>2.1</th><th>2.2</th><th>2.3</th><th>2.4</th><th>3.1</th><th>3.2</th><th>3.3</th><th>3.4</th><th>3.5</th><th>4.1</th><th>4.2</th><th>5.0</th><th>6.1</th><th>6.2</th><th>6.3</th><th>6.4</th><th>6.5</th><th>7.0</th></tr><tr><td>测试模型</td><td>分值</td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>6.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>6.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>8.0</td><td>5.0</td><td>3.0</td><td>6.0</td><td>6.0</td><td>5.0</td><td>2.0</td><td>4.0</td><td>4.0</td><td>3.0</td><td>60.0</td><td>150.0(100%)</td></tr><tr><td>阿里 千问2-72B</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>5.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>2.0</td><td>3.0</td><td>3.0</td><td>6.0</td><td>5.0</td><td>3.0</td><td>6.0</td><td>6.0</td><td>0.0</td><td>1.0</td><td>1.0</td><td>4.0</td><td>3.0</td><td>50.0</td><td>124.0(82.6%)</td></tr><tr><td>上海人工智能实验室 书生·浦语-文曲星-20B	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>5.0</td><td>3.0</td><td>0.0</td><td>3.0</td><td>7.0</td><td>4.0</td><td>3.0</td><td>3.0</td><td>6.0</td><td>0.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td>46.0</td><td>112.0(74.6%)</td></tr><tr><td>OpenAI GPT-4o	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>6.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>5.0</td><td>5.0</td><td>3.0</td><td>5.0</td><td>2.0</td><td>0.0</td><td>2.0</td><td>0.0</td><td>4.0</td><td>3.0</td><td>50.5</td><td>111.5(74.3%)</td></tr><tr><td>阿里 千问2-57B	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>3.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>5.0</td><td>2.0</td><td>0.0</td><td>3.0</td><td>5.0</td><td>2.0</td><td>3.0</td><td>4.0</td><td>6.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>45.5</td><td>99.5(66.3%)</td></tr><tr><td>零一万物 Yi-1.5-34B	</td><td></td><td>3.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>5.0</td><td>3.0</td><td>3.0</td><td>2.0</td><td>4.0</td><td>2.0</td><td>0.0</td><td>0.0</td><td>4.0</td><td>2.0</td><td>3.0</td><td>2.0</td><td>2.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>2.0</td><td>2.0</td><td>50.0</td><td>97.0(64.7%)</td></tr><tr><td>智谱 GLM4-9B	</td><td></td><td>3.0</td><td>3.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>4.0</td><td>2.0</td><td>3.0</td><td>5.0</td><td>6.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>3.0</td><td>41.0</td><td>86.0(57.3%)</td></tr><tr><td>Mistral Mixtral 8x22B</td><td></td><td>0.0</td><td>3.0</td><td>0.0</td><td>1.0</td><td>6.0</td><td>3.0</td><td>0.0</td><td>2.0</td><td>3.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>2.0</td><td>1.0</td><td>3.0</td><td>4.0</td><td>2.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>3.0</td><td>44.5</td><td>77.5(51.7%)</td></tr></table>


## 数学

本次参与测试的模型均为大语言模型，题目的中图片会被丢弃，只有文字题干会输入到模型中（本次测试中，只有数学有2道带图题目）。其中数学的简答题部分不同阅卷老师差距非常大，最大的可达13分，造成这么大的分差的主要原因是由于大模型的回答相对比较凌乱，不一句句核对很容易被公式“欺骗”。阅卷老师会被看似合理的回答迷惑，甚至有的题目大模型解答过程错了，但是最后竟然得出了正确的直线方程，导致有的老师会误以为模型正确回答了问题。因此，对于所有的简答题，我们都进行了逐一复核，并根据步骤进行分数校准，最终复核后每道简答题比阅卷平均分低了4～5分。

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

数学是所有大模型得分率最低的学科。尤其值得注意的是，数学问答题对所有大模型都是巨大的挑战，五道问答题平均得分率仅为18.9%，根据本次测评得分，上海人工智能实验室书生·浦语-文曲星-20B模型获得了该项最具挑战的题型的最高得分率——33.8%。目前评测的所有模型中，没有任何一个模型对任何一道大题被完整地做对完全做对，较好的大模型可以答对第一问以及后面问题的小部分。


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

GPT-4o摘得了英语科目的第一名，并且有阅卷老师高度赞赏GPT-4o的英文作文，仅因为字数原因酌情扣掉1分。从整体分数上来看，阅读理解无疑是所有大模型的拿手好戏，所有大模型平均得分率达到了96.2%，而得分率65.7%让七选五成为了最难得分的部分。完型填空和七选五两种题型的得分率均不足70%，其中一个重要原因是有的大模型不适应题型，会导致输出答案错位导致扣分。作文部分，大部分大模型都因为超出字数限制导致扣分，而人类考生因为字数扣分多是由于字数不够，并且大模型普遍存在单段落过长的问题。

各个具体的小题得分情况如下所示

<table border="1">
    <tr>
        <th rowspan="2">英语</th>
        <th rowspan="2">题号</th>
<th colspan="4">阅读理解</th><th colspan="1">7选5</th><th colspan="1">完形填空</th><th colspan="1">语法</th><th colspan="1">小作文</th><th colspan="1">大作文</th><th rowspan="2">总分</th></tr>
<tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr><tr><td>测试模型</td><td>分值</td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>12.5</td><td>15.0</td><td>15.0</td><td>15.0</td><td>25.0</td><td>120.0(100%)</td></tr><tr><td>OpenAI GPT-4o	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>10.0</td><td>14.0</td><td>15.0</td><td>12.0</td><td>23.0</td><td>111.5(92.9%)</td></tr><tr><td>阿里 千问2-72B</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>7.5</td><td>12.5</td><td>14.0</td><td>13.5</td><td>13.5</td><td>20.5</td><td>109.0(90.8%)</td></tr><tr><td>上海人工智能实验室 书生·浦语-文曲星-20B	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>10.0</td><td>15.0</td><td>13.5</td><td>12.5</td><td>20.0</td><td>108.5(90.4%)</td></tr><tr><td>零一万物 Yi-1.5-34B	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>7.5</td><td>10.0</td><td>11.0</td><td>13.5</td><td>13.0</td><td>22.0</td><td>104.5(87.1%)</td></tr><tr><td>阿里 千问2-57B	</td><td></td><td>7.5</td><td>10.0</td><td>7.5</td><td>10.0</td><td>10.0</td><td>9.0</td><td>15.0</td><td>12.0</td><td>15.5</td><td>96.5(80.4%)</td></tr><tr><td>Mistral Mixtral 8x22B</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>10.0</td><td>5.0</td><td>2.0</td><td>9.0</td><td>11.5</td><td>21.5</td><td>86.5(72.1%)</td></tr><tr><td>智谱 GLM4-9B	</td><td></td><td>7.5</td><td>10.0</td><td>10.0</td><td>7.5</td><td>0.0</td><td>6.0</td><td>6.0</td><td>5.0</td><td>15.0</td><td>67.0(55.8%)</td></tr></table>

## 老师整体点评
在改完所有的科目之后，我们告知了以上试卷的回答由大模型生成，然后我们邀请阅卷老师对7个大模型整体的表现进行了点评。

**语文老师点评**：   
大模型进行文言文翻译问题不大，但主观题大部分审题失败，读不懂题，对题目中某些代词的指向不太明确导致答非所问。大模型写作文都不太像高考作文更像问答题，虽然有针对性但缺乏修饰，人类考生都会使用举例论证、引用论证，习惯用名人名言和人物素材，但是大模型写作文时几乎都没用过。写一个暗喻的句子，大模型几乎全军覆没，本体喻体都搞错了，大模型似乎不懂得“暗喻”手法是什么，都写成了普通的“比喻”，也不懂得“本体”是什么。补写句子也不太能写对，看来对于与上下文语意的衔接、中文中的一些语言习惯(补写句子中后文出现了一个新的概念，如“睡眠质量”，那么补写的这个句子中应该要出现这个概念，否则后文突然提起就很突兀，衔接不紧密)，语言中的一些“潜台词”，大模型还不能完全明白。

**数学老师点评**：  
大模型做题总体感觉很机械，大部分通过穷举完成而非推理，例如第一个解答题，大模型都无法做出第二问，只能教条地选择了一个公式，没有基于像考生做题一样来分析，要得出这个结论，需要怎么根据已知去推理。此外，对于几何题，大模型更擅长解析几何题不擅长立体几何题，立体几何回答过程中会出现离谱的推理过程。大模型的公式记忆能力还可以，但是解题过程中无法做到灵活引用，有些题目从最初的解题思路来看是正确的，但是解题过程容易没有逻辑，导致评阅也比较困难。

**英语老师点评**：  
语言上无可挑剔，但是有的模型无法识别题目要求，如七选五识别为单选，四道题识别为五道题。感觉大模型的能力在续写这一题目上体现的最明显，首先是题干要求总字数150，几个大模型识别为每段150个词，总量就超过了300。其次是对作文题目的理解上有些大模型写出的剧情发展完全悖离出题人的初衷，还有甚者写出了“魔幻现实主义”的剧情，如借钱不收，出租车司机有德国银行内线等极不合理的电影情节。这就是大模型和真实考生的区别，考生普遍是语言能力弱，但是理解能力强，剧情构建基本合理；大模型是语言完美，表达却不符合人之常识和人之常情。


## 回答示例

- 语文  

题目:
```
宿千岁庵听泉  
刘克庄  
因爱庵前一脉泉,襆衾来此借房眠。  
骤闻将谓溪当户,久听翻疑屋是船。  
变作怒声犹壮伟,滴成细点更清圆。  
君看昔日兰亭帖,亦把湍流替管弦。  
 
诗中以对比的方式,对泉声进行了生动的描写,请结合相关内容简要赏析。(6分)
```
模型输出（模型：阿里巴巴 千问2-70B）：
```
【小题1】选项D的解读有误。诗人提到“君看昔日兰亭帖,亦把湍流替管弦”，并非意味着他和兰亭诸贤一样摒弃了乐器，而是用典故表达了对自然之音的欣赏，认为自然界的流水声可以替代乐器发出的音乐，达到同样的审美效果。因此，选项D的表述“都把对音乐之美的追求寄托于山水而摒弃了乐器”并不准确。
【小题2】诗中通过对比的方式，对泉声进行了生动的描绘，具体体现在以下几个方面：
 1. 骤闻与久听的对比：“骤闻将谓溪当户,久听翻疑屋是船。”这句诗通过“骤闻”与“久听”的对比，展现了泉声给人带来的不同感受。初听时，诗人以为是溪水就在门口流淌，声音宏大；而长时间倾听后，却产生了错觉，仿佛自己所处的屋子就像是一艘船，在水上漂浮。这种对比不仅表现了泉声的多变性，也体现了诗人对泉声由外在感知转向内在体验的过程。
 2. 怒声与细点的对比：“变作怒声犹壮伟,滴成细点更清圆。”这里通过“怒声”与“细点”的对比，展现了泉声从强烈到细腻的变化。起初，泉声如怒涛般壮阔，给人以震撼；随后，细小的水滴落下，声音变得清脆圆润，如同珍珠落盘，给人以宁静之美。这种对比手法，使读者能够更加直观地感受到泉声的丰富层次和变化。
 3. 自然与艺术的对比：“君看昔日兰亭帖,亦把湍流替管弦。”诗人引用兰亭雅集的典故，将自然界的湍流声与古代文人雅士聚会时的管弦乐声进行对比，暗示自然之声同样具有艺术美感，甚至可以超越人为的音乐。这种对比不仅提升了泉声的艺术价值，也反映了诗人崇尚自然、追求心灵与自然和谐共融的生活态度。
 综上所述，诗中通过对比的手法，不仅生动地描绘了泉声的多样性和美感，还表达了诗人对自然之美的深刻感悟和对艺术境界的追求。
```
老师点评： 
> 该回答条理清晰地从不同角度剖析了诗中对比手法的运用，包括“骤闻”与“久听”、“怒声”与“细点”等的对比，对诗歌有着较好的理解与分析能力。

_____
- 数学

题目：
```latex
15. 记  $\triangle A B C$ 的内角 $A, B, C$ 的对边分别为 $a, b, c$, 已知 $\sin C=\sqrt{2} \cos B, a^2+b^2-c^2=\sqrt{2} a b$
(1) 求 $B$;
(2) 若  $\triangle A B C$  的面积 $3+\sqrt{3}
$, 求 $c$。
```
模型输出（模型：上海人工智能实验室 书生·浦语-文曲星-20B）：
```latex
首先，我们有两个关于三角形$ABC$的条件：

1. $\sin C = \sqrt{2} \cos B$
2. $a^2 + b^2 - c^2 = \sqrt{2} ab$

从第二个条件出发，我们可以使用余弦定理，它表述为 $c^2 = a^2 + b^2 - 2ab\cos C$。将给定的等式与余弦定理比较，我们得到：

$\cos C = \frac{\sqrt{2} ab}{2ab} = \frac{\sqrt{2}}{2}$

由于$C$是三角形的内角，其范围是$(0, \pi)$，所以$C$的值是：

$C = \frac{\pi}{4}$

接下来，我们使用第一个条件和三角恒等式来找到$B$的值。由于$\sin C = \sin(\frac{\pi}{4}) = \frac{\sqrt{2}}{2}$，我们有：

$\sin(\frac{\pi}{4}) = \sqrt{2} \cos B$

这可以简化为：

$\cos B = \frac{\sin(\frac{\pi}{4})}{\sqrt{2}} = \frac{1}{2}$

由于$B$也是三角形的内角，其范围是$(0, \pi)$，所以$B$的值是：

$B = \frac{\pi}{3}$

现在，我们已知$B = \frac{\pi}{3}$，$C = \frac{\pi}{4}$，我们可以找到$A$的值，因为三角形内角和为$\pi$：

$A = \pi - B - C = \pi - \frac{\pi}{3} - \frac{\pi}{4} = \frac{5\pi}{12}$

接下来，我们使用正弦定理来找到边$c$的长度。正弦定理表述为：

$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$

我们已知三角形的面积$S$为$3 + \sqrt{3}$，面积公式为：

$S = \frac{1}{2} ab\sin C$

代入已知的$\sin C$和面积，我们得到：

$3 + \sqrt{3} = \frac{1}{2} ab \cdot \frac{\sqrt{2}}{2}$

解这个方程得到$ab$的值：

$ab = 2\sqrt{2}(3 + \sqrt{3})$

现在，我们使用正弦定理来找到$c$：

$c = \frac{a\sin C}{\sin A}$

由于$\sin A = \sin(\frac{5\pi}{12})$，我们可以使用和角公式来找到$\sin A$：

$\sin A = \sin(\frac{\pi}{4} + \frac{\pi}{6}) = \sin\frac{\pi}{4}\cos\frac{\pi}{6} + \cos\frac{\pi}{4}\sin\frac{\pi}{6} = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6} + \sqrt{2}}{4}$

现在我们可以计算$c$：

$c = \frac{a\sin C}{\sin A} = \frac{a \cdot \frac{\sqrt{2}}{2}}{\frac{\sqrt{6} + \sqrt{2}}{4}} = \frac{2a}{\sqrt{6} + \sqrt{2}}$

由于$ab = 2\sqrt{2}(3 + \sqrt{3})$，我们可以表示$a$为$b$的函数：

$a = \frac{2\sqrt{2}(3 + \sqrt{3})}{b}$

将$a$代入$c$的表达式中，我们得到：

$c = \frac{2 \cdot \frac{2\sqrt{2}(3 + \sqrt{3})}{b} \cdot \frac{\sqrt{2}}{2}}{\sqrt{6} + \sqrt{2}} = \frac{2(3 + \sqrt{3})}{\sqrt{6} + \sqrt{2}}$

为了简化$c$，我们可以乘以共轭分母：

$c = \frac{2(3 + \sqrt{3})(\sqrt{6} - \sqrt{2})}{(\sqrt{6} + \sqrt{2})(\sqrt{6} - \sqrt{2})} = \frac{2(3\sqrt{6} - 3\sqrt{2} + 3\sqrt{2} - 2\sqrt{3})}{6 - 2}$

$c = \frac{2(3\sqrt{6} - 2\sqrt{3})}{4} = \frac{3\sqrt{6} - 2\sqrt{3}}{2}$

所以，$B = \frac{\pi}{3}$，$c = \frac{3\sqrt{6} - 2\sqrt{3}}{2}$。
```
老师点评：
> 本题考查余弦定理与正弦定理，模型正确地利用余弦定理做出了第一问，且在做第二问时巧妙地使用两角和的正弦公式进行化简，是所有模型中唯一一个正确求出$\sin A$的模型

_____

- 英语  

题目
```
五、书信写作
66．假定你是李华，上周五你们班在公园上了一堂美术课。请你给英国朋友Chris写一封邮件分享这次经历，内容包括：
（1）你完成的作品；
（2）你的感想。
注意：
（1）写作词数应为80个左右；
（2）请按如下格式在答题纸的相应位置作答。
Dear Chris,
I’m writing to share with you an art class I had in a park last Friday. 
_____________________________________                          _____________________________________  

Yours,
Li Hua
````
模型回答（GPT-4o）
```
I'm writing to share with you an art class I had in a park last Friday. We spent the day painting landscapes, and I completed a piece featuring a serene lake surrounded by trees and flowers. The experience was incredibly refreshing and inspiring. It felt wonderful to be outdoors, capturing the beauty of nature on canvas. I realized how much I enjoy painting and how it helps me relax and express my creativity. I hope we can have a similar experience together someday.
```
老师点评：
> 句型丰富，语言无瑕疵，内容完成了表达的任务，字数稍少，酌情扣1分。

