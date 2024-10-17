import torch
import evaluate

from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
mistral_tokenizer = AutoTokenizer.from_pretrained("/home/ckqsudo/code2024/0model/Mistral-7B-Instruct-v0.2",padding="longest")

class Distinct():
    def __init__(self):
        # 加载Distinct模型
        self.distinct = evaluate.load("lsy641/distinct")
    def calc(self,hyps_sentence_list,tokenizer=None,dataset_sentence_list=None):
        if tokenizer!=None:
            results1 = self.distinct.compute(predictions=hyps_sentence_list, vocab_size=mistral_tokenizer.vocab_size)
            return results1
        elif dataset_sentence_list!=None:
            results2 = self.distinct.compute(predictions=hyps_sentence_list, dataForVocabCal=dataset_sentence_list)
            return results2
        else:
            print("建议提供vocab list \  tokenizer")
            results3 = self.distinct.compute(predictions=hyps_sentence_list)
            return results3
distinct_n=Distinct()
predictions = ["It is a guide to action which ensures that the military always obeys the commands of the party."]

references = ["It is a guide to action that ensures that the military will forever heed Party commands."]

dataset = ["This is my friend jack", "I'm sorry to hear that", "But you know I am the one who always support you", "Welcome to our family","Hi.", "I am sorry to hear that", "I don't know", "Do you know who that person is?"]
print(distinct_n.calc(dataset,tokenizer=mistral_tokenizer))