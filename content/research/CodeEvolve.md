+++
title = 'CodeEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# CodeEvolve

> 研究方向：**代码自进化**——以代码为载体的自进化：进化式程序搜索与算法发现、自改进编码 Agent、以及软件工程 Agent 的自训练闭环。

## 研究范畴

代码自进化（code self-evolution）把"代码"同时视为自进化的对象与手段：一方面，LLM 驱动的进化式程序搜索（FunSearch、AlphaEvolve、ShinkaEvolve、OpenEvolve、CodeEvolve）在可自动验证的问题上发现新算法与更优实现；另一方面，编码 Agent 可以修改自身的脚手架与工具（Self-Improving Coding Agent、Darwin Gödel Machine、Live-SWE-agent），形成"写代码的 Agent 改进写代码的 Agent"的递归闭环；再一方面，软件工程 Agent 的训练数据与环境本身也在自动生成与规模化（SWE-smith、SWE-Gym、R2E-Gym、SWE-RL 从开源演化历史学习）。本方向涵盖：自调试与自修复、流程工程（AlphaCodium）、进化式代码优化与算法发现、自改进编码 Agent 的档案与择优策略、可验证奖励下的代码 RL、以及软件工程环境的程序化合成。代码天然具备可执行、可测试、可度量的特点，是自进化闭环最易闭合也最易被作弊的领域，社区关注的核心问题包括：测试用例被"针对性通过"而非真正正确、进化出的代码可读性与可维护性、自修改 Agent 的安全边界，以及从竞赛题到真实仓库级任务的泛化。

## 研究挑战

- 评估作弊：针对测试用例硬编码、绕过验证器而非真正解决问题。
- 进化出的代码可读性、可维护性与安全性难以保证。
- 自修改编码 Agent 的失控与回滚：错误改动破坏自身能力。
- 从算法竞赛 / 函数级任务到仓库级真实软件工程的泛化。
- 进化搜索的算力与采样成本高，样本效率是关键瓶颈。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，代码自进化是自进化机制综述中最易闭环验证的方向。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，自重写 / 自修复编码 Agent 为重点收录对象。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 含代码推理任务族的智能体评测与自进化平台。

## 相关工作

**代码 / 框架**
- [FunSearch](https://github.com/google-deepmind/funsearch) — DeepMind 用 LLM 程序搜索取得数学发现
- [AlphaEvolve results](https://github.com/google-deepmind/alphaevolve_results) — AlphaEvolve 发现的算法与数学结果
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) — AlphaEvolve 开源复现
- [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) — 样本高效的开放式程序进化
- [Darwin Gödel Machine (dgm)](https://github.com/jennyzzt/dgm) — 自修改自身代码的编码 Agent
- [Self-Improving Coding Agent (SICA)](https://github.com/MaximeRobeyns/self_improving_coding_agent) — 编码 Agent 编辑自身代码库以提升性能
- [OpenHands](https://github.com/OpenHands/OpenHands) — 开源软件开发 Agent 平台
- [aider](https://github.com/Aider-AI/aider) — 终端 AI 配对编程工具
- [Agentless](https://github.com/OpenAutoCoder/Agentless) — 无 Agent 的定位-修复-验证流程
- [AlphaCodium](https://github.com/Codium-ai/AlphaCodium) — 从提示工程到流程工程的代码生成
- [SWE-smith](https://github.com/SWE-bench/SWE-smith) — 规模化合成软件工程 Agent 训练数据
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) — 训练软件工程 Agent 与验证器的环境
- [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) — 程序化生成的 SWE 环境与混合验证器
- [SWE-RL](https://github.com/facebookresearch/swe-rl) — 在开源软件演化历史上做 RL

**论文**
- [Evolution through Large Models](https://arxiv.org/abs/2206.08896) — ELM：LLM 作为变异算子的程序进化
- [Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) — FunSearch（Nature 2023）
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)
- [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349)
- [CodeEvolve: an open source evolutionary coding agent for algorithmic discovery and optimization](https://arxiv.org/abs/2510.14150) — 同名开源进化编码 Agent
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954)
- [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) — SICA
- [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646) — 运行中自进化的 SWE Agent
- [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128)
- [Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](https://arxiv.org/abs/2401.08500)
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)
- [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](https://arxiv.org/abs/2502.18449)
- [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/abs/2504.21798)
- [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139)
- [R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents](https://arxiv.org/abs/2504.07164)
