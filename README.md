# LLM-DailyDigest 大模型日报

Stay up-to-date with the latest developments, news, and insights about Large Language Models (LLM). This repository is updated daily with curated content to help enthusiasts, researchers, and developers stay informed about the rapidly evolving field of LLMs.

## 📌 Features

- **Daily Updates**: New content is added every day, covering research papers, tools, breakthroughs, and industry news.
- **Curated Insights**: Focused on high-quality and impactful updates.
- **Community Contributions**: Contributions are welcome! Submit relevant updates via pull requests.

## 📂 Repository Structure

```
Repository Structure
├── README.md                # Overview of the repository
├── updates/                 # Folder containing daily updates
│   ├── 2025-01-26.md        # Example of a daily update file
│   ├── 2025-01-27.md        # Updates from the next day
│   └── ...                  # Daily updates continue
├── tools/                   # Useful tools or scripts related to LLM
│   ├── paper_summarizer.py  # Script to summarize research papers
│   └── ...                  # Additional utilities
├── resources/               # General resources on LLMs
│   ├── papers.md            # List of must-read papers
│   ├── datasets.md          # List of public datasets for LLM training
│   └── ...                  # Additional learning resources
└── CONTRIBUTING.md          # Guide for contributors
```

## 🚀 How to Use

To use the basic features, you can clone the repository with:

```
git clone https://github.com/dujh22/LLM-DailyDigest.git
```

To fetch updates without committing local changes, use:

```
git fetch origin
git reset --hard origin/main
```

1. Navigate to the `updates/` folder to see the daily updates.
2. Use scripts from the `tools/` folder for summarization or processing tasks.
3. Explore `resources/` for a curated list of learning materials and datasets.

## 🤝 Contributing

We welcome contributions! Please check `CONTRIBUTING.md` for guidelines on submitting updates, tools, or additional resources.

## 📅 Update Log

TO DO LIST:

1. Add a program for automatic daily report construction for public accounts.
   - Reference: https://github.com/captainChaozi/wx-ai-collect/blob/main/app/msg_process/llm_chains.py
   - Reference: https://miracleplus.feishu.cn/wiki/LLQewHYx1ilmlpkxHUqc42L8nzf
3. Support changing different query queries
4. Support supplementing historical reports that have not been formed
5. Support data summary of all reports up to history
6. Add programs that can be accessed externally, such as deploying on GitHub
   - Reference: https://github.com/Estelle925/SmartBrief
7. Optimize the function of obtaining code links in arx.py
8. Optimize the function of obtaining star numbers in arx.py
9. Optimize the translation accuracy in tools/arx_batch_to_ch.py
10. Support ACM classification in tools/arx_batch_to_ch.py, such as I.2.7, see https://arxiv.org/category_taxonomy

FINISH:

[2025-02-07] Optimized arxiv pipeline construction | Automatically added arxiv daily reports from 1.27 to 2.6

* Optimized arxiv pipeline construction:
  1. Modified naming to add arxiv distinction
  2. Added readme under the update folder
  3. Optimized classification tree
  4. Optimized arxiv export parameters, such as including classification
  5. Modified arxiv search input parameters to be customizable
  6. Optimized arxiv data download process to ensure automatic verification and complete download, trying to see if waiting time is needed
  7. Supported two types of classification in the daily report: arxiv's own classification and user's own classification
* Added daily automatic execution program
  1. Connected arxiv download process and Chinese report generation process
  2. Connected arxiv download process and Chinese report generation process + uploaded to GitHub project
  3. Connected arxiv download process and Chinese report generation process + uploaded to GitHub project + daily background automatic execution
* Automatically added arxiv daily reports from 1.27 to 2.6, 1.27 may be incomplete

[2025-02-06] Added arxiv automatic daily report construction program | Automatically added 2.5 arxiv daily report

[2025-01-31] Manually added daily reports from 1.28 to 1.31

[2025-01-28] Manually added daily report

[2025-01-27] Manually added daily report

[2025-01-26] Project construction | Manually added daily report

## 🌟 License

This repository is licensed under the MIT License.
