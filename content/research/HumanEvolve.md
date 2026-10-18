+++
title = 'HumanEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# HumanEvolve

> 研究方向：**人机协同进化**——AI 借人类反馈进化、人类借 AI 提升认知与技能的双向闭环，以及由此带来的对齐与认知影响问题。

## 研究范畴

人机协同进化（human-AI co-evolution）研究人与 AI 系统在长期交互中互相塑造的双向反馈环：一方面，人类偏好、示范与批评驱动模型对齐与改进（RLHF、宪法式 AI、可扩展监督）；另一方面，AI 作为协作者、导师与信息过滤器反过来改变人类的学习、决策与创造方式，可能带来技能提升（upskilling）也可能带来认知负债与去技能化（deskilling）。本方向涵盖：基于人类反馈的对齐与偏好学习、双向人机对齐（bidirectional alignment）、人在回路的自进化系统设计、人机共学（co-learning）与 AI 辅助研究 / 教育、AI 对人类认知与劳动生产率的实证影响，以及推荐与信息流算法与人类行为的共演化动力学。社区关注的核心问题包括：当 AI 能力超过人类时反馈信号如何保持有效（弱到强、可扩展监督）、人类反馈中的偏差与被操纵风险、如何设计让人"变强"而非"变懒"的协作界面，以及如何度量协同进化的长期效应而非单次任务效率。

## 研究挑战

- 超越人类能力后反馈信号退化：可扩展监督与弱到强泛化。
- 人类偏好的噪声、偏差与可被模型"讨好"操纵的风险。
- 认知负债与去技能化：AI 辅助可能削弱而非增强人类能力。
- 人机共演化的反馈回路难以在短期实验中观测与度量。
- 多元价值与跨文化偏好的聚合与公平性。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，人机协同进化是从"模型自进化"走向"人机共同进化"的研究延伸。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 内置 co_learner 多 Agent 共学流水线与基于研究画像的推荐系统，是"AI 过滤信息 → 人类反馈标注 → 画像进化"的人机共学实践。
- [AML-LLM](https://github.com/dujh22/AML-LLM) — 教材《Advanced Machine Learning: Large Language Models》配套仓库，含 RLHF / 评测对齐章节。

## 相关工作

**代码 / 框架**
- [TRL](https://github.com/huggingface/trl) — Hugging Face 基于人类反馈训练 Transformer 的库（SFT / RM / PPO / DPO）
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) — 高性能开源 RLHF 框架
- [hh-rlhf](https://github.com/anthropics/hh-rlhf) — Anthropic 有益无害人类偏好数据集
- [summarize-from-feedback](https://github.com/openai/summarize-from-feedback) — OpenAI 从人类反馈学习摘要的代码与数据
- [weak-to-strong](https://github.com/openai/weak-to-strong) — 弱监督引出强模型能力的实验代码

**论文**
- [Human-AI Coevolution](https://arxiv.org/abs/2306.13723) — 提出人机共演化作为独立研究领域，分析推荐系统与人类行为的反馈回路
- [Position: Towards Bidirectional Human-AI Alignment](https://arxiv.org/abs/2406.09264) — 系统综述并倡导"双向对齐"框架
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — InstructGPT，RLHF 范式确立
- [Learning to summarize from human feedback](https://arxiv.org/abs/2009.01325)
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) — 用原则 + AI 反馈替代部分人类标注
- [Scalable agent alignment via reward modeling: a research direction](https://arxiv.org/abs/1811.07871) — 可扩展监督研究路线
- [Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/abs/2312.09390) — 超越人类能力时的监督问题
- [Generative AI at Work](https://arxiv.org/abs/2304.11771) — 生成式 AI 对一线工作者生产率与技能的实证研究
- [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://arxiv.org/abs/2506.08872) — AI 辅助写作对认知参与度的影响
