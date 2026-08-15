# 大模型日报 LLM-DailyDigest

每日精选大模型（LLM）领域论文、开源工具与行业动态，自动抓取、中文摘要、主题/研究分类聚合。

🌐 **网站**：[https://dujh22.github.io/LLMDailyDigestWeb/](https://dujh22.github.io/LLMDailyDigestWeb/)
🔍 **项目解析**：[deepwiki.com/dujh22/LLM-DailyDigest](https://deepwiki.com/dujh22/LLM-DailyDigest)

## 🏗️ 项目架构

```
LLM-DailyDigest/
├── co_learner/          # 自动化系统：爬虫 + 内容代理（auto/briefing/info/content_agent）
├── tools/               # ArXiv 下载 / 批量翻译 / 论文总结 / 定时脚本
├── backend/             # 消息提交后端（Flask + LLM 抽取）
├── content/             # Hugo 内容
│   ├── updates/         # 每日日报（[[items]] 结构化）
│   ├── topic/           # 主题（自动聚合）
│   ├── research/        # 研究项目（自动聚合「相关工作」）
│   ├── resources/       # 学习资源
│   └── posts/           # 项目介绍
├── layouts/             # 布局（updates/topic/research 聚合逻辑）
├── archetypes/          # 内容模板
├── assets/              # 样式 / 品牌 logo
└── hugo.toml            # 配置
```

## 🌐 网站内容体系（Hugo + FixIt）

内容按三维度组织，结构化字段驱动**自动联动**，无需手工搬运。

### 内容模型

```
content/updates/<日期>.md   每日日报，含多条 [[items]]（一条消息一个 item）
content/topic/<主题>.md      主题页，自动聚合命中该主题的 items
content/research/<项目>.md   研究项目页，自动聚合归属该研究的 items（「相关工作」）
```

### item 字段（写在日报 front matter 的 `+++` 内）

| 字段                                    | 说明                                                   |
| --------------------------------------- | ------------------------------------------------------ |
| `id`                                  | 锚点（主题/研究页深链回日报）                          |
| `title` `summary`                   | 标题 / 一句话摘要                                      |
| `subtopic`                            | 子主题，决定在主题页里归入哪个**栏目**           |
| `topics`                              | 主题数组，决定出现在哪些**主题页**               |
| `research`                            | 研究项目数组，决定出现在哪些**研究页**（可留空） |
| `source`                              | 来源（公众号 / arxiv 分类 / 站点）                     |
| `paper` `code` `dataset` `link` | 论文 / 代码 / 数据集 / 原文链接（留空不显示）          |
| `content` `purpose`                 | 正文（LLM 浓缩） + 用途与启示（多行 Markdown）         |
| `notes`                              | 原始逐字笔记（迁移脚本保留原文不浓缩，日报页可折叠展开） |

> `topics` / `research` 取值需与 `content/topic/`、`content/research/` 的**文件名**一致。

### 双聚合

- **主题页**：底部「相关消息」，按 `subtopic` 分栏。
- **研究页**：底部「相关工作」，页头展示**提出者**与**最早研究时间**。

当前研究项目（提出者：杜晋华）：LogicEvolve (2025-05)、EvolveLRM (2026-01)、HarnessEvolve / SwarmEvolve (2026-03)、Groom (2026-05)、Awesome-RSI (2026-06)、DataEvolve / EvalEvolve (2026-08)。

### 本地预览

```bash
hugo server --baseURL http://localhost:1313/ -D
```

## 🛠️ 消息提交后端

`backend/` 提供本地 Web 表单，录入单条消息并自动追加到当日日报，支持 LLM 从原始文本抽取字段。另含**批处理录入**（`/batch/new`）、**当日推荐**（`/recommend`）与**主题归并**（`/merge`）三个辅助页面。

```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cp ../api_key.txt.example ../api_key.txt   # 仓库根目录，填入 key（已 gitignore）

python app.py          # → http://localhost:5050
```

> 默认 GLM 网关 `https://api-gateway.glm.ai/v1`、模型 `gpt-5.6-sol`，可用 `LLM_BASE_URL` / `LLM_MODEL` 覆盖。

**单条提交**：粘原始信息 →「🔗 解析链接」「✨ LLM 抽取」自动填表。原始信息含 github / arxiv / HuggingFace / 微信公众号等链接时会**自动抓取正文**供抽取；抓不到的链接可手动补充（补充内容仅用于抽取，不写入 `notes`）。核对后「➕ 提交」追加一条 `[[items]]`。建议同时开 `hugo server`，提交后刷新即见。

**历史迁移**：表单「目标日期」填 `YYYY-MM-DD`（或 `YYYYMMDD`）即可把条目写入对应历史日报（留空=今天）。可逐步把 `content/topic/*.md` 里的旧条目，按原始日期迁入对应日报并自动索引回主题页。

**批量迁移**（全自动，LLM 驱动）：

```bash
./backend/venv/bin/python backend/migrate_topic.py --topic 智能体 --dry        # 预览
./backend/venv/bin/python backend/migrate_topic.py --topic 智能体 --max 100    # 迁移单主题（上限 100/次）
./backend/venv/bin/python backend/migrate_topic.py --all --workers 4           # 全部主题，4 并发
```

脚本把主题正文按日期/编号锚点拆条 → 逐条送 LLM 结构化（含日期推断）→ 按条目日期写入对应历史日报（原始逐字笔记存入 `notes`，不浓缩）→ **从 topic 正文移除已迁出条目，仅保留笔记/洞察/无日期内容**。`--max` 为**每个主题**本次上限；`--dry` 不写盘。

**批处理录入** `/batch/new`：上传 txt 或粘贴多段（空行分隔每条）→ 生成批次 → 「自动处理全部」并发跑链接抓取 + LLM 抽取（默认 100 并发）→ 逐条状态流转到 `待核对 / 待介入`，人工只在「待介入」条目补充抓取失败的链接、在「待核对」条目核对提交。有链接失败的条目不消耗 LLM。「⚡ 一键自动处理并提交」可跳过人工核对整批直接提交（待介入条目除外，自动提交失败者保留待核对并显示原因）。

**当日推荐** `/recommend`：自动采集最近 24h 内与研究相关的内容，LLM 按各研究项目的「研究方向+范畴」画像判定相关性，勾选后一键导入批处理。公众号三级通道（appmsg 实时可选凭据增强 → 量子位官网实时 → [Wechat-Scholar](https://github.com/osnsyc/Wechat-Scholar) 学术 RSS 兜底 ≤12h）+ arXiv（cs.CL/cs.AI/cs.LG，24h 空窗自动放宽 48h/72h），按标题去重；**默认零配置可用**。结果按日缓存 `.recommend_cache/`，详见 `backend/README.md`。

**主题归并** `/merge`：左侧三级树「主题 ▸ 子主题 ▸ 文章」勾选若干标签 → 右侧填目标名 → 预览影响范围 → 执行。子主题按字符串全局归并；改写为原位替换、diff 最小，可 `git checkout` 回退。内置「🤖 LLM 归并推荐」自动聚类近义标签，支持单条采纳或勾选多条批量执行。

| 方法 | 路径                                    | 说明                                   |
| ---- | --------------------------------------- | -------------------------------------- |
| GET  | `/` `/batch/new` `/recommend` `/merge` | 单条提交 / 批处理 / 当日推荐 / 主题归并 页面 |
| GET  | `/api/topics` `/api/research` | 合法主题 / 研究列表                    |
| POST | `/api/extract`                        | `{raw, extra?}` → 链接抓取 + 结构化 JSON |
| POST | `/api/submit`                         | 追加 item 到当日日报（新主题自动建页） |
| POST | `/api/batch/create` `/api/batch/<id>/process` | 建批次 / 后台并发处理           |
| POST | `/api/batch/<id>/auto_submit` | 一键自动处理并提交（跳过核对） |
| GET/POST | `/api/recommend/status` `/api/recommend/collect` `/api/recommend/credentials` | 推荐状态/采集/凭据 |
| POST | `/api/recommend/to_batch` | 选中候选导入批处理 |
| POST | `/api/merge/preview_multi` `/api/merge/apply_multi` | 多组归并预览 / 批量执行   |

## 🚀 使用方法

```bash
git clone https://github.com/dujh22/LLM-DailyDigest.git
```

**自动化流水线**（爬取 → 翻译 → 日报）：

```bash
cd co_learner && pip install -r requirements.txt
cp config.py config2.py        # 编辑 config2.py 填入 API 密钥

cd ../tools && pip install -r requirements.txt
python arx.py                  # 下载 ArXiv 论文
python arx_batch_to_ch.py      # 批量翻译
python paper_summarizer.py     # 生成日报
# 生成总结性日报：
python paper_summarizer.py --data_file <csv> --date <YYYY-MM-DD> \
  --dairy_report_dir tools/summary --is_summary True
```

**定时任务**：

```bash
chmod +x tools/arx_dairy_summarizer_tmux.sh
./tools/arx_dairy_summarizer_tmux.sh
```

## 📅 更新日志

**2026-08-16**

- 当日推荐 `/recommend`：自动采集最近 24h 相关内容（量子位官网 + 机器之心/新智元 Wechat-Scholar 学术 RSS + 可选 appmsg 实时增强 + arXiv 三分类，标题去重），LLM 按研究画像判定相关性，勾选一键导入批处理；默认零配置可用
- 批处理新增「⚡ 一键自动处理并提交」：跳过人工核对整批提交（待介入条目除外）
- arXiv 采集 24h 空窗自动放宽 48h/72h（公告批次时差）

**2026-08-12**

- 提交后端增强：原始信息含 github/arxiv/HuggingFace/微信公众号链接时自动抓取正文供抽取；抓不到可手动补充（仅用于抽取，不写入原始笔记）
- 批处理录入 `/batch/new`：txt/多段粘贴空行分段，并发（默认 100）自动抓取+抽取，条目状态机 `待核对 / 待介入`
- 主题归并 `/merge`：三级树勾选 + 预览/执行，子主题全局归并，LLM 归并推荐支持批量采纳执行；原位改写、diff 最小

**2026-08-07**

- 主页优化：蓝紫科技风、明暗切换、品牌 logo、导航/页脚
- 日报结构化：单条消息统一为 `[[items]]` 字段
- 主题/研究双聚合：按 `topics`/`research` 自动汇入，按 `subtopic` 分栏
- 主题自动扩展：LLM 推断新主题，提交时自动建页
- 新增「研究」栏目：8 个研究项目（详见上文）
- 消息提交后端：Flask 表单 + LLM 抽取

## 📞 联系

- **GitHub**：[dujh22/LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest)
- **Discussions**：[github.com/dujh22/LLM-DailyDigest/discussions](https://github.com/dujh22/LLM-DailyDigest/discussions)
- **邮箱**：dujh22@mails.tsinghua.edu.cn

## 📄 许可证

MIT，详见 [LICENSE](LICENSE)。
