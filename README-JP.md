# Fill in the Blank

huggingface transformersに基づいたもの

huggingface transformers：https://huggingface.co/transformers/index.html



# 注意

### 本コードを使用した際に発生したいかなる問題について一切の責任を負わない。下記の規約を了承し同意することができない場合は使用できません。
#### 1.私は、このコードの使用から生じるすべての結果を負担することを約束します。
#### 2.私は、このrepositoryを、違法な目的、または所属する組織（会社、学校など）の規則に反する目的で使用しないことを約束します。
#### 3.私は、このrepositoryを学業不正の行為のために使用しないことを約束します。
#### 4.私は、このプログラムが英語学習のために作られたものであることを理解し、このツールを適切に使用することを約束します。
#### 5.私は、その他、Licenceに記載されている全ての条件に同意します。

### Update
#### v1.2

##### new feature:
multi-question to multi-option式のクイズをサポートした。問題数を入力してサイトからコピーすれば結果が得られる。
トラブル回避のため、ここも説明をしない。“running mode”の表示があったときに2を入力すれば使用できる。
##### bug fix: 
例外処理を加えた。これで正しくない入力があっても終了しないので、再起動の時間を節約できた。

#### v1.1 

n to 1式のクイズをサポートした。選択肢の数を入力してサイトからコピーすれば結果が得られる。
トラブル回避のため、ここは説明をしない。“running mode”の表示があったときに1を入力すれば使用できる。

## 1.インストール

#### Mac：

python3をインストールし、

`pip install transformers`

でhuggingfaceのtransformersパッケージをインストールする。

そして

`python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"`

でインストールできたかどうかが確認できる。

`[{'label': 'POSITIVE', 'score': 0.9998704791069031}]`

の表示があれば正しくインストールしたことがわかる。



続いて

``````python
from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')
unmasker("Hello I'm a [MASK] model.")
``````

を入力する。

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

が表示されれば環境の構築は正しく終わった。



`/pythonのインストールファイル/site-packages/transformers/pipelines `

に進み、`fill_mask.py`

の95行目の

```python
    def postprocess(self, model_outputs, top_k=5, target_ids=None):
```

を

```python
    def postprocess(self, model_outputs, top_k=30522, target_ids=None):
```

に変更する。

使用が終わったらtop_kの値を5に戻してください。

#### Windows：

大体同じ手順で進んでください。



## 2.使用：

１まずは空欄を[MASK]に置き換えて入力する。
２選択肢の数を入力。
３選択肢を入力。

選択肢がvocabularyにないときは、可能性の高い順で10個の単語が出力される。

結果が出たらYを押すと続いて使える。Nを押すと終了できる。



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

Offline Mode

https://huggingface.co/transformers/installation.htmlを参考してください。
