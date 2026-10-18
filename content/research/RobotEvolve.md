+++
title = 'RobotEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# RobotEvolve

> 研究方向：**具身智能自进化**——机器人 / 具身 Agent 在仿真与真实环境中通过自主数据采集、自动奖励设计与 sim-to-real 迭代持续提升。

## 研究范畴

具身智能自进化（embodied self-evolution）关注机器人与具身 Agent 如何在与物理（或高保真仿真）世界的交互中自主改进：由模型自己提出任务、生成场景与资产、设计奖励函数、采集与筛选轨迹，再回灌到视觉-语言-动作（VLA）基础模型的训练中，形成"任务生成 → 仿真执行 → 数据回灌 → 模型更新 → sim-to-real 验证"的闭环。本方向涵盖：VLA / 通用机器人基础模型、跨本体（cross-embodiment）数据与迁移、LLM 驱动的奖励与课程自动设计（Eureka 类）、生成式仿真与自动场景合成（RoboGen 类）、世界模型驱动的想象训练，以及具身 Agent 的技能库积累与长程规划。社区关注的核心问题包括：真实交互数据昂贵且不可无限扩展时如何让自进化闭环"跑得起"、仿真进化出的能力能否稳定迁移到真实机器人、自动奖励与自评是否会被策略作弊，以及如何度量具身能力的真实泛化而非在固定基准上过拟合。

## 研究挑战

- 真实世界数据采集成本高、不可逆风险大，自进化闭环难以高频迭代。
- sim-to-real 差距：仿真中进化出的策略在真实环境中退化。
- 自动奖励设计与自评信号的作弊与误导（reward hacking）。
- 跨本体、跨任务的泛化度量缺乏统一标准，易在基准上过拟合。
- 安全约束下的探索：具身系统的失败可能造成物理损害。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述；具身方向作为自进化闭环从数字世界延伸到物理世界的验证场。
- [Awesome-RSI](https://github.com/dujh22/Awesome-RSI) — 递归自我改进资源清单，收录具身 / 机器人自改进相关工作。

## 相关工作

**代码 / 框架**
- [OpenVLA](https://github.com/openvla/openvla) — 开源 7B 视觉-语言-动作模型，基于 Open X-Embodiment 数据训练
- [Octo](https://github.com/octo-models/octo) — 开源通用机器人策略，支持跨本体微调
- [Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment) — 跨机构、跨本体机器人学习数据集与 RT-X 模型
- [openpi (π0)](https://github.com/Physical-Intelligence/openpi) — Physical Intelligence 开源的 π0 / π0-FAST 通用机器人策略
- [LeRobot](https://github.com/huggingface/lerobot) — Hugging Face 真实机器人学习全流程库（数据、训练、部署）
- [Eureka](https://github.com/eureka-research/Eureka) — LLM 编码自动设计奖励函数，达到人类水平
- [DrEureka](https://github.com/eureka-research/DrEureka) — LLM 引导的 sim-to-real 迁移（奖励 + 域随机化自动设计）
- [RoboGen](https://github.com/Genesis-Embodied-AI/RoboGen) — 生成式仿真自动提出任务、生成场景并采集技能数据
- [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) — 面向机器人与具身 AI 的生成式物理引擎
- [ManiSkill](https://github.com/mani-skill/ManiSkill) — GPU 并行的通用操作技能仿真基准
- [Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T) — NVIDIA 人形机器人通用基础模型 GR00T N1 开源实现
- [Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) — 具身智能入门与资源指南

**论文**
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) — VLA 范式奠基
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) — 跨本体数据规模化带来正迁移
- [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)
- [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) — 流匹配动作生成的通用机器人策略
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)
- [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) — 奖励函数的进化搜索
- [DrEureka: Language Model Guided Sim-To-Real Transfer](https://arxiv.org/abs/2406.01967)
- [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) — 自提任务 + 生成仿真的数据飞轮
- [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093) — VLA 综述
