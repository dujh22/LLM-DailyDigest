+++
title = 'LogicEvolve'
proposer = '杜晋华'
since = '2025-05-06'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# LogicEvolve

> 研究方向：大型语言模型的**逻辑推理能力自我进化**——让模型在逻辑 / 多步推理上持续自我改进。

## 研究范畴

大型语言模型的**逻辑推理能力自我进化**，关注让模型在形式逻辑、多步 / 组合推理上持续自我改进。本方向涵盖：神经符号（neuro-symbolic）推理、逻辑推理基准、自我验证 / 自我校正，以及 System 1 → System 2 的能力跃迁。社区关注的核心问题包括：推理过程的逻辑忠实度（faithfulness）与可验证性、组合泛化与分布外泛化及推理鲁棒性、符号求解器 / 验证器如何与神经网络互补，以及自我进化是否会放大逻辑错误（幻觉沿推理链传播）。

## 研究挑战

- 逻辑正确性的自动验证困难、ground truth 成本高。
- 基准污染与"模式匹配"伪推理。
- 符号化方法的可扩展性与工程复杂度。
- 评测有效性：区分真实推理与记忆。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理的智能体评测与自进化平台，统一演绎/归纳、多跳、符号、程序与博弈逻辑，支持 CLUB/CLUBv2/ToolCLUB/ExCLUB/BBH/SynLogic/LogiQA2 等多基准，覆盖数据合成、评测、训练（LLaMA-Factory/verl）与可视化榜单全链路。
- [clubWeb](https://github.com/anonymous1Coder/clubWeb) — LogicEvolve/CLUB 的可视化榜单前端（React + TypeScript + Vite），即 clubweb.site。

## 相关工作

**代码 / 框架**
- [Logic-LLM](https://github.com/teacherpeterpan/Logic-LLM) — 用符号化求解器增强 LLM 逻辑推理
- [mem-kk-logic](https://github.com/AlphaPav/mem-kk-logic) — LLM 逻辑推理中的记忆研究（本站已 fork）
- [SE-Agent](https://github.com/JARVIS-Xs/SE-Agent) — LLM 代码智能体自进化框架
- [Reasoning-Self-Evolution-Survey](https://github.com/cs-holder/Reasoning-Self-Evolution-Survey) — 配套复杂推理自进化综述的资源仓库
- [self-improvement-llm (Zesearch)](https://github.com/Zesearch/self-improvement-llm) — 系统级自我改进语言模型技术整理
- [Awesome-Agentic-Reasoning](https://github.com/weitianxin/Awesome-Agentic-Reasoning) — Agent 推理论文（含自我进化专题）
- [Awesome-LLM-Reasoning-with-NeSy (LAMDA)](https://github.com/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy) — 神经符号学习提升 LLM 推理合集
- [LogicBench](https://github.com/Mihir3009/LogicBench) — 25 种推理模式的逻辑推理基准数据集
- [Neuro-Symbolic Large Models](https://llm-symbol.github.io/) — 符号引导 LLM 推理资源页

**论文**
- [LogicVista: Multimodal LLM Logical Reasoning Benchmark](https://arxiv.org/abs/2407.04973)
- [Making Large Language Models Better Reasoners with Alignment](https://arxiv.org/abs/2309.02144)
- [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) — 零数据自进化推理（被引 157）
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — LLM 自我进化综述
- [Debate, Train, Evolve (DTE) (EMNLP 2025)](https://arxiv.org/abs/2505.15734) — 多 Agent 辩论训练推理自进化（被引 21）
- [STaR: Bootstrapping Reasoning With Self-Taught Reasoning](https://arxiv.org/abs/2203.14465) — 经典自我推理引导（被引 1959）
- [START: Self-taught Reasoner with Tools](https://arxiv.org/abs/2503.04625) — STaR 工具增强版（被引 51）
- [ReVISE (ICML 2025)](https://arxiv.org/abs/2502.14565) — 测试时自我验证推理细化
- [On the Generalization Gap in Self-Evolving Language Models](https://arxiv.org/abs/2606.01075) — 自进化 LLM 泛化差距
- [LogicGraph: Benchmarking Multi-Path Logical Reasoning](https://arxiv.org/abs/2602.21044) — 神经符号评估器多路径逻辑基准
- [FOLIO (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.1229) — 一阶逻辑推理数据集（被引 398）
- [P-FOLIO](https://arxiv.org/abs/2410.09207) — 前提化一阶逻辑推理评估
- [GSM-Symbolic (Apple)](https://machinelearning.apple.com/research/gsm-symbolic) — 符号化数学推理揭示 LLM 脆弱性
- [ALIVE: Adversarial Self-Evolution](https://arxiv.org/abs/2602.05472) — 对抗性自我进化激活推理
- [A Survey of Reasoning LLMs](https://arxiv.org/abs/2502.17419) — System 1→2 视角推理综述（被引 415）
- [Towards Large Reasoning Models: Reinforced Self-Training Survey](https://arxiv.org/abs/2501.09686) — 强化自我训练综述
- [CRESCENT (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.337.pdf) — 零监督推理自举（被引 11）
- [ReST-MCTS\* (NeurIPS 2024)](https://neurips.cc/virtual/2024/poster/96343) — 过程奖励引导树搜索强化自训练
- [RL-STaR: Theoretical Analysis of RL in Self-Taught Reasoner](https://arxiv.org/abs/2410.23912) — STaR 的 RL 理论分析
- [CARE-STaR (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.1116.pdf) — 约束感知自我推理
- [Entropy-Aware Self-Evolution Framework](https://openreview.net/pdf?id=nXENWUSRMw) — 熵感知自进化
- [Mixture-of-Thought (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/file/af80ce1011eb35fe1023c320158c2ad9-Paper-Conference.pdf) — 混合思维提升推理泛化（被引 24）
