+++
title = 'JevEvolve'
proposer = '杜晋华'
since = '2026-09-24'
date = 2026-09-24T00:00:00+08:00
draft = false
toc = true
+++

# JevEvolve

> 研究方向：**快决策模型自进化**——以 Jev 为代表的低延迟结构化判断 / 决策模型，及其在智能体中"快决策—慢思考"分工的持续进化。

## 研究范畴

快决策模型（Jev-style fast decision models）不生成开放式文本，而是对有限候选（动作、选项、路由目标）直接返回评分或概率，把单次决策压到百毫秒乃至几十毫秒级、成本压到普通推理调用的百分之一以下。本方向关注这类模型自身及其使用方式的自进化：如何从智能体交互日志中持续校准判断质量、如何自动学习"哪些决策交给快模型、哪些升级到慢思考推理模型"的路由边界、如何在动作选择 / 工具路由 / 上下文压缩 / 风险检查 / 结果评判等高频环节嵌入并迭代。社区关注的核心问题包括：跳过自回归 Decode、直接利用 Prefill 隐状态打分的推理脚手架设计，快决策与实时环境闭环（观察—决策—执行）的时延预算分配，以及"不生成候选外内容"与"判断正确"之间的评估鸿沟。

## 研究挑战

- 评分稳定性与任务泛化：低幻觉表述不等于高准确率，需与强模型评判独立对标。
- 候选集构造是新瓶颈：动作空间的枚举、剪枝与动态生成决定了判断上限。
- 快 / 慢分工的路由边界如何从反馈中自动学习，而非手工规则固化。
- 无开放文本输出导致可解释性与可调试性差，错误决策难以归因。
- 判断模型的持续校准：交互日志噪声大、奖励信号稀疏，易累积系统性偏差。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 本站日报系统，持续追踪快决策模型热点并按本研究方向聚合条目。

## 相关工作

**代码 / 框架**
- [fast-browser-use (APUS-AI-Lab)](https://github.com/APUS-AI-Lab/fast-browser-use) — 基于 Qwen3.5 / Gemma 复现 Jev 快决策工作流：保留 Prefill 隐状态、跳过逐 Token Decode、直接对候选动作算概率，9B 模型单次决策 79ms
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — 用 Jev 做 Claude Code 上下文压缩的低成本方案
- [RouteLLM](https://github.com/lm-sys/RouteLLM) — 学习式模型路由框架，按查询难度在强弱模型间分配

**论文**
- [FrugalGPT: How to Use LLMs While Reducing Cost](https://arxiv.org/abs/2305.05176) — 级联式成本感知调用策略，快慢分工的早期形态
- [RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665) — 偏好数据训练路由器
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — LLM-as-a-Judge 自我改进（被引 996），判断信号自迭代的代表工作

**报道 / 博客**
- [独家｜撬开 Jev 黑箱，对话全球首批复现者：9B 小模型跑通 79 毫秒"快决策"](https://mp.weixin.qq.com/s/IMrdXJooIEBPpbldvmDdIw) — AI前线对 APUS 复现团队的访谈
- [刚刚，Jev 全网解禁！1.2 亿 Token 限时免费用](https://mp.weixin.qq.com/s/i6w4GVq2NV-mL4IzsDRtVw) — TypeSafe AI 开放 Jev：动作判断（Minecraft 中 Astra 规划 + Jev 判断 + 确定性执行）、模型评判（单次 0.44s / $0.00035）等应用形态
