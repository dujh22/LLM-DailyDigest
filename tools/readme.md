# 工具

这里将汇总一些用于科研的常用脚本。

为了充分利用本项目的工具，请先行构建好python环境（推荐采用conda构建，python使用3.10.0)。具体见requirements.txt。同时注意完成下述配置config。

### 1.  配置与聊天

* llm_chat.py: 包含与大型语言模型（LLM）聊天相关的代码。
* config2.py 和 config.py: 存储基本配置参数。
  * 这里只提供了config.py
  * 最直接的办法是复制一个config.py文件,重命名为config2.py，然后把里面的api_key改为你的api_key
* requirements.txt: 列出项目所需的Python包及其版本。

### 2. 下载工具

1. arx.py 用于下载arxiv上的相关论文。
2. arx_to_ch.py: 用于将arxiv论文转换为中文。
3. arx_batch_to_ch.py: 批量将arxiv论文转换为中文。

### 3. 日报生成

1. paper_summarizer.py: 用于论文摘要。

   ```
   python paper_summarizer.py --data_file /Users/djh/Documents/GitHub/LLM-DailyDigest/tools/arxiv_papers_ch.csv --date 2025-02-05  --is_summary True

   其中，第二个参数是中文的csv路径，第三个参数是日期，第四个参数是是否总结之前的文献。


   ```

   注意⚠️：你需要确保在传递日期参数时，使用正确的短破折号。在日期格式中，应该使用标准的短破折号来分隔年、月、日。而不是长破折号。
2. 自动执行日报生成脚本tools/arx_dairy_summarizer.sh。

   ⚠️ 这里是按照mac开发的脚本，注意如果是linux系统，打开和屏蔽该脚本中提示的行。

   ```
   chmod a+x arx_dairy_summarizer.sh
   ./arx_dairy_summarizer.sh
   ```
3. 自动执行日报生成并提交到github的脚本tools/arx_dairy_summarizer_and_to_github.sh。

   ⚠️ 这里是按照mac开发的脚本，注意如果是linux系统，打开和屏蔽该脚本中提示的行。

   ```
   chmod a+x arx_dairy_summarizer.sh
   ./arx_dairy_summarizer.sh
   ```
4. 每日在凌晨1点自动执行arx_dairy_summarizer_and_to_github.sh脚本。

   1. 详细说明参见tools/arx_dairy_summarizer_tmux.md
   2. 具体会用到tools/arx_dairy_summarizer_tmux.sh，注意调整其中相关的参数。
   3. 注意：
      1. 如果github网络连接有问题，你在arx_dairy_summarizer_tmux.sh中调用的脚本可以是arx_dairy_summarizer.sh，也就是不进行自动的上传github。
      2. 针对其中新增的如下三个文件，可以手动上传到github逐日，我们后续会优化这个问题：
         ```
         tools/arxiv_papers_$timestamp.csv
         tools/arxiv_papers_ch_$timestamp.csv
         updates/arxiv_daily_report_$yesterday.md

         上传的命令可以参考如下：

         如果你已经初始化和添加过远程仓库，可以跳过这几行：
         git init
         git remote add origin https://github.com/dujh22/LLM-DailyDigest.git

         你可以通过git remote -v来检查是否有远程仓库

         你可以继续执行如下操作：
         git add tools/arxiv_papers_$timestamp.csv
         git add tools/arxiv_papers_ch_$timestamp.csv
         git add updates/arxiv_daily_report_$yesterday.md
         git commit -m "添加了三个文件"
         git push origin main
         ```
5. 其他

### 4. 数据文件

1. arxiv_papers_ch.csv: 存储已转换为中文的arxiv论文数据。
2. arxiv_papers.csv: 存储原始的arxiv论文数据。
3. arxiv_papersVbatch.jsonl: 存储批量处理的arxiv论文数据。
