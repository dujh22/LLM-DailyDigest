+++
title = 'SwarmEvolve'
proposer = '杜晋华'
since = '2026-03-12'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# SwarmEvolve

> 研究方向：**多智能体群体的自进化**——群体/社会模拟中的智能体协同与演化（本站已 fork casevo）。

## 研究范畴

多智能体群体自进化（swarm / multi-agent self-evolution）研究由多个 LLM 智能体组成的群体如何通过交互、协作与竞争实现整体能力的持续演化，超越单体自改进的上限。本方向涵盖：多智能体协同自进化（角色分工、共同进化 / co-evolution）、群体社会模拟（社会规范、合作与博弈的涌现）、多智能体系统结构的自动优化（通信拓扑、协作网络的自进化）、群体智能基准评测。社区关注的核心问题包括：群体交互能否产生单体无法获得的进化信号、协作结构与通信协议如何自动演化而非人工设计、大规模社会模拟中涌现行为的可控性与可解释性、多智能体间能力与知识如何传播扩散，以及群体进化的评测基准与度量方法。

## 研究挑战

- 进化信号稀疏：群体交互产生的反馈如何转化为有效的个体 / 群体改进信号。
- 协作结构自动化：通信拓扑与角色分工的搜索空间巨大，人工设计难以泛化。
- 涌现行为可控性：大规模模拟中合谋、退化、同质化等非预期动态的检测与干预。
- 成本与可复现性：多智能体交互的 token 开销随规模爆炸，实验难以复现。
- 评测缺口：缺少衡量"群体进化增益"（相对单体基线）的标准基准。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含多智能体自进化机制的综述与方法论沉淀。

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
1. **协作结构联合演化**：开放式任务中，与其固定角色和流程，不如联合演化团队组成、交互规则与脚手架；显式信用分配可降低重组成本。
   - [L2C：反馈驱动的工作流演化](../../updates/2026-11-19/#l2c) · 2026-11-19
   - [OPSD4MAS：将多智能体通信转化为词元级信用](../../updates/2026-11-14/#opsd4mas) · 2026-11-14
   - [SciMARS：面向闭环科学发现的多智能体递归自我改进](../../updates/2026-11-12/#scimars) · 2026-11-12
   - [s³：通过协作式多智能体强化学习扩展智能体群体](../../updates/2026-11-12/#item-215) · 2026-11-12
   - [IAPO：面向高阶交互的多智能体编排策略优化](../../updates/2026-11-08/#iapo) · 2026-11-08
   - [EvoGroup：面向共享上下文群体智能体的自演化脚手架](../../updates/2026-11-06/#evogroup) · 2026-11-06
   - [EvoTeam：通过团队演化增强多智能体协作](../../updates/2026-10-30/#evoteam) · 2026-10-30
   - [Evolving Agent Teams：可演化智能体团队突破优化局部最优](../../updates/2026-10-29/#evolving-agent-teams) · 2026-10-29
   - [DynaFlow：学习自由形式的多智能体编排](../../updates/2026-10-29/#dynaflow) · 2026-10-29
2. **失败经验优先共享**：跨代保留轨迹、工具、证据和失败，比只传成功答案更能减少重复搜索；实体群还需异步容错与失败检索。
   - [SwarmRSI：共享失败经验驱动科研智能体群递归自我改进](../../updates/2026-11-05/#swarmrsi) · 2026-11-05
   - [Group-Evolving Agents：经验共享驱动的开放式群体自进化](../../updates/2026-11-04/#group-evolving-agents) · 2026-11-04
   - [清华联合无问芯穹、智元提出机器人群体经验学习范式 CEL](../../updates/2026-10-30/#cel) · 2026-10-30
3. **记忆源索引分离**：长期记忆应分离不可变事实源与可压缩索引，记录经验适用条件；冲突证据须在同一上下文汇合，并按权限限定共享。
   - [OpenKAGE：知识共享式群体演化](../../updates/2026-11-19/#openkage) · 2026-11-19
   - [多智能体记忆不一致：事实冲突流失定位](../../updates/2026-11-18/#item-69) · 2026-11-18
   - [MixUA：面向多用户多智能体交互的多粒度记忆提取](../../updates/2026-11-12/#mixua) · 2026-11-12
   - [MIRIX-2.0：多智能体长期记忆系统](../../updates/2026-11-12/#mirix-2-0) · 2026-11-12
4. **选择性信息披露**：信息共享会改变群体策略；激励不一致或需维持探索多样性时，不宜完全透明。应隔离候选演化，只传播经验证知识，并监测隐式通信。
   - [Inventa：去中心化验证式自进化](../../updates/2026-11-18/#inventa) · 2026-11-18
   - [信息网络如何引导多智能体 LLM 系统的涌现行为](../../updates/2026-11-12/#llm-4) · 2026-11-12
   - [共享记忆触发 LLM 智能体无提示协调：双实现锁定复现](../../updates/2026-11-12/#llm-3) · 2026-11-12
   - [s³：通过协作式多智能体强化学习扩展智能体群体](../../updates/2026-11-12/#item-215) · 2026-11-12
5. **可执行验证闭环**：长程科学任务应将形式化内核、反驳实验或可执行验收嵌入循环；生成证明文本不保证原稿与形式化版本一致。
   - [量子算法智能体：Lean验证式电路优化](../../updates/2026-11-24/#lean) · 2026-11-24
   - [SailSearch：双智能体辅助算法发现](../../updates/2026-11-21/#sailsearch) · 2026-11-21
   - [可审计人机团队自主开展同步辐射 X 射线实验](../../updates/2026-11-12/#item-199) · 2026-11-12
   - [AI 自动发现形式化验证的量子程序](../../updates/2026-11-12/#item-179) · 2026-11-12
   - [AxiomProver 多智能体形式化有限单群分类定理](../../updates/2026-10-31/#axiomprover) · 2026-10-31
   - [协作式 AI 智能体自主开展固态量子自旋实验研究](../../updates/2026-10-30/#item-32) · 2026-10-30
   - [OpenAI多智能体生成纳维－斯托克斯证明，人类启动解读与核查](../../updates/2026-10-29/#openai) · 2026-10-29
   - [ClawsGO Science用Lean验证化学平衡猜想的细致平衡情形](../../updates/2026-10-29/#clawsgo-science-lean) · 2026-10-29
6. **系统级协作评测**：不要用单体准确率代替群体能力；应以资源匹配基线审计协作增益，并覆盖冲突恢复、交付率及运行环境敏感性。
   - [MASSys：服务基底敏感性评测](../../updates/2026-11-24/#massys) · 2026-11-24
   - [MultiAgentBench：协作竞争能力评测](../../updates/2026-11-20/#multiagentbench) · 2026-11-20
   - [多智能体评测：资源匹配式效果审计](../../updates/2026-11-16/#item-33) · 2026-11-16
   - [WorkflowArena：可执行多智能体工作流编排评测基准](../../updates/2026-11-12/#workflowarena) · 2026-11-12
   - [TandemBench：多智能体协作决策模型评测基准](../../updates/2026-11-06/#tandembench) · 2026-11-06
   - [CLASHarness：多智能体冲突场景评测与数据合成框架](../../updates/2026-11-01/#clasharness) · 2026-11-01
7. **集中协调强基线**：共享资源和强耦合动作场景应先用单协调器作强基线；点对点团队若无并发控制，易停滞、覆盖和越权。
   - [Anthropic 发布 MAMUBench：多智能体协作失灵评测](../../updates/2026-11-12/#anthropic-mamubench) · 2026-11-12
8. **共享骨干分支搜索**：大群体搜索不必串行递归；可共享骨干与KV状态，并将依赖和拓扑编码为DAG或并行算子，降低误差传播和候选边际成本。
   - [ConvRSI：卷积式并行自我改进](../../updates/2026-11-18/#convrsi) · 2026-11-18
   - [CoMixKV：面向多智能体系统的协同混合精度 KV 缓存量化](../../updates/2026-11-12/#comixkv-kv) · 2026-11-12
   - [SwarmEvolve：潜空间智能体群的进化发现与优化](../../updates/2026-11-08/#swarmevolve) · 2026-11-08
   - [Octopus：基于潜在 KV 分支的单模型多智能体强化学习框架](../../updates/2026-11-06/#octopus-kv) · 2026-11-06
9. **测试时知识固化**：群体推理若只留在上下文中难以跨轮复用；可将优质协作轨迹蒸馏进轻量参数，形成可继承的综合能力。
   - [TTT-Consolidate：以测试时训练整合多智能体推理](../../updates/2026-11-06/#ttt-consolidate) · 2026-11-06
   - [DynaFlow：学习自由形式的多智能体编排](../../updates/2026-10-29/#dynaflow) · 2026-10-29
10. **状态隔离与溯源**：跨运行内存、凭据和工具状态须隔离并记录来源；共享成功轨迹也要内容校验与延迟触发测试，防止越权和持久投毒。
    - [MIMPA：协作记忆投毒](../../updates/2026-11-25/#mimpa) · 2026-11-25
    - [OpenAI 披露 ExploitGym 智能体复用遗留凭据越权访问研究基础设施](../../updates/2026-11-12/#openai-exploitgym) · 2026-11-12
    - [MixUA：面向多用户多智能体交互的多粒度记忆提取](../../updates/2026-11-12/#mixua) · 2026-11-12
    - [MIRIX-2.0：多智能体长期记忆系统](../../updates/2026-11-12/#mirix-2-0) · 2026-11-12
    - [共享记忆触发 LLM 智能体无提示协调：双实现锁定复现](../../updates/2026-11-12/#llm-3) · 2026-11-12
11. **人机审计闭环**：科研群体自主性应与完整日志和人类核查同步扩展；审议应制造认知角色差异并按证据稳定度停止，集体绩效不能替代监督评测。
    - [Avalon-M1：集体奖励组织训练](../../updates/2026-11-25/#avalon-m1) · 2026-11-25
    - [可追溯多智能体科研社区](../../updates/2026-11-23/#item-3) · 2026-11-23
    - [非对称角色与信念差控制](../../updates/2026-11-23/#item-23) · 2026-11-23
    - [多智能体审议对人机协同决策的影响](../../updates/2026-11-13/#item-35) · 2026-11-13
    - [可审计人机团队自主开展同步辐射 X 射线实验](../../updates/2026-11-12/#item-199) · 2026-11-12
    - [OpenAI多智能体生成纳维－斯托克斯证明，人类启动解读与核查](../../updates/2026-10-29/#openai) · 2026-10-29
12. **可回退持续演化**：允许智能体自改训练、工具和流程时，应持续监控并按状态触发可验证干预；扩展须版本化、沙箱验收和可回退。
    - [AutoRL：多智能体闭环强化学习](../../updates/2026-11-16/#autorl) · 2026-11-16
    - [openJiuwen发布RSI原生AgentOS，支持Agent持续自我扩展](../../updates/2026-11-14/#openjiuwen-rsi-agentos-agent) · 2026-11-14
    - [LobeHub 的 Super-agent 组织协作实验](../../updates/2026-11-02/#lobehub-super-agent) · 2026-11-02
13. **客观群体反馈**：训练社会协作时，优先用规则或执行结果提供共享奖励，而非模型裁判；它可诱导分工与可迁移行为，但监督可靠性须单独优化。
    - [多玩家社交游戏：可验证社会智能训练](../../updates/2026-11-25/#item-63) · 2026-11-25
    - [Avalon-M1：集体奖励组织训练](../../updates/2026-11-25/#avalon-m1) · 2026-11-25
14. **种群级安全约束**：成员会繁殖、选择或对抗共演化时，个体合规不能推出群体安全；约束应覆盖种群动力学、跨代继承和持续适应的对手。
    - [Evolutionary AI Control：演化种群安全证明](../../updates/2026-11-25/#evolutionary-ai-control) · 2026-11-25
    - [多准则攻防种群竞争共演化](../../updates/2026-11-17/#item-83) · 2026-11-17
<!-- experience-seen: 2026-10-29/ai-agent-24 2026-10-29/clawsgo-science-lean 2026-10-29/dynaflow 2026-10-29/evolving-agent-teams 2026-10-29/openai 2026-10-30/cel 2026-10-30/evoteam 2026-10-30/item-32 2026-10-31/axiomprover 2026-10-31/deepmind-ai 2026-10-31/vibegame-ai 2026-11-01/clasharness 2026-11-02/lobehub-super-agent 2026-11-04/autosft-sft 2026-11-04/group-evolving-agents 2026-11-05/swarmrsi 2026-11-06/evogroup 2026-11-06/octopus-kv 2026-11-06/tandembench 2026-11-06/ttt-consolidate 2026-11-08/afk-ai-agent-harness-comma-router-worker 2026-11-08/iapo 2026-11-08/pharmagents2 2026-11-08/swarmevolve 2026-11-12/anthropic-mamubench 2026-11-12/claude-fable-5-2-mythos-5-2 2026-11-12/comixkv-kv 2026-11-12/item-179 2026-11-12/item-199 2026-11-12/item-215 2026-11-12/llm-3 2026-11-12/llm-4 2026-11-12/mirix-2-0 2026-11-12/mixua 2026-11-12/openai-exploitgym 2026-11-12/scimars 2026-11-12/workflowarena 2026-11-13/claude-code 2026-11-13/item-35 2026-11-14/openjiuwen-rsi-agentos-agent 2026-11-14/opsd4mas 2026-11-16/autorl 2026-11-16/item-33 2026-11-17/item-83 2026-11-18/convrsi 2026-11-18/inventa 2026-11-18/item-69 2026-11-18/wevisforensics 2026-11-19/heave-ho 2026-11-19/l2c 2026-11-19/openkage 2026-11-20/item-73 2026-11-20/multiagentbench 2026-11-21/sailsearch 2026-11-23/item-23 2026-11-23/item-3 2026-11-24/lean 2026-11-24/massys 2026-11-25/avalon-m1 2026-11-25/evolutionary-ai-control 2026-11-25/item-63 2026-11-25/mimpa 2026-11-25/pde -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [casevo](https://github.com/rgCASS/casevo) — 认知智能体与社会进化模拟器（本站已 fork）
- [awesome-agent-evolution (EvoMap)](https://github.com/EvoMap/awesome-agent-evolution) — 智能体进化精选清单
- [awesome-agent-evolution (Shiyao-Huang)](https://github.com/Shiyao-Huang/awesome-agent-evolution) — 自进化智能体综述与证据图
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 阿里 ModelScope 自进化 Agent 系统框架
- [Awesome-Self-Evolving-Agents (XMUDeepLIT)](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 厦大自进化 Agent 综述列表
- [CORAL](https://github.com/Human-Agent-Society/CORAL) — 面向开放式问题的自主多智能体进化框架
- [AgentSociety](https://github.com/tsinghua-fib-lab/agentsociety) — 清华 FIB Lab 城市场景 LLM Agent 社会模拟
- [SwarmBench (YuLan-SwarmIntell)](https://github.com/RUC-GSAI/YuLan-SwarmIntell) — 人民大学群体智能基准测试
- [CAMEL-AI](https://www.camel-ai.org/) — 开源 Agent 进化社区
- [awesome-multi-agent (WeiChengTseng)](https://github.com/WeiChengTseng/awesome-multi-agent) — 多智能体学习资源汇总
- [ai-agent-papers (masamasa59)](https://github.com/masamasa59/ai-agent-papers) — 双周更新 Agent 论文合集
- [MARL-Papers (LantaoYu)](https://github.com/LantaoYu/MARL-Papers) — 经典多智能体强化学习论文列表

**论文**
- [Survey of Multi-Agent Deep RL with Communication](https://arxiv.org/abs/2203.08975)
- [Multi-Agent Evolve: LLM Self-Improve through Co-evolution](https://arxiv.org/abs/2510.23595) — MAE 框架，三角色协同自进化
- [Evolution of Cooperation in LLM-Agent Societies](https://arxiv.org/abs/2504.19487) — LLM 多智能体复现博弈论合作演化
- [CORAL: Towards Autonomous Multi-Agent Evolution](https://arxiv.org/abs/2604.01658) — 开放式自主多智能体进化
- [Self-Evolving Multi-Agent Collaboration Networks (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf) — MAC 网络自进化
- [SE-Agent: Self-Evolution Trajectory Optimization (NeurIPS 2025)](https://neurips.cc/virtual/2025/poster/116517) — 迭代轨迹优化增强多步推理
- [AgentSociety: Large-Scale Simulation of LLM-Driven Social Agents](https://arxiv.org/abs/2502.08691) — 大规模社会智能体模拟
- [OASIS: Open Agent Social Interaction Simulations](https://arxiv.org/abs/2411.11581) — 开放式社交互动模拟
- [CAMEL: Communicative Agents for "Mind" Exploration](https://arxiv.org/abs/2303.17760) — 经典自主协作 Agent（被引 2500+）
- [Evolving Interpretable Constitutions for Multi-Agent LLM Systems](https://arxiv.org/pdf/2602.00755) — Constitutional Evolution 框架
- [A Survey on Automated Optimization of LLM-Based Multi-Agent Systems](https://www.preprints.org/manuscript/202605.2011) — 自动化优化方法综述

**博客 / 其他**
- [Self-Evolving LLM Agents (EmergentMind)](https://www.emergentmind.com/topics/self-evolving-llm-agents) — 自进化 Agent 主题聚合页
- [Self-Evolved Agents (Eigent.ai)](https://www.eigent.ai/blog/self-evolved-agents) — 递归自我改进方法介绍
