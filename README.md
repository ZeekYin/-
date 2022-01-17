# 完形填空

基于huggingface transformers的N选一完形填空

huggingface transformers：https://huggingface.co/transformers/index.html

If you need Japanese translation，please contact me

# 完形填空

### 作者不对任何错误答案等承担任何责任。使用本代码意味着你同意以下所有条款。

#### 1.我承诺自行承担使用此代码所带来的一切后果。

#### 2.我承诺不将此repository下所有内容作非法亦或是违反所属单位（公司，学校等）的规程之用途。

#### 3.我承诺不使用本repository来进行作弊等学术不端的行为。

#### 4.我理解本程序旨在帮助学习英语，我将用适当的方法使用此工具。

#### 5.我同意所有其他记载于Licence中的条款。

### 更新内容

#### v1.2

1.添加了针对某校的多问多选项quiz的支持。具体为可以在输入选项数目后直接从Safari浏览器中复制，粘贴后直接得到结果
使用时请在提示“running mode”时输入2，详细使用方法请参考使用说明

2.增加了异常处理，输入的内容有问题时程序不会直接退出，借此减少了重新启动时调用模型的时间

#### v1.1 

添加了针对某校的4选1quiz的支持。具体为可以在输入选项数目后直接从Safari浏览器中复制，粘贴后直接得到结果
使用时请在提示“running mode”时输入1，详细使用方法请参考使用说明

## 1.安装

#### Mac：

首先请安装python3，之后使用

`pip install transformers`

安装huggingface的transformers包

之后输入

`python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"`

来查看是否成功安装

如果结果中包含

`[{'label': 'POSITIVE', 'score': 0.9998704791069031}]`

说明已经正确安装了。

接下来输入这三行

``````python
from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')
unmasker("Hello I'm a [MASK] model.")
``````

如果显示

```python
[{'sequence': "[CLS] hello i'm a fashion model. [SEP]",
  'score': 0.1073106899857521,
  'token': 4827,
  'token_str': 'fashion'},
 {'sequence': "[CLS] hello i'm a role model. [SEP]",
  'score': 0.08774490654468536,
  'token': 2535,
  'token_str': 'role'},
 {'sequence': "[CLS] hello i'm a new model. [SEP]",
  'score': 0.05338378623127937,
  'token': 2047,
  'token_str': 'new'},
 {'sequence': "[CLS] hello i'm a super model. [SEP]",
  'score': 0.04667217284440994,
  'token': 3565,
  'token_str': 'super'},
 {'sequence': "[CLS] hello i'm a fine model. [SEP]",
  'score': 0.027095865458250046,
  'token': 2986,
  'token_str': 'fine'}]
```

说明环境已经被正确配置。

接下来前往

`/python的运行目录/site-packages/transformers/pipelines `

打开`fill_mask.py`

将第95行的

```python
    def postprocess(self, model_outputs, top_k=5, target_ids=None):
```

改为

```python
    def postprocess(self, model_outputs, top_k=30522, target_ids=None):
```



即可。使用完成后请将top_k的值修改回5。

#### Windows：

除了fill_mask.py的位置不同外与mac相同。



## 2.使用：

### 0.一般模式

首先将填空的位置替换为[MASK], 按照提示输入。
之后输入选项数量，只能输入整数，否则会报错。
之后输入对应的选项。

由于词表大小限制，选项的单词可能不在词表里。此时会给出10个较为可能的候选词。

得到结果后，如果需要继续，请按Y，否则程序将结束。


使用例：

```
type your question, replace _blanc_ to [MASK]
>>>Hello I'm a [MASK] model.
number of candidates
>>>4
input candidate
>>>fashion
input candidate
>>>role
input candidate
>>>new
input candidate
>>>fine
fashion 0.10731068253517151

role 0.0877448171377182

new 0.05338383466005325

fine 0.027095889672636986

contunue? Y/N
N
```

### 1.n选1quiz模式

如果你的quiz粘贴到记事本后是以下格式

```
[CONTEXT] ________ [CONTEXT].
请选择一项:

a.
[OPTION1]

b.
[OPTION2]

c.
[OPTION3]

d.
[OPTION4]
```

则可以直接按回车键得到结果。否则请先修改为上述格式。结果会按降序给出所有选项以及对应的分数



使用例：

```
number of candidates
>>>4
type your question
>>>Hello I'm a ______ model.
>>>请选择一项:
>>>
>>>a.
>>>fashion
>>>
>>>b.
>>>role
>>>
>>>c.
>>>new
>>>
>>>d.
>>>fine
fashion 0.10731068253517151

role 0.0877448171377182

new 0.05338383466005325

fine 0.027095889672636986

contunue? Y/N
N
```

### 2. 选词填空（每个选项只能用一次）模式

如果你的quiz粘贴到记事本后是以下格式

```
Complete the sentences by using the correct words from the list.
1. [CONTEXT] 空白 [CONTEXT]

2. [CONTEXT]  空白 [CONTEXT]

3. [CONTEXT]  空白 [CONTEXT]
[OPTION1] [OPTION2] [OPTION3] [OPTION4]
```

则可以直接按回车键得到结果。否则请先修改为上述格式。结果会按题号给出填入单词的顺序以及整体分数。

**离线使用**

参考https://huggingface.co/transformers/installation.html
