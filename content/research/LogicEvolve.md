+++
title = 'LogicEvolve'
proposer = '杜晋华'
since = '2025-05-06'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# LogicEvolve

> 研究方向：大型语言模型的**逻辑推理能力自我进化**——让模型在逻辑 / 多步推理上持续自我改进。

## 研究范畴

大型语言模型的**逻辑推理能力自我进化**，关注让模型在形式逻辑、多步 / 组合推理上持续自我改进。本方向涵盖：神经符号（neuro-symbolic）推理、逻辑推理基准、自我验证 / 自我校正，以及 System 1 → System 2 的能力跃迁。社区关注的核心问题包括：推理过程的逻辑忠实度（faithfulness）与可验证性、组合泛化与分布外泛化及推理鲁棒性、符号求解器 / 验证器如何与神经网络互补，以及自我进化是否会放大逻辑错误（幻觉沿推理链传播）。

## 研究挑战

- 逻辑正确性的自动验证困难、ground truth 成本高。
- 基准污染与"模式匹配"伪推理。
- 符号化方法的可扩展性与工程复杂度。
- 评测有效性：区分真实推理与记忆。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理的智能体评测与自进化平台，统一演绎/归纳、多跳、符号、程序与博弈逻辑，支持 CLUB/CLUBv2/ToolCLUB/ExCLUB/BBH/SynLogic/LogiQA2 等多基准，覆盖数据合成、评测、训练（LLaMA-Factory/verl）与可视化榜单全链路。
- [clubWeb](https://github.com/anonymous1Coder/clubWeb) — LogicEvolve/CLUB 的可视化榜单前端（React + TypeScript + Vite），即 clubweb.site。

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
1. **验证器反馈闭环**：可形式化任务宜采用“生成—局部验证—约束反馈—修复”闭环；确定性检查器比笼统自我反思更能阻断错误传播。
   - [FOL-Proof：确定性语义验证](../../updates/2026-11-26/#fol-proof) · 2026-11-26
   - [TopoVerus：基于学习反例与课程奖励的形式化证明修复](../../updates/2026-11-12/#topoverus) · 2026-11-12
   - [实时捕获并纠正 LLM 推理错误](../../updates/2026-11-12/#llm-2) · 2026-11-12
   - [能证明多少就证明多少：混合神经符号逻辑自然语言推理](../../updates/2026-11-12/#item-165) · 2026-11-12
   - [BiVerify：双向验证闭环驱动数学自我纠错](../../updates/2026-11-12/#biverify) · 2026-11-12
   - [ALBI：LLM 引导的迭代式归纳逻辑编程](../../updates/2026-11-06/#albi-llm) · 2026-11-06
2. **分层过程奖励**：长链强化学习应按子问题或证据阶段设置检查点并分配信用，以缩短有效奖励跨度，避免终局奖励掩盖早期错误。
   - [CREDO：面向时序推理智能体的证据条件信用分配](../../updates/2026-11-03/#credo) · 2026-11-03
   - [H²R：基于分层提示奖励的数学推理强化学习](../../updates/2026-10-30/#h-r) · 2026-10-30
3. **忠实性单独优化**：答案正确或推理简短都不代表模型真实依赖所述步骤；训练与评测需单列依赖忠实性，并接受其与性能、效率的权衡。
   - [二维推理：语义图量化推理忠实与效率](../../updates/2026-11-24/#item-67) · 2026-11-24
   - [Verifiable Logic：神经符号临床推理审计](../../updates/2026-11-20/#verifiable-logic) · 2026-11-20
   - [后训练如何影响语言模型的显式算法推理](../../updates/2026-11-12/#item-80) · 2026-11-12
   - [Chain of Faith：策略内部奖励增强推理依赖](../../updates/2026-11-06/#chain-of-faith) · 2026-11-06
4. **组合外推评测**：思维链外推依赖复用可靠的原子状态转移；评测应分别改变规则组合、语境与推理深度，并精确监督中间状态。
   - [ORION：精确规范状态监督](../../updates/2026-11-23/#orion) · 2026-11-23
   - [规模化 ConceptARC：评估推理模型的概念理解](../../updates/2026-11-06/#conceptarc) · 2026-11-06
   - [思维链推理的分布外泛化机制](../../updates/2026-11-05/#item-35) · 2026-11-05
5. **验证引导采样**：测试时推理不宜只选验证器最高分轨迹；结合步骤正确性、未来结果估计与多轨迹一致性可兼顾正确率和搜索多样性。
   - [验证器引导的自一致性：不完美生成器与验证器下的测试时推理](../../updates/2026-11-06/#item-32) · 2026-11-06
6. **首错定位修复**：多步自纠应逐项核验关键论断、定位首个错误并检查遗漏分支，而非仅依据最终答案重写整条推理链。
   - [AGPV：智能体引导过程验证](../../updates/2026-11-17/#agpv) · 2026-11-17
   - [实时捕获并纠正 LLM 推理错误](../../updates/2026-11-12/#llm-2) · 2026-11-12
   - [BiVerify：双向验证闭环驱动数学自我纠错](../../updates/2026-11-12/#biverify) · 2026-11-12
7. **形式证明信任链**：机器编译只保证给定命题可推导；前沿证明还须审计题面对应、依赖与外部证书，并由独立内核和专家复现。
   - [OpenAI Math：AI批量生成数学证明](../../updates/2026-11-26/#openai-math-ai) · 2026-11-26
   - [FOL-Proof：确定性语义验证](../../updates/2026-11-26/#fol-proof) · 2026-11-26
   - [VP≠VNP：AI生成Lean证明](../../updates/2026-11-25/#vp-vnp-ai-lean) · 2026-11-25
   - [VP≠VNP：平坦-收缩双路证明](../../updates/2026-11-24/#vp-vnp) · 2026-11-24
   - [Navier–Stokes爆破证明：Claude协作与Lean核验](../../updates/2026-11-23/#navier-stokes-claude-lean) · 2026-11-23
   - [黎曼猜想形式化证明：多内核交叉验真](../../updates/2026-11-23/#item-7) · 2026-11-23
   - [Claude：Lean形式化证明黎曼猜想](../../updates/2026-11-21/#claude-lean) · 2026-11-21
   - [通过完整集合划分精确认证 QPLIB 2096 全局最优性](../../updates/2026-11-06/#qplib-2096) · 2026-11-06
   - [PSI用AI辅助突破5项量子信息开放问题](../../updates/2026-10-29/#psi-ai-5) · 2026-10-29
   - [OpenAI 邀外部专家与 Lean 核查 AI 科学证明](../../updates/2026-10-29/#openai-lean-ai) · 2026-10-29
   - [OpenAI与Anthropic模型被曝独立证伪指数时间假设](../../updates/2026-10-29/#openai-anthropic) · 2026-10-29
   - [OpenAI多智能体生成纳维－斯托克斯证明，人类启动解读与核查](../../updates/2026-10-29/#openai) · 2026-10-29
8. **分工式形式化**：超大证明工程适合按检索、翻译、证明、反例和核验分工并行，但入库仍须逐项检查原论证与形式命题的忠实对应。
   - [Turing Agent：分工式端到端形式化验证](../../updates/2026-11-18/#turing-agent) · 2026-11-18
   - [AI 自动发现形式化验证的量子程序](../../updates/2026-11-12/#item-179) · 2026-11-12
   - [AxiomProver 多智能体形式化有限单群分类定理](../../updates/2026-10-31/#axiomprover) · 2026-10-31
   - [数十个 AI Agent 24 天形式化有限单群分类定理](../../updates/2026-10-29/#ai-agent-24) · 2026-10-29
9. **形式化驱动发现**：形式化不应只作事后验收；将失败引理与可检验规格反馈给搜索，在实测昂贵时以证明替代实验评价，可发现反例、替代方案与更紧界。
   - [量子算法智能体：Lean验证式电路优化](../../updates/2026-11-24/#lean) · 2026-11-24
   - [Turing Agent：分工式端到端形式化验证](../../updates/2026-11-18/#turing-agent) · 2026-11-18
   - [Claude Code形式化三元哥德巴赫猜想并发现原证明错误](../../updates/2026-11-13/#claude-code) · 2026-11-13
   - [AI 引导的 Lean 证明精化改进解析常数界](../../updates/2026-11-12/#ai-lean) · 2026-11-12
   - [AxiomProver 多智能体形式化有限单群分类定理](../../updates/2026-10-31/#axiomprover) · 2026-10-31
   - [数十个 AI Agent 24 天形式化有限单群分类定理](../../updates/2026-10-29/#ai-agent-24) · 2026-10-29
10. **机器友好证明重构**：库中缺少原证明依赖时，可搜索更弱假设、引入机器友好概念并重构证明路线，而非持续复刻人类原稿。
    - [Astra：自创容量量完成形式证明](../../updates/2026-11-20/#astra) · 2026-11-20
    - [AutoAssumption：搜索算法假设以发现 ML 系统新算法](../../updates/2026-11-13/#autoassumption-ml) · 2026-11-13
    - [AI 引导的 Lean 证明精化改进解析常数界](../../updates/2026-11-12/#ai-lean) · 2026-11-12
11. **可溯源知识监督**：训练与自进化知识库应保留来源、课程顺序、证明依赖和定量保证，使监督可审计并能被后续证明任务复用。
    - [TOME-Math：从结构化教科书扩展数学证明监督](../../updates/2026-11-13/#tome-math) · 2026-11-13
    - [FARMS：面向自动化计算科学的可验证知识基础](../../updates/2026-11-01/#farms) · 2026-11-01
12. **持久推理图**：累积式自动研究应保存可回放的命题、前提、反例和验证关系，让已证发现更新问题图并自动暴露下一轮缺口。
    - [Space-X：证据链驱动空间自进化](../../updates/2026-11-21/#space-x) · 2026-11-21
    - [Colombo：自组织优化科研系统](../../updates/2026-11-19/#colombo) · 2026-11-19
    - [RRE：以演化推理图推进累积式数学研究](../../updates/2026-11-06/#rre) · 2026-11-06
13. **显式工具接口**：隐式思维链接入工具时，应插入少量可观测、可控制的显式状态标记，避免工具调用依赖不可审计的潜在推理。
    - [TAC-CoT：交错显式 Token 增强工具化隐式思维链](../../updates/2026-11-06/#tac-cot-token) · 2026-11-06
<!-- experience-seen: 2026-11-19/colombo 2026-11-20/astra 2026-11-20/verifiable-logic 2026-11-21/claude-lean 2026-11-21/space-x 2026-11-23/claude 2026-11-23/item-7 2026-11-23/navier-stokes-claude-lean 2026-11-23/orion 2026-11-24/item-67 2026-11-24/lean 2026-11-24/vp-vnp 2026-11-25/9-4 2026-11-25/vp-vnp-ai-lean 2026-11-26/fol-proof 2026-11-26/openai-math-ai -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [Logic-LLM](https://github.com/teacherpeterpan/Logic-LLM) — 用符号化求解器增强 LLM 逻辑推理
- [mem-kk-logic](https://github.com/AlphaPav/mem-kk-logic) — LLM 逻辑推理中的记忆研究（本站已 fork）
- [SE-Agent](https://github.com/JARVIS-Xs/SE-Agent) — LLM 代码智能体自进化框架
- [Reasoning-Self-Evolution-Survey](https://github.com/cs-holder/Reasoning-Self-Evolution-Survey) — 配套复杂推理自进化综述的资源仓库
- [self-improvement-llm (Zesearch)](https://github.com/Zesearch/self-improvement-llm) — 系统级自我改进语言模型技术整理
- [Awesome-Agentic-Reasoning](https://github.com/weitianxin/Awesome-Agentic-Reasoning) — Agent 推理论文（含自我进化专题）
- [Awesome-LLM-Reasoning-with-NeSy (LAMDA)](https://github.com/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy) — 神经符号学习提升 LLM 推理合集
- [LogicBench](https://github.com/Mihir3009/LogicBench) — 25 种推理模式的逻辑推理基准数据集
- [Neuro-Symbolic Large Models](https://llm-symbol.github.io/) — 符号引导 LLM 推理资源页

**论文**
- [LogicVista: Multimodal LLM Logical Reasoning Benchmark](https://arxiv.org/abs/2407.04973)
- [Making Large Language Models Better Reasoners with Alignment](https://arxiv.org/abs/2309.02144)
- [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) — 零数据自进化推理（被引 157）
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — LLM 自我进化综述
- [Debate, Train, Evolve (DTE) (EMNLP 2025)](https://arxiv.org/abs/2505.15734) — 多 Agent 辩论训练推理自进化（被引 21）
- [STaR: Bootstrapping Reasoning With Self-Taught Reasoning](https://arxiv.org/abs/2203.14465) — 经典自我推理引导（被引 1959）
- [START: Self-taught Reasoner with Tools](https://arxiv.org/abs/2503.04625) — STaR 工具增强版（被引 51）
- [ReVISE (ICML 2025)](https://arxiv.org/abs/2502.14565) — 测试时自我验证推理细化
- [On the Generalization Gap in Self-Evolving Language Models](https://arxiv.org/abs/2606.01075) — 自进化 LLM 泛化差距
- [LogicGraph: Benchmarking Multi-Path Logical Reasoning](https://arxiv.org/abs/2602.21044) — 神经符号评估器多路径逻辑基准
- [FOLIO (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.1229) — 一阶逻辑推理数据集（被引 398）
- [P-FOLIO](https://arxiv.org/abs/2410.09207) — 前提化一阶逻辑推理评估
- [GSM-Symbolic (Apple)](https://machinelearning.apple.com/research/gsm-symbolic) — 符号化数学推理揭示 LLM 脆弱性
- [ALIVE: Adversarial Self-Evolution](https://arxiv.org/abs/2602.05472) — 对抗性自我进化激活推理
- [A Survey of Reasoning LLMs](https://arxiv.org/abs/2502.17419) — System 1→2 视角推理综述（被引 415）
- [Towards Large Reasoning Models: Reinforced Self-Training Survey](https://arxiv.org/abs/2501.09686) — 强化自我训练综述
- [CRESCENT (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.337.pdf) — 零监督推理自举（被引 11）
- [ReST-MCTS\* (NeurIPS 2024)](https://neurips.cc/virtual/2024/poster/96343) — 过程奖励引导树搜索强化自训练
- [RL-STaR: Theoretical Analysis of RL in Self-Taught Reasoner](https://arxiv.org/abs/2410.23912) — STaR 的 RL 理论分析
- [CARE-STaR (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.1116.pdf) — 约束感知自我推理
- [Entropy-Aware Self-Evolution Framework](https://openreview.net/pdf?id=nXENWUSRMw) — 熵感知自进化
- [Mixture-of-Thought (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/file/af80ce1011eb35fe1023c320158c2ad9-Paper-Conference.pdf) — 混合思维提升推理泛化（被引 24）
