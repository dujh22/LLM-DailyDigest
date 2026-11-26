# 新增研究项目操作指南

> 本文沉淀「在 `content/research/` 新增一个研究项目」需要动哪些部分。
> 结论先行：**只需新建 1 个 md 文件 + 更新 2 个 README 的项目列表**，后端与网站其余部分全部自动生效。

## 一、必做步骤

### 1. 新建研究文件 `content/research/<项目名>.md`

**文件名（不含 .md）即研究项目名**，后续所有引用（日报 items 的 `research` 字段、后端标注、LLM 判定）都以它为准，区分大小写。

必须遵循以下结构（可参考 `DataEvolve.md`）：

```markdown
+++
title = '<项目名>'
proposer = '杜晋华'
since = 'YYYY-MM-DD'          # 最早研究时间，展示在研究页页头
date = YYYY-MM-DDT00:00:00+08:00
draft = false                 # 必须 false，否则 Hugo 不渲染
toc = true
+++

# <项目名>

> 研究方向：**<一句话方向>**——<补充说明>。

## 研究范畴

<一段描述，建议 200~400 字>

## 研究挑战
...

## 自研项目
...

## 自研洞察

<!-- human-only:start 自研洞察｜…（标记原文见 backend/research_sections.py） -->
*（待人工补充）*
<!-- human-only:end 自研洞察 -->

## 自研经验

<!-- human-only:start 自研经验｜… -->
*（待人工补充）*
<!-- human-only:end 自研经验 -->

## 研究经验

<!-- research-experience:start｜… -->
*（暂无，随日报自动积累）*
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
...

**论文**
...
```

> 三个新栏目不必手写：首次整备时后端会自动补齐（`research_sections.ensure_sections`，只新增空栏目、不改已有内容），也可手动运行
> `cd backend && ./venv/bin/python -c 'import app, research_sections as rs; [app.write_research_page(n, rs.ensure_sections) for n in app.valid_research()]'`。

其中以下几处是**机器可读约定**，格式不能改：

| 位置 | 消费方 | 说明 |
|---|---|---|
| `> 研究方向：...` 行 | `backend/recommend.py` 的 `build_research_profile()` | 正则 `^>\s*研究方向[：:]` 提取，作为推荐系统 LLM 判定的研究画像 |
| `## 研究范畴` 小节 | 同上 | 提取该小节前 400 字作为画像补充；缺失则画像只剩一句方向，推荐召回质量下降 |
| `## 自研洞察` / `## 自研经验` 整个小节（标题到下一个 `##`） | 后端写盘守卫 + `.claude/hooks/guard_research_human.py` | **人类专属**：只允许人类手动修改。后端改研究页前后逐字比对，被改动即拒写；Claude Code 中 AI 的编辑若会改动它们，hook 强制弹窗询问人类 |
| `## 研究经验` 的 `research-experience` 标记对 | `backend/app.py` → `refresh_research_experiences()` | 随日报整备自动增量更新（见下文），标记对之间整块替换 |

### 2. 更新两处 README 的研究项目列表（手动）

- `README.md` — "Current research projects" 一行
- `README_ZN.md` — "当前研究项目" 一行

这是**唯一硬编码研究名单的地方**，代码里没有。

## 二、自动生效的部分（无需改代码）

后端和网站对研究项目的发现都是**按文件名动态扫描** `content/research/*.md`，新增文件后：

| 模块 | 位置 | 行为 |
|---|---|---|
| 标注后台合法集合 | `backend/app.py` → `valid_research()` | 每次调用实时 glob，**无需重启服务** |
| 标注页复选框 | `backend/app.py` 首页路由 + `templates/index.html` | 渲染时读 `valid_research()`，刷新页面即出现新项目 |
| API | `GET /api/research` | 同上 |
| LLM 自动标注 | `backend/app.py` 结构化 prompt | 新研究名自动进入候选列表；保存时按合法集合过滤 |
| 推荐系统 | `backend/recommend.py` → `build_research_profile()` | 读「研究方向 + 研究范畴」构建画像做相关性判定 |
| 历史迁移脚本 | `backend/migrate_topic.py` | 复用 `app.valid_research()` |
| 网站研究列表页 | Hugo `/research/`（菜单见 `hugo.toml`） | 自动收录新页面 |
| 网站研究详情页 | `layouts/research/single.html` | 渲染正文 + 页头 `proposer`/`since`，并自动聚合所有 `content/updates/*.md` 中 items 的 `research` 数组命中本项目名的条目为「相关工作」 |

## 三、研究经验栏目（自动维护）

- **内容**：经验列表，每条是面向整个研究社区的具体洞察或方法论，下挂支撑它的具体工作（链接到日报条目锚点，按日期倒序）。格式：
  `1. **经验标题**：经验正文` + 子项 `   - [工作标题](../../updates/<日期>/#<条目id>) · <日期>`。
- **自动更新**：每次当日整备（`/api/finalize`，见 `backend/README.md`）最后一步，按研究项目取当日打了该研究标签的新条目，交给 LLM 增量合并——修订已有经验、把新工作挂到已有经验、或新增经验；不会删除已有经验或已挂工作。每个研究上限 `EXPERIENCE_MAX`（默认 15）条。被去重删除的条目链接会自动清理。
- **可人工修订**：直接改标记对之间的列表即可，下次自动更新以当前内容为基础继续合并。
- **回填历史**：`cd backend && ./venv/bin/python backfill_research_experience.py --days 30 [研究名...]`（或 `--all`；默认不部署，加 `--deploy` 同步提交推送）。可重复执行，已判定条目自动跳过。

## 四、注意事项

1. **不要在 `content/research/` 放非研究项目的 md 文件**（如 README、草稿）——任何 `*.md` 都会被 `valid_research()` 当成研究项目，进入 LLM prompt 和标注复选框，同时被 Hugo 渲染成研究页。本指南因此放在仓库根目录。
2. 日报 items 中 `research` 的取值必须与文件名 stem **完全一致**（含大小写），不一致会在保存 / 部署校验时被过滤掉。
3. 研究页的「相关工作」是自动聚合的，新研究刚建立时为空属正常，等后续日报条目打上该研究标签后自动出现。
4. 网站需要重新构建（Hugo）才会出现新页面；后端标注服务不需要重启。

## 五、验证

```bash
# 1. 后端能发现新研究（含推荐画像提取是否成功）
cd backend && python -c "
import app, recommend
print(app.valid_research())
print([p for p in recommend.build_research_profile() if not p['direction'] or not p['scope']] or '画像提取全部 OK')
"

# 2. 本地预览网站
hugo server --baseURL http://localhost:1313/ -D   # 访问 /research/
```
