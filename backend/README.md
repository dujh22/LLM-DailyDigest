# 提交工具后端（本地）

交互式填写单条消息，追加到当日日报；支持 LLM 从原始文本自动抽取结构化字段。另含**批处理录入**、**当日推荐采集**、**主题/子主题归并**与**条目去重归并**四个辅助页面。

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
- 「⚡ 一键自动处理并提交」：跳过人工核对——待处理条目先自动抽取，随后全部「待核对」条目直接按抽取结果提交（`notes` 逐字保留原文、候选新主题默认并入），适合信任抽取质量的整批快速录入。「待介入」条目不会被自动提交；自动提交失败的条目保持「待核对」并显示原因。

### 当日推荐 `/recommend`

自动采集**最近 24 小时**内与你研究相关的内容，LLM 判定相关性后勾选导入批处理，形成「推荐 → 抽取 → 提交」的完整链路。

**采集通道（公众号三级 + arXiv，按标题自动去重、高层级优先）：**

| 优先级 | 通道 | 覆盖 | 时效 | 前置条件 |
| --- | --- | --- | --- | --- |
| 1（可选） | 微信公众平台 appmsg 接口 | 量子位 / 机器之心 / 新智元 | 实时 | 手动维护 cookie+token，限流风险高 |
| 2 | 量子位官网 qbitai.com | 量子位 | 实时 | 无 |
| 3 | [Wechat-Scholar](https://github.com/osnsyc/Wechat-Scholar) 学术公众号 RSS | 三号全（可扩展） | ≤12h | 无 |
| — | arXiv Atom API（cs.CL/cs.AI/cs.LG） | 论文 | 实时 | 无 |

- **默认零配置可用**（官网 + RSS + arXiv）。appmsg 为可选实时增强：`/recommend` 页粘贴 mp.weixin.qq.com 的 Cookie + token（F12 找 appmsg 请求），保存时自动测试；微信限流（ret 200013，`freq control`）时自动静默回落到默认通道，只有某公众号所有通道都取不到时才报警。
- 相关性判定：解析 `content/research/*.md` 各项目的「研究方向 + 研究范畴」构建画像，候选（标题+摘要）分 chunk 并发送 LLM 打分（`FILTER_CHUNK=40`、`FILTER_WORKERS=8`），返回 相关/不相关 + 匹配的研究项目 + 一句理由；单 chunk 失败降级为「未判定」，不影响整批。
- arXiv 严格 24h 窗口为空时自动放宽到 48h/72h（arXiv 按公告批次入库，刚公告论文的 submittedDate 常在 1~2 天前），页面会注明实际窗口。
- 结果按日缓存到 `.recommend_cache/recommend-<date>.json`（gitignored），同一天重开页面不重复采集；「强制重新采集」忽略缓存。
- 「📦 导入所选到批次」：勾选条目生成批处理会话（raw = 标题 + 链接 + 摘要，链接独立成行便于批处理阶段重新抓取），跳转批次总览页走既有流程；勾选状态存 localStorage，刷新不丢。
- 增删 RSS 公众号：改 `backend/recommend.py` 的 `WECHAT_SCHOLAR_FEEDS` 字典（feed 地址见 Wechat-Scholar 仓库 `channels.json`）。

### 主题 / 子主题归并 `/merge`

随着标签增长，近义/重复标签（如「推理评估 / 推理评测」）需要归并：

- 左侧三级树「主题 ▸ 子主题 ▸ 文章」，勾选若干主题或子主题，右侧填目标名 → **🔍 预览**（显示影响条目/文件数、待删/保留主题页）→ **✓ 执行**。
- **子主题按字符串全局归并**；空样板源主题页自动删除，有自定义内容的保留并提示。
- 「🤖 LLM 归并推荐」自动聚类近义标签，可单条「采纳」或勾选多条「⚡ 批量采纳并执行」。
- 改写采用**原位替换**，未变化的 item 逐字保留，diff 最小；全程可 `git checkout -- content/updates/` 回退。

### 条目去重归并 `/dedup`

条目可能当日内部重复，也可能与过去若干天跨文件重复（同一工作被多个来源/多天反复报道）。本页以 **URL 判重**做条目级归并：

- **判重规则**：`paper` / `code` / `dataset` / `link` 四个字段任一非空值**规范化后相同**即视为同一内容。规范化 = 小写域名、去默认端口与尾 `/`、剥 `utm_*` / `spm` / `ref` 等跟踪参数、丢 fragment、arXiv `abs`/`pdf`/`html` + 版本号统一为 `abs/<id>`（`https://arxiv.org/pdf/2401.12345v2` ≡ `http://arxiv.org/abs/2401.12345`）。无任何 URL 的条目永不参与判重。
- **归并语义（吸收合并）**：每组保留**最早出现**条目（最早文件日期，同文件则最早位置）并吸收后续重复条目的字段——标量字段（title/subtopic/source/四个 URL）空则补；`topics`/`research` 并集保序；summary/content/purpose 取更完整一方；`notes` 原始笔记差异以 `[合并自 日期 id]` 标记追加、**永不丢弃**。其余重复条目删除。
- **两步操作**：填扫描窗口天数（默认 7，可 14/30…90）→ **🔍 扫描重复**预览分组（共享 URL、保留/删除条目、字段吸收 diff）→ 勾选若干组「⚡ 执行选中」或「✓ 全部执行」（也可单组执行）。执行后自动重扫刷新。
- **🤖 LLM 合并解析字段**（可选）：执行时勾选后，每组的 `summary`/`content`/`purpose` 交由 LLM 以保留条目为基础整合为一份连贯内容（替代规则拼接，不带 `[合并自]` 标记）；`notes`/`title` 等仍走规则（原始笔记逐字保留）。单组 LLM 失败自动回退规则合并并计数提示；LLM 调用在锁外并发执行（8 并发），不阻塞提交。
- **提交时自动查重**：每次 `/api/submit`（含批处理一键提交）在写入前自动检查新条目与**目标日期向前 7 天至今天**窗口内已有条目是否同链接，命中则**硬阻断**并显示重复对象（日期/文件/id/标题/匹配链接）；确要保留可勾选「允许重复提交」或在报错上一键「仍要提交」放行。
- 改写同样为**原位替换**（变化块重写、删除块移除、未变化块逐字保留），可 `git checkout` 回退；执行时锁内重新扫描校验，预览后被并发修改的组自动跳过。

## 接口

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/` | 单条提交表单页 |
| GET | `/batch/new` `/recommend` `/merge` `/dedup` | 批处理录入 / 当日推荐 / 主题归并 / 条目去重 页面 |
| GET | `/api/topics` `/api/research` | 合法主题 / 研究列表 |
| POST | `/api/resolve_links` | `{raw}` → 解析并抓取其中的链接，返回状态 |
| POST | `/api/extract` | `{raw, extra?}` → 链接抓取 + LLM 抽取为结构化字段 JSON |
| POST | `/api/submit` | 提交 item，追加到当日（或指定日期）日报；写入前自动查重（近 7 天同链接硬阻断，`{allow_dup:1}` 放行） |
| POST | `/api/batch/create` | 上传 txt 或 `{text}` → 创建批次（空行分段） |
| GET | `/api/batch/<id>` | 批次状态（条目状态/进度） |
| POST | `/api/batch/<id>/process` | 后台并发处理所有待处理条目 |
| POST | `/api/batch/<id>/process_one` | `{idx}` 同步重跑单条（重新处理/链接修复后） |
| POST | `/api/batch/<id>/auto_submit` | 一键自动处理：抽取后跳过核对直接提交全部待核对条目 |
| POST | `/api/batch/mark` | 标记某条目已提交（单条页提交成功后回调） |
| GET | `/api/recommend/status` | 采集运行状态 + 当日缓存候选列表 |
| POST | `/api/recommend/collect` | `{force}` 启动一次采集（后台异步） |
| GET/POST | `/api/recommend/credentials` | appmsg 凭据状态 / 保存并测试（不回显 cookie） |
| POST | `/api/recommend/to_batch` | `{keys}` 把选中候选生成为批处理会话 |
| POST | `/api/merge/index` | 全部主题/子主题的三级树 + 频次 |
| POST | `/api/merge/preview` `/api/merge/preview_multi` | 单组 / 多组归并 dry-run |
| POST | `/api/merge/apply` `/api/merge/apply_multi` | 单组 / 多组归并执行 |
| POST | `/api/merge/suggest` | LLM 归并推荐 |
| POST | `/api/dedup/preview` | `{days}` → 扫描窗口内重复条目组（纯读：分组/保留者/吸收 diff） |
| POST | `/api/dedup/apply` | `{days, groups?: [{file,id}], llm?}` → 执行去重归并；`groups` 仅执行选中组，`llm` 用 LLM 合并解析字段 |
