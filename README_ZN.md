# 大模型日报 LLM-DailyDigest

时刻关注大型语言模型（LLM）的最新发展、新闻和见解。此仓库每日更新精选内容，通过大模型日报的方式，帮助爱好者、研究人员和开发者了解LLM领域的快速演变。

## 📌 功能

-**每日更新**：每天添加新内容，涵盖研究论文、工具、突破和行业新闻。

-**精选见解**：专注于高质量和有影响力的更新。

-**社区贡献**：欢迎贡献！通过拉取请求提交相关更新。

## 📂 仓库结构

```

仓库结构

├── README.md                # 仓库概述

├── updates/                 # 包含每日更新的文件夹

│   ├── 2025-01-26.md        # 每日更新文件示例

│   ├── 2025-01-27.md        # 下一天的更新

│   └── ...                  # 每日更新持续

├── tools/                   # 与LLM相关的有用工具或脚本

│   ├── paper_summarizer.py  # 用于总结研究论文的脚本

│   └── ...                  # 其他实用工具

├── resources/               # LLM的一般资源

│   ├── papers.md            # 必读论文列表

│   ├── datasets.md          # LLM训练的公共数据集列表

│   └── ...                  # 其他学习资源

└── CONTRIBUTING.md          # 贡献者指南

```

## 🚀 如何使用

如果只是基本的使用，你可以通过：`git clone https://github.com/dujh22/LLM-DailyDigest.git`

你可以通过：`git fetch origin` ，在不提交本地修改的情况上，新增远程以及修改的部分代码。如果需要直接覆盖本地代码，可使用

```
git fetch origin
git reset --hard origin/main
```

1. 浏览 `updates/` 文件夹查看每日更新。
2. 使用 `tools/` 文件夹中的脚本进行总结或处理任务。
3. 探索 `resources/` 以获取精选的学习材料和数据集列表。

## 🤝 贡献

我们欢迎贡献！如果你希望参与共建，你可以具体查看 `CONTRIBUTING.md` 以获取有关提交更新、工具或其他资源的指南。

## 📅 更新日志

TO DO LIST:

1. 新增公众号自动日报构建程序

   1. 可参考 https://github.com/captainChaozi/wx-ai-collect/blob/main/app/msg_process/llm_chains.py
   2. 可参考 https://miracleplus.feishu.cn/wiki/LLQewHYx1ilmlpkxHUqc42L8nzf
2. 支持更换不同的查询quert
3. 支持历史未形成日报的补充
4. 支持历史截止所有日报的数据汇总⭕️
5. 新增对外可以访问程序，比如部署在github上

   1. 可参考https://github.com/Estelle925/SmartBrief
6. 优化arx.py中代码链接获取函数
7. 优化arx.py中代码星星数量获取函数
8. 优化tools/arx_batch_to_ch.py中的翻译准确性
9. 支持tools/arx_batch_to_ch.py中支持ACM分类，比如I.2.7 之类的，详见https://arxiv.org/category_taxonomy

FINISH:

[2025-02-13] 更新数据集获取源

[2025-02-08] 修改自动运行脚本的潜在bug✅ 25min

[2025-02-07] 优化arxiv完成构建pipeline ｜ 自动新增1.27～2.6arxiv日报

* 优化arxiv完成构建pipeline：

  1. 修改命名添加arxiv区别位✅
  2. 新增update文件夹下readme✅ 18min
  3. 优化分类树 ✅ 7min
  4. 优化arxiv导出参数，比如包含分类  37+ 1131停滞
  5. 修改arxiv检索传入参数可以自定义✅ 11min
  6. 优化arxiv数据下载流程，保证自动完成检验，确保全部下载，尝试看是否需要等待时间✅ 1h30min
  7. 日报中支持根据arxiv自行的分类和用户本身自己的分类两种 ✅
* 新增每日可以自动执行程序✅

  1. 连接arxiv下载流程和汉化生成日报流程 1h52min✅
  2. 连接arxiv下载流程和汉化生成日报流程+上传github项目中✅ 1h15，由于公司防火墙限制所以不确定是否能成功❌
  3. 连接arxiv下载流程和汉化生成日报流程+上传github项目中+每日后台自动执行 49min
* 自动新增1.27～2.6arxiv日报✅，1.27可能不全❌

[2025-02-06] 新增arxiv自动日报构建程序 | 自动新增2.5arxiv日报

[2025-01-31] 1.28~1.31日报手动新增

[2025-01-28] 日报手动新增

[2025-01-27] 日报手动新增

[2025-01-26] 项目构建 | 日报手动新增

## 🌟 许可证

此仓库采用 MIT 许可证。
