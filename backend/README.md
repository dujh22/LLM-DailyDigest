# 提交工具后端（本地）

交互式填写单条消息，追加到当日日报；支持 LLM 从原始文本自动抽取结构化字段。另含**批处理录入**与**主题/子主题归并**两个维护页面。

## 安装

```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## 配置 API Key（必需，用于 LLM 抽取）

在**仓库根目录**（不是 backend/）创建 `api_key.txt`，填入 GLM/OpenAI 兼容 api_key：

```bash
cp ../api_key.txt.example ../api_key.txt
# 然后编辑 ../api_key.txt 写入你的 key
```

> `api_key.txt` 已被 `.gitignore` 忽略，**不会上传 git**。缺失时启动会提示，且 `/api/extract` 不可用（表单手动填写仍可用）。

LLM 默认走 `https://api-gateway.glm.ai/v1`、模型 `gpt-5.6-sol`，可用环境变量覆盖：

```bash
export LLM_BASE_URL="https://api-gateway.glm.ai/v1"
export LLM_MODEL="gpt-5.6-sol"
```

## 运行

```bash
python app.py
# → http://localhost:5050
```

建议同时开 `hugo server --baseURL http://localhost:1313/ -D`；每次提交后刷新即可在日报页看到新条目。

## 工作流

1. （可选）粘原始信息 → 「🔗 解析链接」先看链接抓取状态，再「✨ LLM 抽取」自动填表
2. 核对字段，选好「主题」与「子主题」
3. 「➕ 提交」→ 追加一条 `[[items]]` 到 `content/updates/<当日>.md` 的 front matter

### 链接自动抓取

原始信息里若含 `github.com` / `arxiv.org` / `huggingface.co` / `mp.weixin.qq.com` 等链接，抽取时会**自动读取正文**供 LLM 使用：

- GitHub → API 取描述 + raw README；arXiv → 官方 API 取标题/作者/摘要；HuggingFace `/papers/<id>` → 复用 arXiv；微信公众号 → 取 `#js_content` 正文；其他 → 通用网页正文抽取。
- 抓取失败的链接会展开「✍️ 补充内容」框，手动粘贴正文后重抽即可。
- **抓取内容与补充内容仅用于本次抽取，绝不写入 `notes` 原始笔记**（`notes` 只回填你粘贴的原文）。

### 批处理录入 `/batch/new`

一次录入多条：上传 txt 或粘贴多段（**空行分隔每条**，行首 `1.` / `-` 等列表标记自动去除）→ 生成批次 → 总览页逐条「打开处理」。

- 「▶ 自动处理全部」并发执行链接抓取 + LLM 抽取（默认 `BATCH_WORKERS=100`，可用环境变量覆盖）。
- 每条状态：`待处理` → `处理中` → **`待核对`**（抽取完成，人工核对提交）/ **`待介入`**（有链接抓不到或抽取失败，需补充）→ `已完成`。
- 有抓取失败链接的条目**不消耗 LLM**，直接进入「待介入」等用户补充。

### 主题 / 子主题归并 `/merge`

随着标签增长，近义/重复标签（如「推理评估 / 推理评测」）需要归并：

- 左侧三级树「主题 ▸ 子主题 ▸ 文章」，勾选若干主题或子主题，右侧填目标名 → **🔍 预览**（显示影响条目/文件数、待删/保留主题页）→ **✓ 执行**。
- **子主题按字符串全局归并**；空样板源主题页自动删除，有自定义内容的保留并提示。
- 「🤖 LLM 归并推荐」自动聚类近义标签，可单条「采纳」或勾选多条「⚡ 批量采纳并执行」。
- 改写采用**原位替换**，未变化的 item 逐字保留，diff 最小；全程可 `git checkout -- content/updates/` 回退。

## 接口

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/` | 单条提交表单页 |
| GET | `/batch/new` `/merge` | 批处理录入 / 主题归并 页面 |
| GET | `/api/topics` `/api/research` | 合法主题 / 研究列表 |
| POST | `/api/resolve_links` | `{raw}` → 解析并抓取其中的链接，返回状态 |
| POST | `/api/extract` | `{raw, extra?}` → 链接抓取 + LLM 抽取为结构化字段 JSON |
| POST | `/api/submit` | 提交 item，追加到当日（或指定日期）日报 |
| POST | `/api/batch/create` | 上传 txt 或 `{text}` → 创建批次（空行分段） |
| GET | `/api/batch/<id>` | 批次状态（条目状态/进度） |
| POST | `/api/batch/<id>/process` | 后台并发处理所有待处理条目 |
| POST | `/api/merge/index` | 全部主题/子主题的三级树 + 频次 |
| POST | `/api/merge/preview` `/api/merge/preview_multi` | 单组 / 多组归并 dry-run |
| POST | `/api/merge/apply` `/api/merge/apply_multi` | 单组 / 多组归并执行 |
| POST | `/api/merge/suggest` | LLM 归并推荐 |
