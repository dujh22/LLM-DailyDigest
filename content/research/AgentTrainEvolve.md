+++
title = 'AgentTrainEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# AgentTrainEvolve

> 研究方向：**Agent 训练侧自进化**——通过多轮 Agentic RL、自博弈与自生成课程，让 Agent 的参数在与环境交互中持续进化。

## 研究范畴

Agent 训练侧自进化（training-time agent self-evolution）关注如何把 Agent 在环境中的交互经验稳定地转化为参数更新：从早期的轨迹蒸馏 / 指令微调（AgentTuning），走向多轮、长程、带工具调用的 Agentic 强化学习，再到由 Agent 自己提出任务、构造课程、合成经验并自我博弈的零数据训练范式（Absolute Zero、SPIRAL、WebRL 的自进化在线课程）。本方向涵盖：面向 Agent 的 RL 训练框架与基础设施（verl、SkyRL、rLLM、Agent Lightning）、多轮交互下的信用分配与回合级奖励、自博弈与对抗式课程生成、经验合成与模拟环境放大（DreamGym 类）、训练-评测环境生态（AgentGym），以及 Agent RL 中的自进化动力学诊断（RAGEN 揭示的"回声陷阱"等失败模式）。社区关注的核心问题包括：长程稀疏奖励下训练是否稳定、自生成任务的难度与多样性如何自适应、训练出的能力能否跨环境迁移、以及 Agent RL 的算力与环境吞吐瓶颈如何突破。

## 研究挑战

- 多轮长程交互的信用分配与稀疏 / 延迟奖励。
- 自博弈与自生成课程的难度失控、多样性坍缩与"回声陷阱"。
- 环境吞吐与 rollout 成本成为训练瓶颈，异步与解耦训练框架仍在演进。
- 训练环境过拟合：在训练环境上提升但跨环境泛化差。
- 奖励作弊与评估器被攻陷（尤其在使用 LLM 作为奖励时）。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，训练侧自进化是《大语言模型复杂推理的自我进化机制》综述的核心路线之一。
- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理智能体评测与自进化平台，提供可程序化验证的任务族，可作为 Agent RL 训练环境。

## 相关工作

**代码 / 框架**
- [verl](https://github.com/verl-project/verl) — 字节跳动开源的 LLM RL 训练框架，Agentic RL 主流基础设施
- [SkyRL](https://github.com/NovaSky-AI/SkyRL) — 面向长程多轮 Agent 任务的模块化 RL 框架
- [rLLM](https://github.com/rllm-org/rllm) — Agentica 面向语言 Agent 后训练的 RL 框架
- [Agent Lightning](https://github.com/microsoft/agent-lightning) — 微软"训练任意 Agent"的 RL 框架，训练与 Agent 实现解耦
- [ART](https://github.com/OpenPipe/ART) — Agent Reinforcement Trainer，多轮 Agent 的 GRPO 训练
- [AgentGym](https://github.com/WooooDyy/AgentGym) — 多环境 Agent 训练-评测平台与自进化方法 AgentEvol
- [WebRL](https://github.com/THUDM/WebRL) — 自进化在线课程 RL 训练 Web Agent
- [RAGEN](https://github.com/mll-lab-nu/RAGEN) — 多轮 RL 训练 Agent 并诊断自进化失败模式
- [Absolute Zero Reasoner](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) — 零数据自博弈：模型自己出题、自己解题
- [SPIRAL](https://github.com/spiral-rl/spiral) — 零和博弈自博弈激发推理能力
- [AgentTuning](https://github.com/THUDM/AgentTuning) — 轨迹微调赋予 LLM 通用 Agent 能力
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 自进化 Agent 系统：自问、自导航、自归因

**论文**
- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) — Agentic RL 全景综述
- [AgentTuning: Enabling Generalized Agent Abilities for LLMs](https://arxiv.org/abs/2310.12823)
- [AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151)
- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337)
- [RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2504.20073) — StarPO 框架与"回声陷阱"
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)
- [SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2506.24119)
- [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) — SPIN
- [SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks](https://arxiv.org/abs/2503.15478) — 多轮信用分配
- [Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03680)
- [Scaling Agent Learning via Experience Synthesis](https://arxiv.org/abs/2511.03773) — DreamGym：合成经验放大 Agent RL
- [AgentEvolver: Towards Efficient Self-Evolving Agent System](https://arxiv.org/abs/2511.10395)
