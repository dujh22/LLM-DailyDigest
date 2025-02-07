from tqdm import tqdm
import csv
import json
from zhipuai import ZhipuAI
import time
import ast
import os
import argparse

from config2 import api_key # 注意，这里的实现只支持glm系列，如果是你可以把config2换为config,最直接的办法是复制一个config.py文件,重命名为config2.py，然后把里面的api_key改为你的api_key

# 预先读入分类
categories = {}
with open('category.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        categories[row['字段']] = row['学科（中文）']

# 工具：按照指定格式构造jsonl文件
def turn_to_jsonl(input_str, request_id):
    '''
    input_str: 输入字符串
    request_id: 请求id,字符串, 每个请求必须包含custom_id且是唯一的，用来将结果和输入进行匹配
    '''
    prompt = '''您是一位精通「源文本语言」与「目标语言」文化和语言的翻译专家。
# User prompt
源本文 
""" 
{input1} 
""" 
## 翻译要求:
1.忠实于"源文本"，确保每个句子都得到准确且流畅的翻译。
2.大额数字的翻译需准确无误，符合简体中文的表达习惯。

##任务:
1.仔细研究并深入理解"源文本"的内容、上下文、语境、情感以及和目标语言的文化细微差异。
2.根据「翻译要求」将"源文本"准确翻译为{{input 2}}。
3.确保翻译对目标受众来说准确、自然、流畅，必要时可以根据需要调整表达方式以符合文化和语言习惯。

注意:不要输出任何额外的内容，只能输出翻译内容。这一点非常关键。'''

    output_jsonl = {
        "custom_id": request_id,
        "method": "POST",
        "url": "/v4/chat/completions", 
        "body": {
            "model": "glm-4-flash", 
            "messages": [
                {"role": "system","content": "你是一个翻译家，你擅长把英文翻译成中文。现在开始， 每次你收到一个英文短语、句子或者段落，都把它翻译成地道的中文。"},
                {"role": "user", "content": input_str}
            ],
            "temperature": 0.1 # 温度，0-1之间，越高越随机
        }
    }
    return output_jsonl

# 1. 读取arxiv_papers.csv文件并构建jsonl文件
def translate_csv_to_jsonl(input_csv, output_jsonl):
    with open(output_jsonl, mode='w', encoding='utf-8', newline='') as outfile:
        with open(input_csv, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in tqdm(reader, desc="To jsonl"):
                # 获取当前是第几行
                row_num = reader.line_num - 1
                outfile.write(json.dumps(turn_to_jsonl(row['Title'], str(row_num)+'_Title'), ensure_ascii=False) + '\n')
                outfile.write(json.dumps(turn_to_jsonl(row['Summary'], str(row_num)+'_Summary'), ensure_ascii=False) + '\n')
                outfile.write(json.dumps(turn_to_jsonl(row['First Author'], str(row_num)+'_First Author'), ensure_ascii=False) + '\n')

# 2. 上传文件并创建batch任务
def upload_file_and_create_batch(upload_jsonl, return_jsonl, error_jsonl):
    client = ZhipuAI(api_key=api_key)
    result = client.files.create(
        file=open(upload_jsonl, "rb"),
        purpose="batch"
    )
    print("批处理文件ID: ", result.id)
    print("--------------------------------")
    
    create = client.batches.create(
        input_file_id=result.id,
        endpoint="/v4/chat/completions", 
        auto_delete_input_file=True,
        metadata={
            "description": "Sentiment classification"
        }
    )
    print("批处理任务: ", create)
    print("--------------------------------")
    output_file_id = ""
    error_file_id = ""
    used_time = 0
    while True:
        batch_job = client.batches.retrieve(create.id)
        print("当前批处理任务状态: ",batch_job.status, "已用时间: ", used_time, "秒")
        if batch_job.status == "completed":
            output_file_id = batch_job.output_file_id
            error_file_id = batch_job.error_file_id
            break
        time.sleep(1)
        used_time += 1
    print("批处理任务完成")
    print("--------------------------------")

    # 3. 下载批处理任务结果
    content = client.files.content(output_file_id)
    content.write_to_file(return_jsonl)
    print("下载批处理任务结果-----------------")

    # 4. 下载批处理任务错误结果
    if error_file_id != "":
        error = client.files.content(error_file_id)
        error.write_to_file(error_jsonl)
        print("下载批处理任务错误结果-----------------")
    else:
        # 生成一个空的错误文件
        with open(error_jsonl, mode='w', encoding='utf-8') as outfile:
            outfile.write('')
        print("无错误结果-------------------------")

    # 5. 删除文件
    result = client.files.delete(
        file_id = output_file_id      
    )
    if error_file_id != "":
        result = client.files.delete(
            file_id = error_file_id
        )
    print("删除文件-------------------------")

# 3. 将jsonl文件转换为csv文件
def jsonl_to_csv(raw_csv, return_jsonl, error_jsonl, output_csv):
    # 首先解析jsonl中的相关文件
    jsonl_dict = {}
    with open(return_jsonl, mode='r', encoding='utf-8') as infile, open(error_jsonl, mode='r', encoding='utf-8') as errorfile:
        for line in infile:
            temp = json.loads(line)
            id = temp['custom_id'].split('_')[0]
            type = temp['custom_id'].split('_')[1]
            value = temp['response']['body']['choices'][0]['message']['content']
            if id not in jsonl_dict:
                jsonl_dict[id] = {}
            jsonl_dict[id][type] = value

        for line in errorfile:
            temp = json.loads(line)
            id = temp['custom_id'].split('_')[0]
            type = temp['custom_id'].split('_')[1]
            value = "None"
            if id not in jsonl_dict:
                jsonl_dict[id] = {}
            jsonl_dict[id][type] = value

        # 打开原始文件
        with open(raw_csv, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            # 获取CSV的字段名称
            fieldnames = reader.fieldnames

            # 打开用于保存翻译结果的新CSV文件
            with open(output_csv, mode='w', encoding='utf-8', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                # 遍历每一行，翻译特定字段
                for row in tqdm(reader, desc="Translating"):
                    # 获取行数
                    row_num = reader.line_num - 1
                    # 翻译Title, Summary, First Author等需要翻译的字段
                    row['Title'] = jsonl_dict[str(row_num)]['Title'] if jsonl_dict[str(row_num)]['Title'] != 'None' else row['Title']
                    row['Summary'] = jsonl_dict[str(row_num)]['Summary'] if jsonl_dict[str(row_num)]['Summary'] != 'None' else row['Summary']
                    row['First Author'] = jsonl_dict[str(row_num)]['First Author'] if jsonl_dict[str(row_num)]['First Author'] != 'None' else row['First Author']
                    # 字符串转list，比如['astro-ph.CO', 'astro-ph.GA']
                    temp_categories = ast.literal_eval(row['Categories'])
                    row['Categories'] = []
                    for category in temp_categories:
                        if category in categories.keys():
                            row['Categories'].append(categories[category])
                
                    # 将翻译结果写入新CSV文件
                    writer.writerow(row)



def arx_batch_to_ch():
    # 时间戳
    # current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    # 如果调用的文件的时间戳不是上面这个，需要手动输出
    parser = argparse.ArgumentParser(description="批量翻译arxiv论文")
    parser.add_argument("--time", help="指定时间戳", default='2025_02_07_11_10_39')
    args = parser.parse_args()

    input_csv = 'arxiv_papers_' + args.time + '.csv'
    upload_jsonl = 'arxiv_papers_' + args.time + '_upload.jsonl'
    return_jsonl = 'arxiv_papers_' + args.time + '_return.jsonl'
    error_jsonl = 'arxiv_papers_' + args.time + '_error.jsonl'
    output_csv = 'arxiv_papers_ch_' + args.time + '.csv'
    translate_csv_to_jsonl(input_csv, upload_jsonl)
    upload_file_and_create_batch(upload_jsonl, return_jsonl, error_jsonl)
    jsonl_to_csv(input_csv, return_jsonl, error_jsonl, output_csv)
    # 删除upload_jsonl和return_jsonl
    os.remove(upload_jsonl)
    os.remove(return_jsonl)
    os.remove(error_jsonl)


if __name__ == "__main__":
    arx_batch_to_ch()
            
    
