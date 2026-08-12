+++
title = 'EvolveLLM'
proposer = '杜晋华'
since = '2026-08-12'
date = 2026-08-12T00:00:00+08:00
draft = false
toc = true
+++

# EvolveLLM

> 研究方向：**大语言模型（LLM）的自我进化 / 自我改进**——通过自生成数据、自我奖励、自我博弈、自我精炼、推理时自我改进等范式，让 LLM 在缺乏（或尽量少依赖）人类标注的情况下持续提升自身能力。与聚焦“推理”的 [[EvolveLRM]] 互补，这里覆盖更通用的基础模型自进化。

## 公开相关资源

**代码 / 框架 / 资源仓库**
- [Awesome-Self-Improving-Agents](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents) — 基础模型智能体自我改进的精选清单（★347）
- [Awesome-LLM-Self-Improvement](https://github.com/dongxiangjue/Awesome-LLM-Self-Improvement) — LLM 推理时自我改进（ITSI）论文与资源整理（★110）
- [awesome-agent-evolution](https://github.com/Shiyao-Huang/awesome-agent-evolution) — 智能体进化 / 自进化 / 记忆系统的开放综述与证据图谱（★174）
- [self-improvement-llm](https://github.com/Zesearch/self-improvement-llm) — 系统级自我改进语言模型技术整理

**论文（经典与方法）**
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — LLM 自我进化方法综述（被引 996+）
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — LLM 作为自身裁判生成偏好数据自我改进（ICML 2024）
- [Self-Play Fine-Tuning (SPIN)](https://arxiv.org/abs/2401.01335) — 自我博弈微调，弱模型变强模型，无需额外人类标注（ICML 2024）
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) — 单模型自我反馈迭代精炼（NeurIPS 2023）
- [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610) — 仅用自身生成的推理作为训练信号实现自我改进（EMNLP 2023）
- [CRITIC: Self-Correction with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) — 与外部工具交互的自我批评与纠正（ICLR 2024）
- [Self-Instruct: Aligning LMs with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) — 用模型自身生成的指令对齐语言模型（ACL 2023）
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) — 用 AI 反馈（RLAIF）实现无害化对齐

**论文（前沿与边界）**
- [On the Limits of Self-Improving in Large Language Models](https://arxiv.org/abs/2601.05280) — 自我改进的理论极限分析

## 关键子主题

- **自生成数据 / 自指令**：Self-Instruct 范式，用模型自身扩张指令与样本，相关 [[DataEvolve]]。
- **自我奖励 / 偏好学习**：Self-Rewarding、RLAIF、迭代 DPO，模型充当自身裁判。
- **自我博弈**：SPIN 等让模型与历史版本对抗以变强。
- **自我精炼 / 自我纠正**：Self-Refine、CRITIC，推理时与训练时双轨。
- **推理时自我改进（ITSI）**：不重训，仅在推理阶段提升输出质量。
- **持续学习与遗忘**：避免灾难性遗忘的连续自我进化。
