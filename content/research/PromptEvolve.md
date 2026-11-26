+++
title = 'PromptEvolve'
proposer = '杜晋华'
since = '2026-10-08'
date = 2026-10-08T00:00:00+08:00
draft = false
toc = true
+++

# PromptEvolve

> 研究方向：**提示自进化**——系统提示 / 指令 / 示例 / 多阶段 LM 程序的自动优化与持续进化，以及智能体从执行反馈中自我改写提示的闭环。

## 研究范畴

提示自进化（prompt self-evolution / automatic prompt optimization）把提示词视为可搜索、可学习、可版本化的"软参数"：在冻结模型权重的前提下，由模型自身或外层优化器依据任务反馈持续改写系统提示、指令措辞、推理模板、few-shot 示例乃至多阶段 LM 程序的全部提示集合。本方向涵盖：基于进化算法 / 束搜索的离散提示搜索（Promptbreeder、EvoPrompt、ProTeGi 类）、LLM-as-Optimizer 的元提示优化（OPRO、APE）、面向多阶段程序的编译式优化（DSPy / MIPRO）、以自然语言反馈为"梯度"的反思式进化（TextGrad、GEPA）、智能体在运行时把失败经验沉淀为提示 / 技能 / 记忆的自我改写（Reflexion、Voyager 类），以及提示与模型权重协同进化（提示优化 vs. 强化微调的样本效率对比）。社区关注的核心问题包括：提示优化是否能以远低于 RL 的 rollout 成本逼近甚至超过权重训练、自动演化的提示能否跨模型 / 跨任务迁移、如何在开发集上避免过拟合与"评测钻空子"、多阶段程序中各节点提示的信用分配，以及自演化提示的可审计性与安全边界。

## 研究挑战

- 评估成本与过拟合：每轮候选都需跑完整评测，开发集小则易过拟合，评测指标本身也可能被提示"钻空子"。
- 跨模型迁移脆弱：针对某一模型演化出的提示换模型后收益常大幅衰减，提示与模型的耦合难以解耦。
- 多阶段程序的信用分配：Agent 流水线包含多个提示节点，终局反馈难以归因到具体节点与措辞。
- 搜索空间无界且不连续：自然语言提示缺乏平滑的优化几何，变异 / 交叉算子的设计高度依赖经验。
- 提示 vs. 权重的边界：何时该演化提示、何时该更新权重，二者协同的理论与工程框架尚缺。
- 可审计性与安全漂移：自动改写的系统提示可能引入越权指令、泄露约束或削弱安全护栏，需版本化与门禁。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 本站日报系统，推荐判定 / 自动标注 / 概览生成均由提示驱动，可作为提示迭代与回归评测的实验场。

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
1. **评测先于搜索**：优化停滞常源于评测分辨率不足或选择噪声；比较机制时须匹配采样、轮次、词元与成本，并用留出集确认增益。
   - [Resolution Hypothesis：评测分辨率瓶颈](../../updates/2026-11-19/#resolution-hypothesis) · 2026-11-19
   - [DCPS：示例条件式提示搜索](../../updates/2026-11-18/#dcps) · 2026-11-18
   - [BiPA：用二部归因重新评估智能体技能优化](../../updates/2026-10-29/#bipa) · 2026-10-29
2. **经验先策展**：先筛选可靠任务并检索成功轨迹，避免噪声反馈污染更新；失败样本只有按模式归纳后才适合沉淀为经验。
   - [LCE：失败模式多样性诊断](../../updates/2026-11-25/#lce) · 2026-11-25
   - [GEPA-Curator：面向自改进智能体的经验策展学习](../../updates/2026-10-29/#gepa-curator) · 2026-10-29
3. **批量并行搜索**：反思式优化应在同轮并行提出并评估多个候选，而非串行单候选，以改善墙钟时间、预算利用率和解质量。
   - [批处理反思优化循环：并行候选让 GEPA 更快更优](../../updates/2026-10-29/#gepa) · 2026-10-29
4. **约束搜索空间**：冻结不可变契约并分离通用规则与角色策略，只开放必要编辑范围；这比无约束重写更可审计，也更少行为漂移。
   - [SPLICE：分块约束式提示演化](../../updates/2026-11-17/#splice) · 2026-11-17
   - [FinEvolveKG：面向金融知识图谱的可控可归因提示演化](../../updates/2026-11-12/#finevolvekg) · 2026-11-12
5. **评判提示持续校准**：评判提示应视为持续维护的软件资产；监控用户与被评智能体的分布漂移，再用新交互闭环重校准。
   - [AutoRefine：基于工作流结果自动校准代码评判器](../../updates/2026-11-12/#autorefine) · 2026-11-12
   - [PromptOps：LLM 评判系统的迭代提示优化](../../updates/2026-11-06/#promptops-llm) · 2026-11-06
6. **量规化优化接口**：将目标拆成任务量规或专用误差信号，比单一总分更易定位修改；评测昂贵时可用世界模型预筛编辑。
   - [教育AI提示精炼：情感认知双反馈](../../updates/2026-11-24/#item-47) · 2026-11-24
   - [LegalEvolver：量规引导自进化的法律判决预测智能体](../../updates/2026-11-05/#legalevolver) · 2026-11-05
   - [RubricWorld：世界模型引导的 LLM 评分规约优化](../../updates/2026-11-03/#rubricworld-llm) · 2026-11-03
7. **安全更新门禁**：把风险设为硬约束，并从执行失误提炼可触发、可迁移的安全原则；每次更新仍须回归复测，失败即拒绝或回滚。
   - [PRECEPT：失误驱动的安全原则演化](../../updates/2026-11-26/#precept) · 2026-11-26
   - [Safe Personal RSI：回滚修复式安全更新](../../updates/2026-11-19/#safe-personal-rsi) · 2026-11-19
   - [CPS与CRISP：风险认证提示优化](../../updates/2026-11-17/#cps-crisp) · 2026-11-17
8. **先学技能再压缩**：先在不惩罚长度时学会可靠技能，再以准确率护栏删减指令；从一开始惩罚词元更易牺牲能力。
   - [EfficientSkill：准确率护栏式技能压缩](../../updates/2026-11-17/#efficientskill) · 2026-11-17
9. **反馈器独立审计**：更强评论器或可追溯门控都不保证更新有益；应以故障注入和隐藏留出集审计影响，并淘汰无效规则。
   - [Notary门控回顾环：规则准入效用验证](../../updates/2026-11-25/#notary) · 2026-11-25
   - [CRITFAULT：评论器安全审计](../../updates/2026-11-17/#critfault) · 2026-11-17
10. **脚手架整体演化**：冻结权重时，可协同演化提示、工具、记忆、技能和更新器；对递归自改写须限定深度与可修改范围。
    - [MetaFORGE：执行反馈式脚手架优化](../../updates/2026-11-26/#metaforge) · 2026-11-26
    - [智能体脚手架演化：冻结策略领域适配](../../updates/2026-11-20/#item-60) · 2026-11-20
    - [长程角色扮演对话的递归自我改进](../../updates/2026-11-08/#item-53) · 2026-11-08
11. **路由提示先优化**：工具或能力路由受容量限制时，先优化路由提示可部分弥补模型不足，并在维持质量时减少下游调用开销。
    - [小语言模型能力路由：容量与提示优化对质量和效率的影响](../../updates/2026-11-14/#item-30) · 2026-11-14
12. **撤架后验收**：训练脚手架应按撤除提示后的学生能力验收；由教师动态诊断瓶颈并生成策略，可避免只学会依赖脚手架。
    - [AutoScaffold：AI 自动生成自适应训练脚手架](../../updates/2026-11-12/#autoscaffold-ai) · 2026-11-12
13. **软提示组合验收**：独立学会的软提示技能不可直接视为可拼接模块；入库前须检验组合兼容、原能力保持与跨模型迁移。
    - [软提示技能的组合兼容与保持](../../updates/2026-11-26/#item-39) · 2026-11-26
    - [CSPD：可组合软提示蒸馏](../../updates/2026-11-25/#cspd) · 2026-11-25
14. **质量约束多样性**：优化创意等分布属性时，应在质量门槛下选择差异化候选；只追求行为多样性会牺牲平均质量。
    - [SEPO：演化系统提示集成](../../updates/2026-11-26/#sepo) · 2026-11-26
<!-- experience-seen: 2026-11-19/resolution-hypothesis 2026-11-19/safe-personal-rsi 2026-11-20/item-60 2026-11-24/item-47 2026-11-25/cspd 2026-11-25/lce 2026-11-25/notary 2026-11-26/item-39 2026-11-26/metaforge 2026-11-26/precept 2026-11-26/sepo 2026-11-26/vsft -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [DSPy](https://github.com/stanfordnlp/dspy) — 斯坦福声明式 LM 编程框架，内置 MIPROv2 / BootstrapFewShot 等提示与示例优化器
- [GEPA](https://github.com/gepa-ai/gepa) — 反思式提示进化：用自然语言反思 + 帕累托前沿采样演化多节点提示
- [TextGrad](https://github.com/zou-group/textgrad) — 以 LLM 文本反馈为"梯度"自动微分提示、代码与答案
- [OPRO](https://github.com/google-deepmind/opro) — DeepMind "LLM 即优化器"，在元提示中迭代生成更优指令
- [EvoPrompt](https://github.com/beeevita/EvoPrompt) — 遗传算法 / 差分进化与 LLM 结合的离散提示进化
- [automatic_prompt_engineer (APE)](https://github.com/keirp/automatic_prompt_engineer) — 自动指令生成与选择的早期代表实现
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 含提示 / 工作流进化专题的自进化 Agent 合集

**论文**
- [Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution](https://arxiv.org/abs/2309.16797) — DeepMind 自指式进化：任务提示与变异提示同时进化
- [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers (EvoPrompt)](https://arxiv.org/abs/2309.08532) — LLM 充当进化算子的离散提示优化
- [Large Language Models as Optimizers (OPRO)](https://arxiv.org/abs/2309.03409) — 以自然语言描述优化问题、LLM 迭代生成解
- [Large Language Models Are Human-Level Prompt Engineers (APE)](https://arxiv.org/abs/2211.01910) — 自动指令生成 + 评分选择
- [Automatic Prompt Optimization with "Gradient Descent" and Beam Search (ProTeGi)](https://arxiv.org/abs/2305.03495) — 文本"梯度"+ 束搜索的提示编辑
- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) — 把提示工程编译为可优化的 LM 程序
- [Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs (MIPROv2)](https://arxiv.org/abs/2406.11695) — 多阶段程序的指令与示例联合优化
- [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) — 文本反馈反向传播的通用优化框架
- [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) — 以极少 rollout 的反思式提示进化超越 GRPO
- [PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization](https://arxiv.org/abs/2310.16427) — MCTS 规划式提示优化
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — 把失败反思写回提示上下文的运行时自进化
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — 技能库作为可增长的提示 / 代码资产
- [Are Large Language Models Good Prompt Optimizers?](https://arxiv.org/abs/2402.02101) — 对 LLM 反思式提示优化有效性边界的审视
- [A Systematic Survey of Automatic Prompt Optimization Techniques](https://arxiv.org/abs/2502.16923) — 自动提示优化方法综述
