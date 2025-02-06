from tqdm import tqdm
import csv
import json
from zhipuai import ZhipuAI
import time

from config2 import api_key # 注意，这里的实现只支持glm系列，如果是你可以把config2换为config


# 工具：按照指定格式构造jsonl文件
def turn_to_jsonl(input_str, request_id):
    '''
    input_str: 输入字符串
    request_id: 请求id,字符串, 每个请求必须包含custom_id且是唯一的，用来将结果和输入进行匹配
    '''
    output_jsonl = {
        "custom_id": request_id,
        "method": "POST",
        "url": "/v4/chat/completions", 
        "body": {
            "model": "glm-4-flash", 
            "messages": [
                {"role": "system","content": "你是一个翻译家，你擅长把英文翻译成中文。现在开始， 每次你收到一个英文句子或者段落，都把它翻译成地道的中文。"},
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
def upload_file_and_create_batch(file_path):
    client = ZhipuAI(api_key=api_key)
    result = client.files.create(
        file=open(file_path, "rb"),
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
    while True:
        batch_job = client.batches.retrieve(create.id)
        print(batch_job)
        if batch_job.status == "completed":
            output_file_id = batch_job.output_file_id
            break
        time.sleep(1)
    print("批处理任务完成")
    print("--------------------------------")

    # 3. 下载批处理任务结果
    content = client.files.content(output_file_id)
    content.write_to_file(file_path.replace('.jsonl', 'Vbatch.jsonl'))
    print("--------------------------------")

    # 4. 删除文件
    result = client.files.delete(
        file_id = output_file_id      
    )
    print("--------------------------------")

# 3. 将jsonl文件转换为csv文件
def jsonl_to_csv(raw_csv, input_jsonl, output_csv):
    # 首先解析jsonl中的相关文件
    jsonl_dict = {}
    with open(input_jsonl, mode='r', encoding='utf-8') as infile:
        for line in infile:
            temp = json.loads(line)
            id = temp['custom_id'].split('_')[0]
            type = temp['custom_id'].split('_')[1]
            value = temp['response']['body']['choices'][0]['message']['content']
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
                    row['Title'] = jsonl_dict[str(row_num)]['Title']
                    row['Summary'] = jsonl_dict[str(row_num)]['Summary']
                    row['First Author'] = jsonl_dict[str(row_num)]['First Author']

                    # 将翻译结果写入新CSV文件
                    writer.writerow(row)



def arx_batch_to_ch():
    input_csv = 'arxiv_papers.csv'
    output_jsonl = 'arxiv_papers.jsonl'
    return_jsonl = 'arxiv_papersVbatch.jsonl'
    output_csv = 'arxiv_papers_ch.csv'
    translate_csv_to_jsonl(input_csv, output_jsonl)
    upload_file_and_create_batch(output_jsonl)
    jsonl_to_csv(input_csv, return_jsonl, output_csv)


if __name__ == "__main__":
    arx_batch_to_ch()
    
