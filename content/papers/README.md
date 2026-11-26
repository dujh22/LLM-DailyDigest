# 相关工作复现注册规范

> 目标：**一次复现，终身复用**。每个尝试复现的相关工作都在这里注册，网站「论文」页按研究展示进度、已完成项与下一步。
> 本文件不会渲染到网站（`hugo.toml` 的 `module.mounts` excludeFiles）。

## 一、目录树

```
content/papers/
├── _index.md                     # 栏目首页；active_research 决定根页展示哪些在研研究及顺序
├── <研究>/                       # 第一层：content/research/ 下的文件名（区分大小写）
│   ├── _index.md
│   └── <data|method|eval|other>/ # 第二层：数据 / 方法 / 评测 / 其他
│       ├── _index.md
│       └── <短语>/               # 第三层：具体工作的指代短语（小写 + 连字符，如 self-rewarding-lm）
│           ├── index.md          # 整体笔记（front matter 驱动进度）
│           ├── paper/            # 论文中英文：en.pdf、zh.pdf（文件名以 en / zh 结尾即可，如 2605.23872_zh.pdf）
│           ├── resources/        # 可复用资源：数据 / 模型索引、官方代码、下载脚本
│           ├── repro/            # 个人复现过程中新增的东西：代码、配置、环境锁定、结果、日志
│           └── cache/            # 即用即下的数据 / 模型（git 与 Hugo 均忽略，可随时删）
└── *.md                          # 历史的单篇论文笔记（非复现），照常作为「论文笔记」列出
```

当前在研：EvolveLLM、Awesome-RSI、LogicEvolve、EvolveLRM、EvalEvolve、DataEvolve、Groom、HarnessEvolve、SwarmEvolve、CVTransformer、JevEvolve（改 `_index.md` 的 `active_research` 即可增删）。

一个工作只注册一次，放在**最初引入它的研究**下；其他研究复用时登记到 `reused_by`，不要复制目录。

## 二、注册

```bash
python3 tools/repro.py new EvolveLLM method self-rewarding-lm \
  --title 'Self-Rewarding Language Models' \
  --paper https://arxiv.org/abs/2401.10020 --code https://github.com/xxx/yyy
python3 tools/repro.py check   # 校验结构与 reused_by，打印全部进度
```

脚本会补齐上两层的 `_index.md`、建好四个子目录（含 `.gitkeep`），并生成笔记模板 `index.md`。

## 三、各文件夹约定

| 位置 | 放什么 | 不放什么 |
|---|---|---|
| `paper/` | 英文原文 `en.pdf`、中文译文 `zh.pdf`（也可放 `.tex`/`.md` 版）。太大或不便入库时，在 front matter 填 `paper_en` / `paper_zh` 外链 | — |
| `resources/` | `README.md` 资源索引（数据 / 模型的来源、版本、许可、大小）、`download.sh`（下载到 `../cache/`）、官方代码（小则直接放，大则记录仓库 + commit 或用 git submodule） | 原始大数据、模型权重 |
| `repro/` | 自己新增的代码 / 配置 / prompt、环境锁定（`requirements.txt`、`environment.yml`）、结果表与日志。在原数据上做了后处理的，**只留处理代码**，产物可重算 | 可由代码重算的大产物 |
| `cache/` | 运行时下载的数据与模型 | 任何需要长期保存的东西 |
| `index.md` | 整体笔记：论文要点、可复用资源表、复现记录（环境 / 命令 / 论文 vs 复现结果对照 / 踩坑）、二次利用、进展日志 | — |

### 入库与网站展示

- **GitHub**：`paper/`、`resources/`、`repro/` 全部正常入库（PDF、代码、数据 / 模型索引都会上传）；只有 `cache/` 被 `.gitignore` 忽略。单文件超过 100 MB 时 GitHub 会拒收，这类文件放外链或下载脚本。
- **网站工作页**：进度卡下方按 `paper/`、`resources/`、`repro/` 分组列出全部文件：
  - 点 **PDF** → 站内直接在浏览器打开（构建时只发布 PDF，`publishResources = false` 保证代码等不被复制到站点）；旁边的 GitHub 图标跳仓库原文件；
  - 点 **代码 / md / 配置等** → 跳 GitHub 查看（带语法高亮、md 渲染）；
  - `resources/README.md`（资源索引）直接渲染在列表下方，不用点开；
  - 每个分组标题旁的 GitHub 图标跳对应目录。

## 四、进度口径

由网站构建时自动计算（`layouts/partials/papers/progress.html`，`tools/repro.py check` 同口径）。里程碑**依次累计**，前一档没达成，后面的不计：

| 进度 | 条件 |
|---|---|
| 0% | 已注册，什么都没干 |
| 20% | `paper/` 中英文论文齐全（或 `paper_en` / `paper_zh` 外链） |
| 40% | `resources/` 已整理（至少有一个非占位文件，如资源索引 `README.md`；没有公开代码 / 数据也要写明「无」） |
| 60% | `repro/` 有个人复现新增内容 |
| 80% | front matter `reused_by` 记录了被哪些 `content/research` 研究二次利用 |
| 100% | 已达 80%，且 `index.md` 超过 365 天无变化（git 最后修改时间） |

工作页显示进度条、每档是否完成和「下一步」。因为「无变化」只看 `index.md`，**每次推进都在笔记「进展日志」追加一行**，否则在 `repro/` 里的改动不会刷新计时。

## 五、与 SOP 的对应

《【核心】如何做研究写论文》§3「复现相关工作」：

1. 注册：`tools/repro.py new …`
2. AI 阅读原文、整理关键信息 → `index.md`「论文要点」
3. 下载英文论文、翻译成中文并归档 → `paper/`（20%）
4. 整理资源 → `resources/`（40%）；尝试复现 → `repro/` + 「复现记录」（60%）
5. 被研究用到时登记 `reused_by` + 「二次利用」（80%）
