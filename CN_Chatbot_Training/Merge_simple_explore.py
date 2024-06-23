# %%
""" json.dumps(): 将 Python 对象编码成 JSON 字符串。 json.dump(): 将 Python 对象编码成 JSON 字符串，并写入到文件中。json.loads(): 将已编码的 JSON 字符串解码为 Python 对象。json.load(): 读取文件中的 JSON 编码的数据，并解码为 Python 对象。
"""
import os
import json
import torch
torch.cuda.is_available()
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
def check_file(file_path:str):
    """返回该路径下是否存在文件"""
    is_exist=os.path.exists(file_path)
    if is_exist:
        file_name=file_path.split("/")[-1]
        print(f"{file_name} exist")
    return is_exist

# %%
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
model_path="/home/ckqsudo/code2024/0model/Mistral-7B-Instruct-v0.2"
# BitsAndBytesConfig int-4 config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16
)


# %%
eval_arg="mix"
version="4"
print(version,"版本","注意查看所有的路径是否正确")

# %%
from peft import LoraConfig, PeftModel

# 这里注意，from_pretrained 接收两个值作为参数，第一个为基础模型，第二个为lora/
# 
# 
#  所在的path
eval_list=["o_r_d","r_d","d","base","mix"]


lora_path=None
baseline_lora_path=""
dialog_lora_path="/home/ckqsudo/code2024/Mistral-7b-finetune/trl_standard_output/fuck8_6_8_unpacking__pure_dialog/checkpoint-300"
reasoning_lora_path="/home/ckqsudo/code2024/Mistral-7b-finetune/fuck7_6_5_unpacking__reasoning_3/checkpoint-228"
reasoning_observation_lora_path="/home/ckqsudo/code2024/Mistral-7b-finetune/trl_standard_output/fuck8_6_8_unpacking__observation_reasoning/checkpoint-240"
mix_lora_path="/home/ckqsudo/code2024/Mistral-7b-finetune/trl_standard_output/fuck8_6_11_unpacking__continue_training/checkpoint-240"



d_test="/home/ckqsudo/code2024/Mistral-7b-finetune/train_and_test_data/test_dataset_pure_dialog.jsonl"
r_d_test="/home/ckqsudo/code2024/Mistral-7b-finetune/train_and_test_data/test_dataset_reasoning.jsonl"
o_r_d_test="/home/ckqsudo/code2024/Mistral-7b-finetune/train_and_test_data/test_dataset_observation_reasoning.jsonl"
base_test=d_test
mix_test=d_test

lora_path_list=[reasoning_observation_lora_path,reasoning_lora_path,dialog_lora_path,baseline_lora_path,mix_lora_path]
test_path_list=[o_r_d_test,r_d_test,d_test,base_test,mix_test]

lora_dict=dict(zip(eval_list,lora_path_list))
test_dataset_dict=dict(zip(eval_list,test_path_list))
# base_model = AutoModelForCausalLM.from_pretrained(
#     model_path,
#     device_map="auto",
#     attn_implementation="flash_attention_2",
#     torch_dtype=torch.bfloat16,
#     quantization_config=bnb_config
# )
print("注意 merge的时候不需要4bit 量化")
base_model = AutoModelForCausalLM.from_pretrained(
    model_path,
    low_cpu_mem_usage=True,
    return_dict=True,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
# 
if eval_arg in eval_list:
    print(eval_arg,eval_list)
    lora_path=lora_dict[eval_arg]
    test_dataset_path=test_dataset_dict[eval_arg]
else:
    raise ValueError()

if eval_arg=="base":
    merged_model=base_model
    tokenizer=AutoTokenizer.from_pretrained(model_path)
    tokenizer.pad_token=tokenizer.unk_token
    print("原始模型")
else:
    merged_model= PeftModel.from_pretrained(base_model,model_id=lora_path)
    tokenizer=AutoTokenizer.from_pretrained(lora_path)
    tokenizer.pad_token=tokenizer.unk_token

print([eval_arg]*10)

# %%
from datasets import load_dataset
test_dataset= load_dataset("json",data_files=test_dataset_path)

# %%
test_dataset["train"]

# %%
item=test_dataset["train"]

# %%
test_dataset["train"][6]["messages"][3:9]

# %%
# 如果生成的结果是100% 一样，那大概率就是训练集被测试集污染了！！！

# %%
# str_="NST]Therapist: So, what is your goal in coming here?</s>"

# beg_idx=str_.find("Therapist: ")
# end_idx=str_.find("</s>")
# str_[beg_idx:end_idx]
# l=[{"a":1},{"a":2}]


# %%


# %%
import copy
def generate_test_format_data(cur_dataset):
    """Explore_data 将 cur_dataset 炸裂开"""
    explore_test_dataset=[]
    
    for idx,msg_item in enumerate(test_dataset['train']):
        msg_list=copy.deepcopy(msg_item['messages'])
        while True:
            while len(msg_list)!=0 and 'user' in msg_list[-1]['role']:
                msg_list=msg_list[:-1]
            while len(msg_item)!=0 and 'assistant' in msg_list[-1]['role']:
                raw_ground_truth=msg_list[-1]['content']
                ground_truth=raw_ground_truth[raw_ground_truth.find('Therapist:'):]
                dialog_history=msg_list[:-1]
                template={"history":dialog_history,"ground_truth":ground_truth}
                explore_test_dataset.append(template)
                msg_list=msg_list[:-1]
                # print(ground_truth)
        # 如
            if len(set([item['role'] for item in msg_list]))<2:
                break
    return explore_test_dataset
format_datset=generate_test_format_data(test_dataset)
len(format_datset)

# %%
tokenizer.pad_token,tokenizer.pad_token_id

# %%
tokenizer.name_or_path

# %%
result=[]
for idx,msg_item in enumerate(format_datset):
    print_prompt=tokenizer.apply_chat_template(msg_item['history'], tokenize=False)# 用于估计编码长度
    input_ids=tokenizer.apply_chat_template(msg_item['history'], tokenize=True,return_tensors="pt", truncation=False)
    input_ids = input_ids.to('cuda') 
    print(input_ids.shape,len(print_prompt))
    with torch.inference_mode():
        with torch.no_grad():
            beg_idx,end_idx=0,0
            top_p_value=0.5
            Counter=3
            outputs = merged_model.generate(input_ids=input_ids, max_new_tokens=512, do_sample=True, top_p=top_p_value,temperature=0.7)
            str_output=tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=False)[0][len(print_prompt)-3:]
            # 
            beg_idx=str_output.rfind("Therapist:")
            if beg_idx==-1:
                beg_idx=str_output.rfind("Therapist")
                if beg_idx==-1:
                    beg_idx=str_output.rfind("Therapapist:")
                    # Therapapist:
                    # raise ValueError()
                    continue
            end_idx=str_output.find("</s>")
            if end_idx==-1:
                end_idx=len(str_output)
            
            top_p_value+=0.1
            str_response=str_output[beg_idx:end_idx]
            if beg_idx==-1 or end_idx==-1:
                print(str_output)
                print("跳过")
                continue
            print("generate:  ",str_response)
            print("ground_truth:  ",msg_item['ground_truth'])
            if eval_arg=="r_d":
                annotation_str=str_output[str_output.find("Reasoning:"):str_output.find("Therapist:")]
            elif eval_arg=="o_r_d":
                annotation_beg_idx=str_output.find("Observation:")
                if annotation_beg_idx==-1:
                    annotation_beg_idx=str_output.find("Reasoning:")
                annotation_str=str_output[annotation_beg_idx:str_output.find("Therapist:")]
                # 
            elif eval_arg in ["d","base","mix"]:
                annotation_str=""
                print(eval_arg)
            else:
                raise ValueError()
            result.append({'hyps':str_response,
                        'ref':msg_item['ground_truth'],'annotation':annotation_str,
                        "history":msg_item,})
            print('annotation',result[-1]['annotation'])
format_result=[]
for item in result:
    format_result.append({'hyps':item['hyps'],'ref':item['ref'],"history":item['history']['history']})

write_file(f"/home/ckqsudo/code2024/Mistral-7b-finetune/metrics/nlg-metrics/new_result_for_eval/6_12_mistral_eval_{eval_arg}_{version}_explore_pad_eos_token.json",format_result,True)
# 需要人工筛查和删除 Therapapist


# %%
# write_file(f"/home/ckqsudo/code2024/Mistral-7b-finetune/metrics/nlg-metrics/new_result_for_eval/mistral_eval_{eval_arg}_{version}_not_explore.json",format_result,True)

# %%
# import argparse
# import json
# import tabulate
# import os
# import sys
# # 添加特定路径
# path_to_directory = '/home/ckqsudo/code2024/Mistral-7b-finetune/metrics/nlg-metrics'
# sys.path.append(path_to_directory)
# from nlg_metrics.metrics import Metrics

# # from logging import 
# import sys
# # logger.info(f"{sys.getrecursionlimit()=}")
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(8735 * 2080 + 10)

# parser = argparse.ArgumentParser()

# #         "rouge-1": Rouge1,
#         # "rouge-2": Rouge2,
#         # "rouge-l": RougeL,
#         # "bleu": Bleu,
#         # "self-bleu": SelfBleu,
#         # "meteor": Meteor,
#         # "ppl": Perplexity
# print(cfg.metrics)
# metrics = Metrics(metrics=cfg.metrics, path=cfg.ppl_model_path)
# with open(cfg.input, "r") as f:
#     inputs = json.load(f)
# results = metrics.calc(inputs=inputs, verbose=cfg.verbose)
# input_file_name=cfg.input
# if "/" in input_file_name:
#     input_file_name=input_file_name.split("/")[-1]
# print(input_file_name.split('.')[0])

# print(results)
# mean_result={}
# for metric in metrics.metrics:
#     score = [res[metric] for res in results]
#     mean_sore =sum(score) / len(score)
#     mean_result[metric] =mean_sore
# sorted_dict = {k: mean_result[k] for k in sorted(mean_result)}
# mean_result=sorted_dict

# output_dir="/home/ckqsudo/code2024/Mistral-7b-finetune/metrics/nlg-metrics/6_6_fuck_simple"
# if os.path.exists(output_dir+"/"+input_file_name+".json")==True:
#     input_file_name+="exist"
# with open(output_dir+input_file_name+".json","w") as f:
#     json.dump(mean_result, f)

# # print(sorted_dict)
# print(input_file_name.split('.')[0])
# print(mean_result)


# # print("Table saved to table_output.txt")
# # #  meteor │   self-bleu │   rouge-2 │     bleu │   rouge-1 │   data size │
# # ╞══════════╪═════════════╪═══════════╪══════════╪═══════════╪═════════════╡
# # │ 0.347502 │           1 │  0.409538 │ 0.381412 │  0.785638 │
# # 除了PPL 和模型相关，其他的都好算！！！


# %%
# eval_arg

# %%


# %%
# write_file(f"/home/ckqsudo/code2024/Mistral-7b-finetune/metrics/nlg-metrics/Input_for_eval/mistral_eval_{eval_arg}.jsonl",format_result,True)

# %%
# result[0]["history"]

# %%


# %%
# format_result[0:2]

# %%


# %%
len(format_result)


# %%
# input_ids=tokenizer.apply_chat_template(item[0]["messages"], tokenize=True,return_tensors="pt", truncation=False)

# %%
# input_ids

# %%
# input_ids.cuda()
# with torch.inference_mode():
#     outputs = merged_model.generate(input_ids=input_ids, max_new_tokens=512, do_sample=True, top_p=0.5,temperature=0.7)

#     print(f"Prompt:\n{print_prompt}\n")
#     print(f"\nGenerated instruction:\n{tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=False)[0][len(print_prompt):]}")
# # print(f"\nGround truth:\n{sample['output']}")

# %%
# tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0]

# %%
print_prompt


