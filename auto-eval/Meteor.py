import torch
import evaluate
import jieba
from nltk.translate.meteor_score import meteor_score
class Meteor():
    def __init__(self):
        # 加载Distinct模型
        self.model =  evaluate.load('rouge')
    def calc(self,hyps:list,ref:list):
        if len(hyps)>1 or len(ref)>1:
            raise ValueError()
        else:
            reference_tokens = list(jieba.cut(hyps[0]))
            candidate_tokens = list(jieba.cut(ref[0]))

            meteor = meteor_score([reference_tokens], candidate_tokens)
            print(meteor) # 0.7261457550713748
            return {"meteor":meteor}
rouge=Meteor()
predictions = ["It is a guide to action which ensures that the military always obeys the commands of the party."]

references = ["It is a guide to action that ensures that the military will forever heed Party commands."]
print(rouge.calc(predictions,references))