# !pip install bert_score
import os
os.environ['HF_ENDPOINT']='https://hf-mirror.com' 
# 需要在命令行操作才行
from bert_score import score
class BertScore():
    def __init__(self):
        super().__init__()
        self.model =""
        print("初始化~使用自定义bertsore")

    def calc(self, hyps:list, ref:list, *args, **kwargs) :
        # 自动处理中英文 

        P, R, F1 = score(hyps, ref, lang="en", verbose=True)

        return {"BertScore-F1": float(F1.mean()),"BertScore-P": float(P.mean()),"BertScore-Recall": float(R.mean())}