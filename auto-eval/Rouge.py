import torch
import evaluate

class Rouge():
    def __init__(self):
        # 加载Distinct模型
        self.model =  evaluate.load('rouge')
    def calc(self,hyps:list,ref:list):
        results = self.model.compute(predictions=hyps, references=ref)
        return results
rouge=Rouge()
predictions = ["It is a guide to action which ensures that the military always obeys the commands of the party."]

references = ["It is a guide to action that ensures that the military will forever heed Party commands."]
print(rouge.calc(predictions,references))