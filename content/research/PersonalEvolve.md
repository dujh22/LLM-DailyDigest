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

## 自研洞察

<!-- human-only:start 自研洞察｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->
*（待人工补充）*
<!-- human-only:end 自研洞察 -->

## 自研经验

<!-- human-only:start 自研经验｜仅限人类手动编辑：AI 与自动化流程不得修改，确需修改必须先询问人类并获得同意 -->
*（待人工补充）*
<!-- human-only:end 自研经验 -->

## 研究经验

<!-- research-experience:start｜随日报整备自动更新：每条经验是面向整个研究社区的洞察或方法论，后附支撑它的具体工作。可人工修订，下次自动更新会在此基础上增量合并 -->
1. **可迁移演化画像**：长期画像不要压成静态事实或绑定某代模型；应由用户掌控关系层，显式记录关系、时间、偏好转变及策略效果，并分离变更检测和内容修复。
   - [MERIT：经验引导的个性化说服记忆](../../updates/2026-11-28/#merit) · 2026-11-28
   - [HabitusMem：信念式动态偏好记忆](../../updates/2026-11-20/#habitusmem) · 2026-11-20
   - [认知共生体：关系可迁移的终身增强](../../updates/2026-11-19/#item-1) · 2026-11-19
   - [TRACE：关系感知持续个性化](../../updates/2026-11-17/#trace) · 2026-11-17
   - [TransMem：面向演化式个人记忆的转变感知检索](../../updates/2026-11-12/#transmem) · 2026-11-12
   - [MemShift：分离个人记忆的变更检测与修复评测](../../updates/2026-11-06/#memshift) · 2026-11-06
   - [EvoMemState：面向个人智能体的演化记忆状态](../../updates/2026-11-06/#evomemstate) · 2026-11-06
2. **可控选择性遗忘**：偏好局部漂移时只撤销受影响维度；显式与参数记忆均应独立控制强度、期限和拒答，并用在线效用决定冲突抑制范围。
   - [参数记忆：可控持久与衰减](../../updates/2026-11-20/#item-63) · 2026-11-20
   - [RegimeCouncil：配对证据路由记忆冲突](../../updates/2026-11-18/#regimecouncil) · 2026-11-18
   - [PEARL：部分偏好漂移下的预测误差自适应选择性遗忘](../../updates/2026-11-06/#pearl) · 2026-11-06
3. **弱证据分层**：零散行为先进入歧义缓冲区，跨会话聚合并经后续交互确认后再升格为画像规则；反馈应按保真度加权。
   - [Learning through Discernment：辨别式反馈学习](../../updates/2026-11-19/#learning-through-discernment) · 2026-11-19
   - [UAPM：从未来交互学习的不确定性感知动态用户画像](../../updates/2026-11-12/#uapm) · 2026-11-12
   - [WeFair：基于反馈保真度的短视频个性化查询改写](../../updates/2026-11-03/#wefair) · 2026-11-03
   - [HABIT-Bench：评估智能体从长期弱证据中归纳用户习惯](../../updates/2026-10-29/#habit-bench) · 2026-10-29
4. **证据保真记忆**：长期记忆应保留事实的局部语境与原始证据，并按实体、事件、情感、时间等视图组织；先优化记忆构建边界，再按查询动态分配检索预算与语义轴。
   - [ContextFact：事实上下文记忆](../../updates/2026-11-28/#contextfact) · 2026-11-28
   - [Procedure Memory：情节驱动的程序记忆](../../updates/2026-11-26/#procedure-memory) · 2026-11-26
   - [STARK：事件作边的双图记忆](../../updates/2026-11-20/#stark) · 2026-11-20
   - [ChronoDossier：长档案式时序记忆评测](../../updates/2026-11-20/#chronodossier) · 2026-11-20
   - [KV-LTM：会话KV缓存长期记忆](../../updates/2026-11-18/#kv-ltm-kv) · 2026-11-18
   - [Axis-LoRA：面向个人记忆检索的多轴嵌入适配](../../updates/2026-11-08/#axis-lora) · 2026-11-08
   - [ETAMem：面向长期对话智能体的异构记忆解耦与对齐](../../updates/2026-10-29/#etamem) · 2026-10-29
5. **历史自监督**：无标注历史可转成带证据问答，终局反馈再拆为逐步、逐用户信用，先优化写入、检索和上下文而非立即改参。
   - [PMR：面向用户个性化记忆更新的细粒度信用分配](../../updates/2026-11-12/#pmr) · 2026-11-12
   - [MemSteer：从用户历史生成监督信号以优化智能体记忆](../../updates/2026-10-30/#memsteer) · 2026-10-30
6. **纠错沉淀资产**：将纠正、工具失败和反复选择提炼为带适用条件的程序或技能；在决策点按本地任务效用路由并运行时验证，才能跨会话或客户端复用。
   - [Procedure Memory：情节驱动的程序记忆](../../updates/2026-11-26/#procedure-memory) · 2026-11-26
   - [P-FedSkill：个性化联邦技能学习](../../updates/2026-11-26/#p-fedskill) · 2026-11-26
   - [Brain：会话驱动的个性化技能演化](../../updates/2026-11-20/#brain) · 2026-11-20
   - [DeepSeek Harness：可演化插件工作台](../../updates/2026-11-15/#deepseek-harness) · 2026-11-15
   - [Skill Adapter：通用技能的个性化适配与在线路由](../../updates/2026-11-14/#skill-adapter) · 2026-11-14
   - [LiveAsset：从纠正性交互学习意图资产以控制智能体运行](../../updates/2026-11-12/#liveasset) · 2026-11-12
   - [Decision Context：智能体持久化行为学习](../../updates/2026-11-12/#decision-context) · 2026-11-12
7. **有界递归改进**：自我改进应限定可修改组件，用失败轨迹修补记忆与脚手架；候选更新须经独立或跨模型回归测试，失败默认拒绝并可回滚。
   - [Safe Personal RSI：回滚修复式安全更新](../../updates/2026-11-19/#safe-personal-rsi) · 2026-11-19
   - [长程角色扮演对话的递归自我改进](../../updates/2026-11-08/#item-53) · 2026-11-08
   - [Reglos：递归自我改进的自演化个人记忆智能体](../../updates/2026-11-05/#reglos) · 2026-11-05
8. **主动协助闭环**：主动助手要联合评测感知、预判、介入时机、行动和适应；持续在线还需用户边界、失败重规划与可撤回机制。
   - [持续在线个人智能：三模块持续闭环](../../updates/2026-11-17/#item-1) · 2026-11-17
   - [Looki 发布第一视角多模态模型系列 Loom](../../updates/2026-11-14/#looki-loom) · 2026-11-14
   - [Deep Personalization：面向本地主动智能体的持续上下文观察](../../updates/2026-11-12/#deep-personalization) · 2026-11-12
   - [千问 Personal Agent：模型、记忆与生态的协同架构](../../updates/2026-11-06/#personal-agent) · 2026-11-06
   - [单一紧凑解码器联合决策辅助时机与记忆提示生成](../../updates/2026-10-30/#item-31) · 2026-10-30
   - [StreamVibe：面向意图演变的主动式视频智能体](../../updates/2026-10-29/#streamvibe) · 2026-10-29
   - [主动式 AI 如何走向超级智能体：6A 框架综述](../../updates/2026-10-29/#ai-6a) · 2026-10-29
9. **个性化安全边界**：个性化记忆不得覆盖高风险任务的确认、验证和必知信息；完整性审计应独立于事实核查与风格适配。
   - [Remembered as Brief：偏好记忆静默删减](../../updates/2026-11-18/#remembered-as-brief) · 2026-11-18
   - [记忆陷阱：语言智能体从良性交互中过度泛化](../../updates/2026-11-08/#item-44) · 2026-11-08
   - [ProcessPrefBench：个体过程偏好的跨任务迁移评测](../../updates/2026-11-05/#processprefbench) · 2026-11-05
10. **因果化个性评测**：错用户对照必须匹配主题，否则下降不能证明利用了个体偏好；还应分测个体生成与评价、跨任务迁移和虚构证据。
    - [AI Twin：学习式社交评价](../../updates/2026-11-24/#ai-twin) · 2026-11-24
    - [个性化评测中的错误用户对照混淆](../../updates/2026-11-12/#item-187) · 2026-11-12
    - [ProcessPrefBench：个体过程偏好的跨任务迁移评测](../../updates/2026-11-05/#processprefbench) · 2026-11-05
11. **轻量适配优先**：单用户数据少时先用偏好方向、规则、技能或共享生成的脚手架；流式参数更新可由紧凑状态生成，但仅在预注册曲线稳定胜过简单基线后采用。
    - [WASP：流式权重个性化](../../updates/2026-11-25/#wasp) · 2026-11-25
    - [HyperHarness：历史驱动的个性化脚手架生成](../../updates/2026-11-24/#hyperharness) · 2026-11-24
    - [Train After You Measure：预注册个性化微调曲线](../../updates/2026-11-18/#train-after-you-measure) · 2026-11-18
    - [Skill Adapter：通用技能的个性化适配与在线路由](../../updates/2026-11-14/#skill-adapter) · 2026-11-14
    - [LiveAsset：从纠正性交互学习意图资产以控制智能体运行](../../updates/2026-11-12/#liveasset) · 2026-11-12
    - [UPSHIFT：从人机交互反馈轨迹中提取用户偏好导向](../../updates/2026-11-06/#upshift) · 2026-11-06
12. **分歧驱动标注**：主动获取反馈时应选择用户偏好仍未解决的答案分歧，而非模型自身犹豫，并优先索取高保真验证信号。
    - [MPG-DPO：偏好锥引导在线对齐](../../updates/2026-11-18/#mpg-dpo) · 2026-11-18
    - [WeFair：基于反馈保真度的短视频个性化查询改写](../../updates/2026-11-03/#wefair) · 2026-11-03
13. **谱系化隐私治理**：个人原始上下文优先端侧保留；跨用户只共享按范围分级提炼的经验，撤回时须沿谱系清除提示、技能与学习状态并验证不可再用。
    - [P-FedSkill：个性化联邦技能学习](../../updates/2026-11-26/#p-fedskill) · 2026-11-26
    - [跨载体隐私记忆治理](../../updates/2026-11-23/#item-45) · 2026-11-23
    - [MixUA：面向多用户多智能体交互的多粒度记忆提取](../../updates/2026-11-12/#mixua) · 2026-11-12
    - [Deep Personalization：面向本地主动智能体的持续上下文观察](../../updates/2026-11-12/#deep-personalization) · 2026-11-12
14. **个体实验闭环**：高噪声个体反馈宜用可审计、可证伪的N-of-1实验和贝叶斯选试验，避免把短期相关性固化为长期画像。
    - [EpiCoach：面向个体生理建模的智能体贝叶斯实验设计](../../updates/2026-10-30/#epicoach) · 2026-10-30
15. **托管导向指标**：Personal Agent应以事务托管量、完成率、长期托管留存和人工接管率衡量进化收益，而非使用时长或活跃度。
    - [Personal Agent 的北极星指标：从活跃度转向事务托管](../../updates/2026-11-13/#personal-agent) · 2026-11-13
<!-- experience-seen: 2026-11-23/item-45 2026-11-24/ai-twin 2026-11-24/hyperharness 2026-11-25/wasp 2026-11-26/p-fedskill 2026-11-26/procedure-memory 2026-11-28/contextfact 2026-11-28/merit -->
<!-- research-experience:end -->

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
