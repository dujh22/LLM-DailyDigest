+++
title = 'PromptEvolve'
proposer = '杜晋华'
since = '2026-10-08'
date = 2026-10-08T00:00:00+08:00
draft = false
toc = true
+++

# PromptEvolve

> 研究方向：**提示自进化**——系统提示 / 指令 / 示例 / 多阶段 LM 程序的自动优化与持续进化，以及智能体从执行反馈中自我改写提示的闭环。

## 研究范畴

提示自进化（prompt self-evolution / automatic prompt optimization）把提示词视为可搜索、可学习、可版本化的"软参数"：在冻结模型权重的前提下，由模型自身或外层优化器依据任务反馈持续改写系统提示、指令措辞、推理模板、few-shot 示例乃至多阶段 LM 程序的全部提示集合。本方向涵盖：基于进化算法 / 束搜索的离散提示搜索（Promptbreeder、EvoPrompt、ProTeGi 类）、LLM-as-Optimizer 的元提示优化（OPRO、APE）、面向多阶段程序的编译式优化（DSPy / MIPRO）、以自然语言反馈为"梯度"的反思式进化（TextGrad、GEPA）、智能体在运行时把失败经验沉淀为提示 / 技能 / 记忆的自我改写（Reflexion、Voyager 类），以及提示与模型权重协同进化（提示优化 vs. 强化微调的样本效率对比）。社区关注的核心问题包括：提示优化是否能以远低于 RL 的 rollout 成本逼近甚至超过权重训练、自动演化的提示能否跨模型 / 跨任务迁移、如何在开发集上避免过拟合与"评测钻空子"、多阶段程序中各节点提示的信用分配，以及自演化提示的可审计性与安全边界。

## 研究挑战

- 评估成本与过拟合：每轮候选都需跑完整评测，开发集小则易过拟合，评测指标本身也可能被提示"钻空子"。
- 跨模型迁移脆弱：针对某一模型演化出的提示换模型后收益常大幅衰减，提示与模型的耦合难以解耦。
- 多阶段程序的信用分配：Agent 流水线包含多个提示节点，终局反馈难以归因到具体节点与措辞。
- 搜索空间无界且不连续：自然语言提示缺乏平滑的优化几何，变异 / 交叉算子的设计高度依赖经验。
- 提示 vs. 权重的边界：何时该演化提示、何时该更新权重，二者协同的理论与工程框架尚缺。
- 可审计性与安全漂移：自动改写的系统提示可能引入越权指令、泄露约束或削弱安全护栏，需版本化与门禁。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 本站日报系统，推荐判定 / 自动标注 / 概览生成均由提示驱动，可作为提示迭代与回归评测的实验场。

## 相关工作

**代码 / 框架**
- [DSPy](https://github.com/stanfordnlp/dspy) — 斯坦福声明式 LM 编程框架，内置 MIPROv2 / BootstrapFewShot 等提示与示例优化器
- [GEPA](https://github.com/gepa-ai/gepa) — 反思式提示进化：用自然语言反思 + 帕累托前沿采样演化多节点提示
- [TextGrad](https://github.com/zou-group/textgrad) — 以 LLM 文本反馈为"梯度"自动微分提示、代码与答案
- [OPRO](https://github.com/google-deepmind/opro) — DeepMind "LLM 即优化器"，在元提示中迭代生成更优指令
- [EvoPrompt](https://github.com/beeevita/EvoPrompt) — 遗传算法 / 差分进化与 LLM 结合的离散提示进化
- [automatic_prompt_engineer (APE)](https://github.com/keirp/automatic_prompt_engineer) — 自动指令生成与选择的早期代表实现
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 含提示 / 工作流进化专题的自进化 Agent 合集

**论文**
- [Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution](https://arxiv.org/abs/2309.16797) — DeepMind 自指式进化：任务提示与变异提示同时进化
- [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers (EvoPrompt)](https://arxiv.org/abs/2309.08532) — LLM 充当进化算子的离散提示优化
- [Large Language Models as Optimizers (OPRO)](https://arxiv.org/abs/2309.03409) — 以自然语言描述优化问题、LLM 迭代生成解
- [Large Language Models Are Human-Level Prompt Engineers (APE)](https://arxiv.org/abs/2211.01910) — 自动指令生成 + 评分选择
- [Automatic Prompt Optimization with "Gradient Descent" and Beam Search (ProTeGi)](https://arxiv.org/abs/2305.03495) — 文本"梯度"+ 束搜索的提示编辑
- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) — 把提示工程编译为可优化的 LM 程序
- [Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs (MIPROv2)](https://arxiv.org/abs/2406.11695) — 多阶段程序的指令与示例联合优化
- [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) — 文本反馈反向传播的通用优化框架
- [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) — 以极少 rollout 的反思式提示进化超越 GRPO
- [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://arxiv.org/abs/2310.16427) — MCTS 规划式提示优化
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — 把失败反思写回提示上下文的运行时自进化
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — 技能库作为可增长的提示 / 代码资产
- [Are Large Language Models Good Prompt Optimizers?](https://arxiv.org/abs/2402.02101) — 对 LLM 反思式提示优化有效性边界的审视
- [A Systematic Survey of Automatic Prompt Optimization Techniques](https://arxiv.org/abs/2502.16923) — 自动提示优化方法综述
