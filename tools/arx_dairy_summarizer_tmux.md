# 自动执行arx_dairy_summarizer_and_to_github.sh脚本 🎯

使用 tmux 完成这个任务，并且相对于直接使用 cron，tmux 可以提供更多的灵活性和可视化的操作。

## 1. 前置操作 🛠️

你需要确保你已经安装了tmux：

```
apt-get update
apt-get install tmux
```

你需要确保你已经安装了cron：

你需要确保你已经安装好了conda环境：

```
conda create -n o1
conda activate o1
conda install python=3.10
pip install -r requirements.txt
```

通过 tmux 可以创建一个持久的会话并在其中运行脚本，这样即使在脚本运行过程中发生了网络或会话断开等问题，tmux 会话仍然存在，可以稍后重新连接。

## **2. 具体操作** 🚀

#### **步骤1：在 tmux 中运行你的脚本**

我们可以通过一个 bash 脚本来在 tmux 会话中自动执行需要的操作。

创建一个bash 脚本（例如 arx_dairy_summarizer_tmux.sh），并确保它会在一个新的 tmux 会话中激活 conda 环境，执行相应的脚本。

**解释：**

• **tmux has-session -t session_name**：检查是否已存在名为 session_name 的 tmux 会话。

• **tmux new-session -d -s session_name**：如果会话不存在，创建一个新的会话并在后台运行。

• **tmux send-keys -t session_name**：将命令发送到指定的 tmux 会话中执行。这里我们首先激活 conda 环境，然后运行脚本。

• **tmux attach -t session_name**：如果没有错误，附加到会话，这样你可以看到脚本的输出。

注意要给这个脚本赋权：

```
chmod a+x arx_dairy_summarizer_tmux.sh
```

---

#### **步骤2：定期自动执行脚本** ⏰

可以将这个脚本与 cron 配合使用，定期运行它。下面是如何设置 cron 来每天自动启动 tmux 会话并执行任务：

1. 打开 crontab 编辑器：

```
crontab -e
```

    如果出现选择，可以选1:/bin/nano

3. 添加以下行来设置每天在凌晨1点自动运行：

```
0 1 * * * /bin/bash /path/to/arx_dairy_summarizer_tmux.sh
```

这行表示每天凌晨1点（即01:00）执行 arx_dairy_summarizer_tmux.sh 脚本。

请按 `Ctrl + O` 保存文件，然后按 `Enter` 确认文件名。接着按 `Ctrl + X` 退出编辑器。这样就完成了定时任务的设置。

---

#### **步骤3：验证设置** ✅

可以通过运行 crontab -l 来验证定时任务是否已经添加。

**优势：**

• **持久性**：即使 tmux 会话被断开，脚本也会继续运行。可以随时重新附加到会话查看脚本的运行状态。

• **灵活性**：可以在会话中查看输出，进行调试，或停止/重启会话等。

通过 tmux，可以更灵活地管理脚本的运行状态，并避免一些 cron 可能会遇到的问题，尤其是与环境变量相关的问题。


## 3. 手动尝试

目前可能还存在bug，导致无法完成自动执行。可以参照对应的sh脚本进行手动执行，比如：

```
tmux new -s arx_dairy_session
conda activate llm
cd /workspace/dujh22/LLM-DailyDigest/tools
python arx.py --start_date "2025-02-07" --end_date "2025-02-12"

```
