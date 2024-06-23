# %%
# 载入
import json
input_file_path="/home/ckqsudo/code2024/0dataset/E-bed/Chinese/中文数据_处理错reasoning_分离长对话数据_分离label_对话人.json"
with open(input_file_path,"r",encoding="utf-8") as i_f:
    cn_data=json.load(i_f)

# %%
# dialog_id=0
cn_dialog_data=[]
for x,item in enumerate(cn_data):
    if item['key']=="fewshot":
        new_dialog_json=[]
        new_list={"unit_id":item["unit_id"],"dialog_list":[]}
        for y,dialog_item in enumerate(item['dialog']):
            # print(dialog_item)
            new_unit={"id":dialog_item["id"],"participant":dialog_item["participant"],"text":dialog_item["text"]}
            new_list['dialog_list'].append(new_unit)
            # new_list["dialog_list"]
        cn_dialog_data.append(new_list)

# %%
from pyexpat.errors import messages
import tiktoken
# 2. Load an encoding
# 使用tiktoken.get_encoding()按名称加载编码。

# 第一次运行时，它将需要互联网连接进行下载。后续运行不需要互联网连接。

encoding = tiktoken.get_encoding("cl100k_base")
# 使用tiktoken.encoding_for_model()函数可以自动加载给定模型名称的正确编码。

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
# 3. Turn text into tokens with encoding.encode()
# The .encode() method converts a text string into a list of token integers.
encoding.encode("tiktoken is great!")
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """返回文本字符串中的Token数量"""
    num_tokens=0
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
def calculate_messages(messages:list) -> int:
    """返回总的message长度"""
    counter=0
    for mess in messages:
        counter+=num_tokens_from_string(mess.content,"cl100k_base")
    return counter
num_tokens_from_string(json.dumps(cn_data),"cl100k_base")
# 2554978
# 1937335
# 2541877

# %%
print(len(cn_dialog_data))

# %%
from z6_prompt import *
# print(input_str) 
# from z6_prompt import *
import json

# %%
# from dotenv import load_dotenv
import os
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage,AIMessage
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(temperature=0,model="gpt-3.5-turbo")
long_chat =ChatOpenAI(temperature=0,model="gpt-3.5-turbo-16k")


# %%

# question=HumanMessage(content="请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"+json.dumps(cn_dialog_data[315]['dialog_list'],ensure_ascii=False))

# messages.append(question)

# %%
import os 
cache_dir_path="/home/ckqsudo/code2024/0dataset/E-bed/Chinese/ChatGPT_缓存文件夹"
def get_beg_idx(dir_path):
    files=os.listdir(dir_path)
    if len(files)==0:
        beg_idx=0
    else:
        idx_list=[]
        files.sort()
        for f in files:
            tmp=f.split("_")[-1].split(".")[0]
            idx_list.append(int(tmp))
        beg_idx=max(idx_list)
    return beg_idx
beg_idx=get_beg_idx(cache_dir_path)

# %%
beg_idx

# %%
messages = [
    SystemMessage(
        content="我希望你扮演一个中文语法和心理咨询专家，你需要根据语境纠正下列文本中的OCR的语法错误和中文符号使用错误。我希望你以json格式输出纠正错误OCR识别后的结果。json元素的键值包括：'id','participant','text','reason',其中'id','participant' 保留原始数据，不得修改，如果text中有语法或符号错误，输出修改后结果。'reason'记录修改原因，如果没有修改，reason值为空。请不要大幅度修改句子结构，主要修改错词和错误的中文标点符号。下面为三个例子："
    ),
    HumanMessage(
        content=r"""请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"""+input_str
    ),
    AIMessage(content=output_str),
    HumanMessage(
        content=r"""请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"""+input_str2
    ),
    AIMessage(
        content=output_str2
    ),
    HumanMessage(content=r"""请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"""+input_str3),
    AIMessage(
        content=output_str3
    ),
    HumanMessage(content="请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"+json.dumps(cn_dialog_data[315]['dialog_list'],ensure_ascii=False))
]

# %%
len(messages),beg_idx

# %%
beg_idx=get_beg_idx(cache_dir_path)

# %%
beg_idx
error_index=[]
# %%
# beg_idx=0
import json
import time
cache_dir="/home/ckqsudo/code2024/0dataset/E-bed/Chinese/ChatGPT_缓存文件夹"
print("起始标签",beg_idx)
for x,dialog_item in enumerate(cn_dialog_data):
    if x>=beg_idx:
        file_name="d"+"_"+str(x)+".json"
        print(file_name)
        with open(cache_dir+"/"+file_name,"w",encoding="utf-8") as o_f:
            response=None
            question=HumanMessage(content="请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"+json.dumps(dialog_item['dialog_list'],ensure_ascii=False))
            messages[-1]=question
            total_tokens=calculate_messages(messages)
            last_tokens=num_tokens_from_string(question.content,"cl100k_base")
            # if last_tokens*1.5> 16385 or total_tokens*1.2>16385:
            #     print(file_name,"片段过长，需要单独处理")
            #     continue
            try:
                if last_tokens*2/3>4096 or total_tokens>4096-100:#需要用long
                    response=long_chat(messages).content
                else:
                    response=chat(messages).content
                response_json=json.loads(response)
                json.dump(response_json,o_f,ensure_ascii=False)
            except Exception as e:
                print(e)
                print(file_name,"出现错误，需要单独处理")
                error_index.append(x)
                print(error_index)
            continue
        time.sleep(5)
"""          
try:
    2/0
except Exception as e:
    print(e)
    # pass
continue
"""
# %%


# %%
# messages
# HumanMessage(content="请你帮我纠正下面这段心理咨询对话OCR后的结果，以json数组形式输入，以json数组的形式输出:"+json.dumps(cn_dialog_data[315]['dialog_list'],ensure_ascii=False))

# %%


# %%


# %%
# testfiles=["d_1.json","d_21.json","d_14"]
# testfiles.sort()
# print(testfiles)


