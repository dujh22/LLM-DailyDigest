#!/bin/bash

# 设置项目路径
project_dir="/Users/djh/Documents/GitHub/LLM-DailyDigest"

# 获取时间戳,格式为2025_02_07_11_10_39
timestamp=$(date +'%Y_%m_%d_%H_%M_%S')
# 打印时间戳
echo "Timestamp: $timestamp"

# 下载数据
filename="arxiv_papers_$timestamp.csv"
python arx.py --filename $filename
# 下载结束后打印
echo "Downloaded data"

# 处理数据
python arx_batch_to_ch.py --time $timestamp
# 处理结束后打印
echo "Processed data"

# 获取前一天的时间戳 (YYYY-MM-DD)
yesterday=$(date -v-1d +'%Y-%m-%d')
dairy_report_dir="$project_dir/updates"
# 生成日报
python paper_summarizer.py --data_file "arxiv_papers_ch_$timestamp.csv" --date $yesterday --dairy_report_dir $dairy_report_dir
# 日报生成结束后打印
echo "Generated daily report"