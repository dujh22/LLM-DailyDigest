#!/bin/bash

# tmux 会话名称
session_name="arx_dairy_session"

# Conda 环境名称
conda_env="o1"

# tmux 会话是否已经存在，如果存在就附加到会话
tmux has-session -t $session_name 2>/dev/null
if [ $? != 0 ]; then
  # 创建一个新的 tmux 会话
  tmux new-session -d -s $session_name

  # 激活 Conda 环境并运行脚本
  tmux send-keys -t $session_name "source /path/to/miniconda3/bin/activate $conda_env" C-m
  tmux send-keys -t $session_name "chmod a+x /path/to/arx_dairy_summarizer_and_to_github.sh" C-m
  tmux send-keys -t $session_name "/path/to/arx_dairy_summarizer_and_to_github.sh" C-m
fi

# 附加到 tmux 会话
tmux attach -t $session_name