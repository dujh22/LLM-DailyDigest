# 工具

这里将汇总一些用于科研的常用脚本。

### 1.  配置与聊天

* llm_chat.py: 包含与大型语言模型（LLM）聊天相关的代码。
* config2.py 和 config.py: 存储基本配置参数。
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
2. 其他

### 4. 数据文件

1. arxiv_papers_ch.csv: 存储已转换为中文的arxiv论文数据。
2. arxiv_papers.csv: 存储原始的arxiv论文数据。
3. arxiv_papersVbatch.jsonl: 存储批量处理的arxiv论文数据。
