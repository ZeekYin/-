# -完形填空
基于transformers的N选一完形填空
huggingface transformers：https://huggingface.co/transformers/index.html
# 完形填空
### 作者不对任何错误答案等承担任何责任。使用本代码意味着你同意本文件夹下的所有条款。

## 1.安装

#### Mac：

首先请安装python3，之后使用

`pip install transformer`

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

说明环境已经正确被配置。

接下来前往

`/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/transformers/pipelines `

打开`fill_mask.py`

将第95行的

```python
    def postprocess(self, model_outputs, top_k=5, target_ids=None):
```

改为

```python
    def postprocess(self, model_outputs, top_k=30522, target_ids=None):
```



即可。

#### Windows：

除了fill_mask.py的位置不同外与mac相同。



## 2.使用：

按照说明操作即可。
