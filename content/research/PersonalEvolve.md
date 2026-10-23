+++
title = 'PersonalEvolve'
proposer = '杜晋华'
since = '2026-10-18'
date = 2026-10-18T00:00:00+08:00
draft = false
toc = true
+++

# PersonalEvolve

> 研究方向：**个性化 AI 的自主进化**——为单个用户定制的模型 / Agent 依据个人数据与交互持续自我改进，而非依赖全网反馈的统一进化。

## 研究范畴

个性化自进化（personalized self-evolution）研究"为一个人服务的 AI"如何自主变强：系统从单个用户的对话、偏好、示范、纠正与行为轨迹中学习，把经验沉淀为长期记忆、用户画像、个性化技能与参数适配，使模型对齐的粒度从"全人类平均偏好"下沉到"这一个用户"。本方向涵盖：个人 Agent 的长期记忆与画像进化、用户行为轨迹转训练信号（行为监督、轨迹蒸馏）、个性化偏好学习与 RLHF 变体、从少量样本推断用户价值与个性（persona / value inference）、用户级技能归纳与复用、个性化与通用能力的权衡（catastrophic personalization）、以及个性化带来的过拟合、谄媚、隐私与越权边界。社区关注的核心问题包括：如何在不污染通用能力的前提下做用户级适配、个人数据稀缺且含噪时如何稳健学习、个性化的长期效应如何度量、以及"懂你"与"讨好你""替你决定"之间的边界。

## 研究挑战

- 单用户数据量小、噪声大、分布漂移，长期迭代容易过拟合与自我强化偏见。
- 个性化能力与通用能力的冲突：用户级微调可能损害基础能力与安全性。
- 谄媚与价值灌输：模型可能迎合用户叙事而非坚持事实与规范。
- 个性化记忆的隐私、可迁移性与用户控制权（可遗忘、可解释）。
- 越界风险：个性化偏好被误当作授权，自动代为决策或购买。
- 缺乏评测：个性化自进化的长期收益难以用单次任务指标衡量。

## 自研项目

- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 基于研究画像的推荐系统与多 Agent 共学流水线，是"AI 过滤信息 → 用户反馈标注 → 画像进化"的个性化自进化实践。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，个性化自进化是"自进化"从模型级走向用户级的研究延伸。
- [AML-LLM](https://github.com/dujh22/AML-LLM) — 教材《Advanced Machine Learning: Large Language Models》配套仓库，含 RLHF / 评测对齐章节，是用户级偏好适配的方法学基础。

## 相关工作

**代码 / 框架**
- [TRL](https://github.com/huggingface/trl) — Hugging Face 基于人类反馈训练 Transformer 的库（SFT / RM / PPO / DPO），可用于用户级偏好适配
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) — 高性能开源 RLHF 框架
- [MemGPT / Letta](https://github.com/letta-ai/letta) — 面向长期对话的分层记忆，个人 Agent 记忆进化的代表实现
- [LangMem](https://github.com/langchain-ai/langmem) — 从交互中提取与更新长期记忆
- [weak-to-strong](https://github.com/openai/weak-to-strong) — 弱监督引出强模型能力的实验代码

**论文**
- [VISTA: Steering LLMs with Latent User Values Inferred from a Few Survey Answers](https://arxiv.org/abs/2610.23702) — 从少量问卷回答推断潜在价值并个性化引导
- [PerSPL: Personalized Semi-supervised Preference Learning](https://arxiv.org/abs/2610.29219) — 将无标签回答转为用户特定训练信号
- [Trapped in Your Story](https://arxiv.org/abs/2610.23525) — 用户叙事诱导的谄媚行为受控评测
- [Human-AI Coevolution](https://arxiv.org/abs/2306.13723) — 推荐系统与用户行为的反馈回路分析
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — RLHF 范式确立，个性化适配的方法学起点
- [Generative AI at Work](https://arxiv.org/abs/2304.11771) — 生成式 AI 对个体工作者生产率与技能的实证研究
