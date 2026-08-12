+++
title = 'EvolveLLM'
proposer = '杜晋华'
since = '2026-08-12'
date = 2026-08-12T00:00:00+08:00
draft = false
toc = true
+++

# EvolveLLM

> 研究方向：**大语言模型（LLM）的自我进化 / 自我改进**——在尽量少依赖人工标注的前提下，让基础模型持续提升自身能力。与聚焦"推理"的 [[EvolveLRM]] 互补，覆盖更通用的基础模型自进化。

## 研究范畴

EvolveLLM 是关于**大语言模型自我进化 / 自我改进**的通用研究方向，涵盖：自生成数据 / 自指令、自我奖励与偏好学习（Self-Rewarding、RLAIF、迭代 DPO）、自我博弈（Self-Play）、自我精炼 / 自我纠正（Self-Refine、CRITIC）、推理时自我改进（ITSI），以及持续学习与遗忘。社区关注的核心问题包括：自我改进的边界（提升是否单调、是否存在上限或退化）、自我奖励 / 自评判的系统性偏差如何度量与缓解、合成数据与自迭代是否引发模型崩溃（model collapse）、持续学习中如何平衡新能力与灾难性遗忘，以及推理时自我改进（不重训）的可靠性与成本。

## 研究挑战

- 奖励作弊（reward hacking）与退化解。
- 偏差、幻觉与错误沿迭代累积。
- 自我进化系统的对齐、安全与可控性。
- 评测有效性：如何评估一个持续变化的系统。
- 算力与数据成本随迭代轮次膨胀。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM)
- [Daily-Work-Log-Public](https://github.com/dujh22/Daily-Work-Log-Public)
- [Daily-Work-Log-Private](https://github.com/dujh22/Daily-Work-Log-Private)
- [Dujinhua-wiki](https://github.com/dujh22/Dujinhua-wiki)
- [Dujinhua-wiki-Source](https://github.com/dujh22/Dujinhua-wiki-Source)
- [MetaEvaluation](https://github.com/dujh22/MetaEvaluation)
- [AutoLLM](https://github.com/dujh22/AutoLLM)

## 相关工作

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
