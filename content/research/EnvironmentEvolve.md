+++
title = 'EnvironmentEvolve'
proposer = '杜晋华'
since = '2026-09-24'
date = 2026-09-24T00:00:00+08:00
draft = false
toc = true
+++

# EnvironmentEvolve

> 研究方向：**环境自进化**——智能体训练环境的自动合成、难度进化与智能体—环境协同演化。

## 研究范畴

环境自进化（environment self-evolution / environment engineering）把训练环境本身当作可进化对象：环境 E 由任务生成器、执行载体和验证器组成，是一台可扩展的经验数据生产机器（d = (E, q, τ, v)）。本方向涵盖：训练环境与任务的自动合成（API 池 / 工具图 / 代码化环境）、环境逐组件自纠错、同一策略兼任环境生成器与求解器的协同进化（EvoEnv 类）、存量 benchmark 的插件化改装复用，以及 Environment-as-a-Service 等基础设施形态。社区关注的核心问题包括：环境必须同时满足可执行与可验证这一质量底线、任务难度如何持续对准模型能力边界（自动课程）、环境规模是否存在 scaling law，以及智能体进化与环境进化如何形成稳定的共同进化闭环。

## 研究挑战

- 可执行性与可验证性保障：破坏任一条，环境产出的就不是数据而是噪声。
- 全自动环境生成的质量控制——LLM 直接造环境的可靠性仍不过关，需逐组件自纠错与验证棘轮。
- 难度对准能力边界：自进化可行的关键是模型能为"自己解不出的题"写出可靠验证代码。
- 验证器被钻空子（reward hacking）：奖励作弊会随环境规模放大。
- 环境池与策略协同进化的非平稳性、多样性坍缩与成本膨胀。
- 合成环境与真实任务分布的对齐（sim-to-real gap）。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 元数据驱动的可验证任务合成平台（Sudoku/迷宫/Knights&Knaves/Zebra/代码推理等），任务生成器＋验证器的可编程环境雏形。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

## 相关工作

**代码 / 框架**
- [AgentGym](https://github.com/WooooDyy/AgentGym) — 跨多样环境进化 LLM 智能体的框架与环境套件
- [meta-agents-research-environments](https://github.com/facebookresearch/meta-agents-research-environments) — Meta 智能体研究环境平台
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 阿里 ModelScope 自进化 Agent 系统，含任务/环境自主构造
- [R-Zero](https://github.com/Chengsong-Huang/R-Zero) — 零数据自进化：同一模型兼任出题者与求解者
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 含环境进化专题的自进化 Agent 合集

**论文**
- [EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents](https://arxiv.org/abs/2403.12014) — LLM 按智能体弱项动态生成训练环境
- [OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://arxiv.org/abs/2405.15568) — 代码化环境的开放式生成
- [Eurekaverse: Environment Curriculum Generation via LLM](https://arxiv.org/abs/2411.01775) — LLM 环境课程生成
- [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) — 神经路线的可交互生成环境（世界模型）
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) — 自博弈出题—求解闭环，任务分布随能力进化
- [CogEvol：迈向高效可靠的学习环境生成](https://huggingface.co/papers/2608.30968) — 交互式学习环境单次生成 + GRPO 训练，修复"视觉逼真但不可玩"的奖励作弊

**综述 / 报道**
- [Agentic Environment Engineering：智能体环境工程综述](https://mp.weixin.qq.com/s/FAqFpQw6MZoM9iph9Fu_4w) — 以环境生命周期为主线，提出智能体—环境共同进化闭环与 Environment-as-a-Service
- [从手工构建到自进化：Agent 环境扩展五篇论文（RLVE / AgentScaler / AWM / EvoEnv / EnvHarness）](https://mp.weixin.qq.com/s/zEge9AxeQXJFxjmYOD74FA) — 统一形式化框架下的环境扩展演进线：人工构建 → 自动合成 → 自纠错生成 → 协同进化 → 存量改装
