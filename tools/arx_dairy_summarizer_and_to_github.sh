#!/bin/bash

# 设置项目路径
project_dir="/Users/djh/Documents/GitHub/LLM-DailyDigest"
# 进入项目路径
cd $project_dir
# 进入/tools路径
cd tools

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

# 获取前一天的时间戳 (YYYY-MM-DD) Mac 版本
yesterday=$(date -v-1d +'%Y-%m-%d')
# yesterday=$(date -d "yesterday" +'%Y-%m-%d') # Linux 版本
dairy_report_dir="$project_dir/updates"
# 生成日报
python paper_summarizer.py --data_file "arxiv_papers_ch_$timestamp.csv" --date $yesterday --dairy_report_dir $dairy_report_dir
# 日报生成结束后打印
echo "Generated daily report"

# 切换到项目目录
cd $project_dir || { echo "Failed to change directory to $project_dir"; exit 1; }

# 检查是否已初始化 Git 仓库
if [ ! -d ".git" ]; then
  echo "Git repository not initialized. Initializing now..."
  git init
  git remote add origin https://github.com/dujh22/LLM-DailyDigest.git
  echo "Git repository initialized and remote origin added."
fi

# 检查是否已经配置远程仓库
git remote -v | grep -q "https://github.com/dujh22/LLM-DailyDigest.git"
if [ $? -ne 0 ]; then
  echo "Remote repository URL is incorrect. Updating remote URL."
  git remote set-url origin https://github.com/dujh22/LLM-DailyDigest.git
fi

# 强制将新增的文件添加到 Git
git add -f tools/arxiv_papers_$timestamp.csv tools/arxiv_papers_ch_$timestamp.csv updates/arxiv_daily_report_$yesterday.md

# 提交更新
git commit -m "Update daily digest for $yesterday"

# 推送到 GitHub
git push origin main

# 打印成功消息
echo "Successfully pushed new files to GitHub."