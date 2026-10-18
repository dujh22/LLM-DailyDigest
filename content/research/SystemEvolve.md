+++
title = 'SystemEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# SystemEvolve

> 研究方向：**AI 系统级自进化**——不止改模型权重，而是让 Agent 系统的架构、工作流、工具链与自身代码成为被进化的对象。

## 研究范畴

系统级自进化（system-level self-evolution）把优化对象从单个模型扩展到整个 AI 系统：Agent 的编排结构、工作流图、提示与工具配置、运行时 harness，乃至系统自身的源代码，都可以由系统自己提出修改、实验验证并择优保留，形成达尔文-哥德尔机式的开放式演化。本方向涵盖：自动化 Agent 系统设计（ADAS / AFlow 类元搜索）、以文本或执行轨迹为"梯度"的生成式优化（TextGrad / Trace / DSPy）、自指式递归自改进框架（Gödel Agent、Darwin Gödel Machine）、程序进化型发现系统（AlphaEvolve / ShinkaEvolve / OpenEvolve），以及系统演化的档案管理、分支选择与回滚机制。社区关注的核心问题包括：系统级改动的搜索空间巨大且不可微，如何高效评估与择优；进化出的系统是否只在基准上过拟合；自修改系统的可解释性、可审计性与安全边界；以及如何让"改进改进机制本身"的元层也被纳入闭环而不失控。

## 研究挑战

- 搜索空间组合爆炸，每次评估都需真实运行，样本效率低、算力成本高。
- 评估基准被进化过程"攻陷"（目标作弊、基准过拟合）。
- 自修改代码的正确性与安全性：错误改动可能破坏系统自身。
- 演化档案（archive）管理：多样性保持、分支选择与回滚。
- 可解释与可审计：难以追溯系统为何演化成当前形态。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，系统级自进化是其"自进化机制"综述的核心层次之一。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，系统自重写 / 自修复相关工作均在收录范围。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 本站本身是一个"爬取 → 抽取 → 归并 → 推荐"的多 Agent 流水线，是系统自进化方法的试验床。

## 相关工作

**代码 / 框架**
- [Darwin Gödel Machine (dgm)](https://github.com/jennyzzt/dgm) — 开放式进化的自改进编码 Agent，自己修改自己的代码并经基准验证
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) — AlphaEvolve 的开源复现，进化式代码优化框架
- [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) — Sakana AI 开放式、样本高效的程序进化框架
- [ADAS](https://github.com/ShengranHu/ADAS) — Automated Design of Agentic Systems：元 Agent 在代码空间搜索新 Agent 设计
- [AFlow](https://github.com/FoundationAgents/AFlow) — MCTS 自动生成 Agent 工作流
- [DSPy](https://github.com/stanfordnlp/dspy) — 声明式 LM 程序框架，可对提示与模块进行自动优化
- [TextGrad](https://github.com/zou-group/textgrad) — 以自然语言反馈为"梯度"自动优化复合 AI 系统
- [Trace](https://github.com/microsoft/Trace) — 基于执行轨迹的生成式优化（"下一代 AutoDiff"）
- [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) — 自指式递归自改进 Agent 框架
- [EvoAgentX](https://github.com/ANative-Lab/EvoAgentX) — 自进化 Agent 生态系统，自动演化工作流
- [Self-Evolving-Agents](https://github.com/CharlesQ9/Self-Evolving-Agents) — 自进化 Agent 综述配套资源库
- [Awesome-Self-Evolving-Agents](https://github.com/ANative-Lab/Awesome-Self-Evolving-Agents) — 自进化 AI Agent 综述与论文清单

**论文**
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) — 自修改代码 + 开放式档案，SWE-bench 从 20% 提升到 50%
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) — DeepMind 进化式编码 Agent，改进矩阵乘法等算法
- [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349)
- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) — 元 Agent 搜索 Agent 设计空间
- [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762)
- [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444)
- [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496)
- [Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs](https://arxiv.org/abs/2406.16218)
- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046)
- [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407)
