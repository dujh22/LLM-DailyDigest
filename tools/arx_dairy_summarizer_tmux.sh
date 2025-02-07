#!/bin/bash

# tmux 会话名称
session_name="arx_dairy_session"

# Conda 环境名称
conda_env="o1"

# 检查 tmux 会话是否已经存在
tmux has-session -t $session_name 2>/dev/null
if [ $? != 0 ]; then
  # 创建一个新的 tmux 会话
  tmux new-session -d -s $session_name

  # 激活 Conda 环境并运行脚本
  tmux send-keys -t $session_name "source /path/to/miniconda3/bin/activate $conda_env" C-m
  tmux send-keys -t $session_name "chmod a+x /path/to/arx_dairy_summarizer_and_to_github.sh" C-m
  tmux send-keys -t $session_name "/path/to/arx_dairy_summarizer_and_to_github.sh && tmux kill-session -t $session_name" C-m
else
  # 如果会话已经存在，创建一个新的会话
  new_session_name="${session_name}_$(date +'%Y%m%d%H%M%S')"
  tmux new-session -d -s $new_session_name

  # 激活 Conda 环境并运行脚本
  tmux send-keys -t $new_session_name "source /path/to/miniconda3/bin/activate $conda_env" C-m
  tmux send-keys -t $new_session_name "chmod a+x /path/to/arx_dairy_summarizer_and_to_github.sh" C-m
  tmux send-keys -t $new_session_name "/path/to/arx_dairy_summarizer_and_to_github.sh && tmux kill-session -t $new_session_name" C-m
fi
