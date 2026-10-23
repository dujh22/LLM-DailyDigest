+++
title = 'HumanEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# HumanEvolve

> 研究方向：**AI 辅助的人类进化**——AI 作为协作者、导师与认知放大器，如何改变人的学习、技能、判断与创造方式，以及去技能化与认知负债等反向效应。

## 研究范畴

AI 辅助的人类进化（AI-augmented human evolution）关注"人这一侧"如何因 AI 而改变：AI 承担检索、写作、编码与决策支持后，人类的时间分配、技能结构与认知习惯发生怎样的迁移；哪些设计让人变强（upskilling、认知参与度提升），哪些让人变弱（deskilling、认知债务、判断外包）。本方向涵盖：AI 辅助学习与教育、AI 协作对劳动生产率与技能结构的实证影响、人机联合决策的互补性与增益条件、认知负荷与批判性思维的长期变化、AI 辅助科研与知识工作、面向"增强人"的交互界面设计，以及职业通道与人才培养体系的结构性变化。与 [[PersonalEvolve]] 的分工：PersonalEvolve 研究"AI 自己怎么变强"，本方向研究"人借助 AI 怎么变强或变弱"。

## 研究挑战

- 长期效应难以度量：短期效率提升与长期能力退化往往方向相反。
- 增益条件不明：何种任务分工、解释方式与信任校准才能产生人机互补而非依赖。
- 认知负债与去技能化：隐性知识与练习机会被 AI 挤占后的补偿机制。
- 职业通道断裂：初级岗位减少对人才培养的影响需长期追踪。
- 公平与可及性：增强效应是否只惠及已具备较高能力的人群。

## 自研项目

- [AML-LLM](https://github.com/dujh22/AML-LLM) — 教材《Advanced Machine Learning: Large Language Models》配套仓库，本身即 AI 辅助知识传递的教学实践。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，"模型自进化 → 人机共同进化"是其中的研究延伸。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 以 AI 过滤信息、由人反馈标注的日常科研信息流，是"AI 增强研究者认知带宽"的实践样本。

## 相关工作

**代码 / 框架**
- [hh-rlhf](https://github.com/anthropics/hh-rlhf) — Anthropic 有益无害人类偏好数据集，人类判断作为训练信号的基准资源
- [weak-to-strong](https://github.com/openai/weak-to-strong) — 人类监督失效后如何继续引导强模型的实验代码

**论文**
- [Human-AI Coevolution](https://arxiv.org/abs/2306.13723) — 人机共演化作为独立研究领域
- [Position: Towards Bidirectional Human-AI Alignment](https://arxiv.org/abs/2406.09264) — "双向对齐"：AI 对齐人类价值，同时人类认知被 AI 塑造
- [Generative AI at Work](https://arxiv.org/abs/2304.11771) — 生成式 AI 对一线工作者生产率与技能的实证研究
- [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://arxiv.org/abs/2506.08872) — AI 辅助写作对认知参与度与脑活动的影响
- [Experimental evidence on the productivity effects of generative artificial intelligence](https://arxiv.org/abs/2302.06590) — 客服场景的随机对照实验
- [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390) — 人类能力上限之外的监督问题
