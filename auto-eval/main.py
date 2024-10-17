print("一定要开代理跑")

import os 
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from Bleu import Bleu
from Distinct import Distinct
from Rouge import Rouge
from Meteor import Meteor
from BertScore import BertScore
import argparse

import argparse
import json
import tabulate
import os
from transformers import AutoTokenizer
import sys
""" json.dumps(): 将 Python 对象编码成 JSON 字符串。 json.dump(): 将 Python 对象编码成 JSON 字符串，并写入到文件中。json.loads(): 将已编码的 JSON 字符串解码为 Python 对象。json.load(): 读取文件中的 JSON 编码的数据，并解码为 Python 对象。
    """
import os
import json
def json_standard(input_object):
    # print(input_object,type(input_object))
    return json.dumps(input_object,ensure_ascii=False,indent=4)
def read_file(file_path:str):
    with open(file_path,"r",encoding="utf-8") as i_f:
        return json.load(i_f)
def write_file(file_path:str,obj,overwrite=False):
    if os.path.exists(file_path)==False or overwrite==True:
        with open(file_path,"w",encoding="utf-8") as o_f:
            json.dump(obj,o_f,ensure_ascii=False)
        print(f"写入{file_path}")
    else:
        print(f"{file_path}文件已经存在")
def write_jsonl_file(file_path:str,obj,overwrite=False):
    if os.path.exists(file_path)==False or overwrite==True:
        with open(file_path, "w", encoding="utf-8") as file:
            for item in obj:
                json.dump(item, file, ensure_ascii=False)  # ensure_ascii=False以支持中文字符
                file.write("\n")  # 写入换行符分隔每个JSON对象
        print(f"写入{file_path}")
    else:
        print(f"{file_path}文件已经存在")
def read_jsonl_file(file_path:str)->list:
    result=[]
    with open(file_path, "r", encoding="utf-8") as file:
        for item in file.readlines():
            item=json.loads(item.strip())  # ensure_ascii=False
            result.append(item)
    return result
def check_file(file_path:str):
    """返回该路径下是否存在文件"""
    is_exist=os.path.exists(file_path)
    if is_exist:
        file_name=file_path.split("/")[-1]
        print(f"{file_name} exist")
    return is_exist



#         "rouge-1": Rouge1,
        # "rouge-2": Rouge2,
        # "rouge-l": RougeL,
        # "bleu": Bleu,
        # "self-bleu": SelfBleu,
        # "meteor": Meteor,
        # "ppl": Perplexit
mistral_tokenizer = AutoTokenizer.from_pretrained("/home/ckqsudo/code2024/0model/Mistral-7B-Instruct-v0.2",padding="longest")
import pandas as pd
print("Keqi") 
print(sys.getrecursionlimit())
sys.setrecursionlimit(8735 * 2080 + 10)

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, help="待评估文件，格式为json[{'ref': str, 'hyps': [str, ..]}, ...]")
arg = parser.parse_args()
file_path=arg.input
class Metrics():
    def __init__(self,metrics=["Bleu","BertScore","Distinct","Meteor","Rouge"]):
        self.metrics=metrics
# logger.info(f"{sys.getrecursionlimit()=}")
    def calc(self,hyps:list,ref:list,metrics=["Bleu","BertScore","Distinct","Meteor","Rouge"],tokenizer=None):
        bleu=Bleu()
        distinct=Distinct()
        bertScore=BertScore()
        meteor=Meteor()
        rouge=Rouge()
        dis_dict=distinct.calc(hyps_sentence_list=hyps,tokenizer=tokenizer)
        data=[]
        print("自我检查完成")
        for idx in range(len(hyps)):
            result=[]
            for m in metrics:
                print(m)
                if m=="Bleu":
                    result.append(     bleu.calc([hyps[idx]],[ref[idx]],[1,2,3,4]))
                elif m=="BertScore":
                    result.append(bertScore.calc([hyps[idx]],[ref[idx]]))
                elif m=="Meteor":
                    result.append(   meteor.calc([hyps[idx]],[ref[idx]]))
                elif m=="Rouge":
                    result.append(    rouge.calc([hyps[idx]],[ref[idx]]))
            explore_dict={}
            print(result[0])
            for item in result:
                for key,value in item.items():
                    if key in explore_dict:
                        raise ValueError()
                    explore_dict[key]=value
            print(explore_dict)
            data.append(explore_dict)
        return dis_dict,data


metrics = Metrics()
input_file_path=arg.input
if input_file_path.endswith(".json"):
    with open(input_file_path, "r") as f:
        inputs = json.load(f)
elif input_file_path.endswith(".jsonl"):
    inputs=read_jsonl_file(input_file_path)
distinct_dict,data = metrics.calc([item['hyps'] for item in  inputs],[item['ref'] for item in  inputs], metrics=["Bleu","BertScore","Distinct","Meteor","Rouge"],tokenizer=mistral_tokenizer)

mean_counter={k: 0 for k in sorted(data[0])}
print(distinct_dict)
mean_counter.update(distinct_dict)
for idx,item in enumerate(data):
    
    for key,value in item.items():
        mean_counter[key]+=value

for key,value in mean_counter.items():
    mean_counter[key]=mean_counter[key]/len(data)

if "/" in file_path:
    file_name=file_path.split("/")[-1]
output_dir="/home/ckqsudo/code2024/Mistral-7b-finetune/metrics/nlg-metrics/keqi_evaluation/keqi_eval_result"

with open(output_dir+"/6_11-"+file_name+"_mean_6_11_.json","w") as f:
    json.dump(mean_counter, f)
with open(output_dir+"/6_11-"+file_name+"data_6_11_.json","w") as f:
    json.dump(data, f)
# 、

