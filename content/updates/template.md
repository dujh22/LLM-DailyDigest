+++
title = '[模版] 2026-XX-XX 科研追新'
date = 2026-08-07T09:00:00+08:00
draft = true
toc = true
+++

> 本页是日报模板示例（`draft = true`，不发布）。**一个日报文件 = 当日多条 item**，item 作为 `[[items]]` 写在 front matter 里（单一数据源），日报页自动渲染，主题页按子主题自动聚合。

## 字段说明（每个 `[[items]]` 条目）

| 字段 | 说明 | 必填 |
| --- | --- | --- |
| `id` | 条目锚点（英文短横线），用于主题页深链回日报 | ✅ |
| `title` | 标题（日报页渲染为 H2） | ✅ |
| `subtopic` | **子主题**，决定在主题页里归入哪个栏目 | ✅ |
| `topics` | 所属主题数组，须与 `content/topic/` 文件名一致（如 `推理`、`智能体`） | ✅ |
| `source` | 来源（公众号 / arxiv 分类 / 站点） | ✅ |
| `summary` | 一句话摘要 | ✅ |
| `paper` / `code` / `dataset` / `link` | 论文 / 代码 / 数据集 / 原文链接，留空不显示 | 按需 |
| `content` | 正文（TOML 三引号多行，支持 Markdown） | 按需 |
| `purpose` | 用途与启示（多行 Markdown） | 按需 |

> `topics` 决定**出现在哪些主题页**；`subtopic` 决定**在主题页的哪个栏目（分组）**。

## 示例：当日两条消息（不同子主题）

（以下内容仅作 front matter 示例，复制时把整段连同 `[[items]]` 放进 `+++` 区块内）

    [[items]]
    id = 'hop-skip-overthink'
    title = 'Hop, Skip, and Overthink：诊断推理模型多跳失误'
    subtopic = '多跳问答'
    topics = ['推理']
    source = 'arxiv cs.CL'
    summary = '从跳跃、覆盖、过度思考三维度刻画推理模型失败模式。'
    paper = 'https://arxiv.org/abs/2508.04699'
    code = ''
    dataset = ''
    link = ''
    content = '''
    本研究系统探讨了语言模型在多跳问答中的推理失败，提出错误分类框架。
    '''
    purpose = '''
    - 为评估推理模型提供超越准确率的诊断维度
    '''

    [[items]]
    id = 'mmgrpo'
    title = 'Multi-module GRPO：组合策略梯度与提示优化'
    subtopic = '强化学习对齐'
    topics = ['强化学习', '训练']
    source = 'arxiv cs.CL'
    summary = 'mmGRPO 按模块分组 LM 调用，结合自动提示优化平均提升 11%。'
    paper = 'https://arxiv.org/abs/2508.04660'
    content = '''
    GRPO 的多模块推广，处理可变长度与中断轨迹。
    '''

## 用法

1. `hugo new updates/2026-08-08.md`（自动套用 `archetypes/updates.md`）
2. 在 `+++` 内填 `[[items]]` 条目
3. 保存 → 日报页渲染条目；对应主题页底部按子主题聚合出现

## 验证

到 `content/topic/` 对应主题页底部确认「相关消息（按子主题自动聚合）」按子主题分栏列出。
