import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import os
import pandas as pd
from tqdm import tqdm

# 将上一级目录添加到系统路径
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from llm_chat import llm_chat_with_prompt

def fetch_webpage_content(url):
    # 发起HTTP请求获取网页内容
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # 查找 id 为 'js_content' 的 div
    content_div = soup.find(id="js_content")
    # 如果找到了内容，去掉所有标签
    if content_div:
        return content_div.get_text(strip=True)
    else:
        return ""

def generate_summary(text_content):
    # 调用自定义的llm_chat生成摘要
    prompt = "你是一个摘要生成器，你擅长从一篇文章中提取关键信息。现在开始， 请生成这篇文章的摘要。"
    summary = llm_chat_with_prompt(prompt, text_content)
    return summary

import concurrent.futures

def process_row(index_row):
    index, row = index_row
    url = row['URL']
    try:
        html_content = fetch_webpage_content(url)
        full_text = extract_text_from_html(html_content)
        summary = generate_summary(full_text)
        # print("html_content", html_content)
        # print("full_text", full_text)
        # print("summary", summary)
        print(f"已生成第 {index + 1} 行摘要。")
        return (index, summary)
    except Exception as e:
        print(f"处理URL失败：{url}。错误信息：{e}")
        return (index, "摘要生成失败")

def process_csv(input_csv, output_csv, max_workers=100):
    # 读取CSV文件，添加列名
    df = pd.read_csv(input_csv, names=["标题", "URL", "日期"])
    # 初始化摘要列
    df['摘要'] = ""

    # 使用并发处理
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(tqdm(executor.map(process_row, df.iterrows()), total=len(df), desc="Processing"))

    # 写入摘要
    for index, summary in results:
        df.at[index, '摘要'] = summary

    # 保存到新的CSV文件
    df.to_csv(output_csv, index=False)
    print(f"处理完成，摘要已保存至新文件：{output_csv}")


if __name__ == "__main__":
    input_csv = "url.csv"  # 原始CSV文件
    output_csv = "url_with_summaries.csv"  # 带摘要的新CSV文件
    process_csv(input_csv, output_csv)