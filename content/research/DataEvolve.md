+++
title = 'DataEvolve'
proposer = '杜晋华'
since = '2026-08-05'
date = 2026-08-07T00:00:00+08:00
draft = false
toc = true
+++

# DataEvolve

> 研究方向：**数据自进化**——以数据为中心的自进化训练数据 / 合成与迭代。

## 研究范畴

数据自进化（data-centric self-evolution）以"数据"为核心驱动，让模型自主生成、筛选、配比并迭代训练数据，从而在尽量少依赖人工标注的情况下持续提升。本方向涵盖：合成数据生成、指令进化（Evol-Instruct 类）、自奖励 / 自评判偏好数据、数据飞轮（data flywheel）、以数据为中心的 Agent 自进化。社区关注的核心问题包括：合成数据的质量 / 多样性 / 覆盖度如何度量与保证、自迭代是否会引发模型崩溃（model collapse）或分布坍缩、数据污染与配比对下游能力的边际影响，以及如何量化"数据价值"并据此做主动筛选。

## 研究挑战

- 偏差与错误在迭代中累积放大。
- 真实性与事实性控制（幻觉随合成数据传播）。
- 大规模数据治理与自动化精炼的成本。
- 长期迭代稳定性与可复现性。

## 自研项目

- [CLUB-benchmark (LogicEvolve)](https://github.com/dujh22/CLUB-benchmark) — 复杂逻辑推理的智能体评测与自进化平台，含元数据驱动的数据合成（Sudoku/迷宫/数独/Knights&Knaves/Zebra/代码推理等）与多基准（CLUB/CLUBv2/ToolCLUB/ExCLUB/BBH/SynLogic/LogiQA2）数据管线。
- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

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
1. **覆盖优先于难度**：微调选数应先覆盖输入、组合依赖与解法多样性，再追求难度；难度筛选常不及覆盖式分配，示例解答还可能掩盖组合复用成本。
   - [智能体强化学习：三轴数据缩放定律](../../updates/2026-11-25/#item-20) · 2026-11-25
   - [重新审视“RL 泛化、SFT 记忆”：SFT 数据的关键作用](../../updates/2026-11-13/#rl-sft-sft) · 2026-11-13
   - [示例解答会掩盖自生成训练数据中的规则组合能力成本](../../updates/2026-11-12/#item-106) · 2026-11-12
   - [重思数据选择：LLM 微调中覆盖度比难度更重要](../../updates/2026-11-06/#llm) · 2026-11-06
   - [Trajectory2Gym：面向工具智能体的决策接地交互合成](../../updates/2026-11-03/#trajectory2gym) · 2026-11-03
   - [Trajectory2Gym：面向工具使用智能体的决策驱动交互合成](../../updates/2026-10-29/#trajectory2gym) · 2026-10-29
   - [可控环境合成揭示工具使用智能体缩放定律](../../updates/2026-10-29/#item-58) · 2026-10-29
2. **模型无关的任务深度**：合成长程或工程任务时，用工作量、必要顺序交互深度和结构复杂度定义难度，避免依赖特定模型的轮数或成功率。
   - [BuggyMLE：可控注错扩展工程难度](../../updates/2026-11-20/#buggymle) · 2026-11-20
   - [终端长程任务的真实深度测量与合成](../../updates/2026-11-03/#item-30) · 2026-11-03
3. **真实证据接地合成**：从真实职业需求、API或协作会话反推任务，并经探测执行或模拟器验证，可兼顾规模、真实性与可复现性。
   - [VADE：专业源可验证任务合成](../../updates/2026-11-25/#vade) · 2026-11-25
   - [LogT：逻辑链引导视觉搜索](../../updates/2026-11-20/#logt) · 2026-11-20
   - [TCP4D：统一TCP跟踪与轨迹生成](../../updates/2026-11-19/#tcp4d-tcp) · 2026-11-19
   - [Ropedia Xperience 2：扩展具身环境与行为数据的黄金标准](../../updates/2026-11-14/#ropedia-xperience-2) · 2026-11-14
   - [TOME-Math：从结构化教科书扩展数学证明监督](../../updates/2026-11-13/#tome-math) · 2026-11-13
   - [SynthCorp：面向数据智能体的可定制基准生成平台](../../updates/2026-11-13/#synthcorp) · 2026-11-13
   - [Firefly：先探索后出题的可验证工具调用数据合成](../../updates/2026-11-08/#firefly) · 2026-11-08
   - [Agent-R²：基于真实来源数据合成扩展生产力智能体](../../updates/2026-11-08/#agent-r) · 2026-11-08
   - [SessionFarmer：从真实 Vibe Coding 会话构建 SWE 评测基准](../../updates/2026-11-06/#sessionfarmer-vibe-coding-swe) · 2026-11-06
   - [PyRUA-DataFarm：LLM 远程操作者驱动的真实场景机器人数据采集](../../updates/2026-11-06/#pyrua-datafarm-llm) · 2026-11-06
   - [WorkFactory：将职业意图转化为可执行任务以规模化训练智能体](../../updates/2026-10-29/#workfactory) · 2026-10-29
4. **可验证闭环供数**：递归训练应优先生成答案可独立验证、可修复的任务；验证闭环能在无教师场景下减少错误信号累积。
   - [3DCodeFactory：实机验证式3D数据合成](../../updates/2026-11-26/#3dcodefactory-3d) · 2026-11-26
   - [VeriTouch：验证式视触觉轨迹合成](../../updates/2026-11-25/#veritouch) · 2026-11-25
   - [VADE：专业源可验证任务合成](../../updates/2026-11-25/#vade) · 2026-11-25
   - [SWE-Gym-Verified：执行证据式数据审计](../../updates/2026-11-25/#swe-gym-verified) · 2026-11-25
   - [GLM-5.5：多模型后训练汇流式RSI](../../updates/2026-11-25/#glm-5-5-rsi) · 2026-11-25
   - [Game2Player：环境玩家协同演化](../../updates/2026-11-20/#game2player) · 2026-11-20
   - [Verifiable pXRD：验证器引导的爬山解析](../../updates/2026-11-16/#verifiable-pxrd) · 2026-11-16
   - [KernelMosaic：CUDA Kernel 生成数据集与智能体框架](../../updates/2026-11-13/#kernelmosaic-cuda-kernel) · 2026-11-13
   - [Firefly：先探索后出题的可验证工具调用数据合成](../../updates/2026-11-08/#firefly) · 2026-11-08
   - [PROVE：自博弈视觉-语言验证器的组合理解训练](../../updates/2026-11-06/#prove) · 2026-11-06
   - [CUA-Master：开放世界双循环递归改进计算机使用智能体](../../updates/2026-11-04/#cua-master) · 2026-11-04
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
5. **靶向合成并刷新题池**：零外部数据时可围绕目标能力及当前未知边界自合成任务，再按有效优势、正确率变化、模型分歧或风险预测刷新，避免静态题池失效。
   - [The Frontier Must Grow：验证前沿扩展训练](../../updates/2026-11-17/#the-frontier-must-grow) · 2026-11-17
   - [Model Annealing：历史自我回顾巩固](../../updates/2026-11-16/#model-annealing) · 2026-11-16
   - [ICRPM以前瞻风险预测优化Rollout任务采样](../../updates/2026-11-08/#icrpm-rollout) · 2026-11-08
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
   - [LongZero：零外部数据增强长上下文推理](../../updates/2026-10-30/#longzero) · 2026-10-30
   - [OXR 1.3B 开源：文档解析三榜第一并引入 RSI 训练](../../updates/2026-10-29/#oxr-1-3b-rsi) · 2026-10-29
6. **轨迹策展重于堆量**：自改进不能等量吸收历史轨迹，也不能只按成功筛选；应按决策质量、优化边际价值和解法新颖性策展，并贴近目标模型状态分布补入专家监督。
   - [E2L：梯度对齐经验演化](../../updates/2026-11-25/#e2l) · 2026-11-25
   - [THRIFTY：预算约束推理数据合成](../../updates/2026-11-24/#thrifty) · 2026-11-24
   - [From Acting to Learning：优化器感知梯度选样](../../updates/2026-11-23/#from-acting-to-learning) · 2026-11-23
   - [AutoMaster：技能引导式自主后训练](../../updates/2026-11-20/#automaster) · 2026-11-20
   - [RSI-Prime：决策级损失掩码训练](../../updates/2026-11-19/#rsi-prime) · 2026-11-19
   - [JudgeMix：评判器引导的混合轨迹智能体数据合成](../../updates/2026-11-14/#judgemix) · 2026-11-14
   - [SWE-Trail：历史引导的编码智能体轨迹收集](../../updates/2026-11-04/#swe-trail) · 2026-11-04
   - [GEPA-Curator：面向自改进智能体的经验策展学习](../../updates/2026-10-29/#gepa-curator) · 2026-10-29
7. **策展收益先分型**：评估数据策展时应分开测最终上限与收敛加速，并用前置小测预测持续收益，避免把早期加速误判为上限提升。
   - [数据策展究竟提升上限还是加速训练？](../../updates/2026-10-29/#item-73) · 2026-10-29
8. **防坍缩需真实锚点**：递归自消费会侵蚀稀有知识并造成表征漂移；应持续加入真实锚点，联合监测覆盖与特征，并在动力学稳定时用单代条件校准预警坍缩。
   - [单代校准预测稀有模式坍缩](../../updates/2026-11-25/#item-90) · 2026-11-25
   - [自消费训练：稀疏特征解释性退化](../../updates/2026-11-18/#item-59) · 2026-11-18
   - [自训练中的有序 Rényi 熵交叉：丰富度不等于均匀度](../../updates/2026-11-12/#r-nyi) · 2026-11-12
   - [谁为模型复制的知识买单？Rogers 悖论下的模型坍缩](../../updates/2026-11-05/#rogers) · 2026-11-05
   - [带验证合成数据的统计分析：线性回归框架](../../updates/2026-10-30/#item-46) · 2026-10-30
9. **合成预训练算力对齐**：合成数据预预训练须在总算力和自然数据量对齐后评估；独立合成阶段常不如直接训练自然语言，收益依赖初始化与预算。
   - [重新审视合成数据预预训练](../../updates/2026-10-30/#item-52) · 2026-10-30
10. **真实反馈驱动飞轮**：将真实检索、操作、用户历史与问答误差回流，可让数据或知识结构随使用更新；闭环问题须代表真实分布，生成问题收益未必迁移到人工问题。
    - [Knowledge-Base Gradient Descent：问答驱动知识库重构](../../updates/2026-11-26/#knowledge-base-gradient-descent) · 2026-11-26
    - [知识在脚手架、可靠性在权重：无教师智能体协同演化](../../updates/2026-11-13/#item-26) · 2026-11-13
    - [DriveFoundry：数据与模型协同演化的自动驾驶闭环框架](../../updates/2026-11-12/#drivefoundry) · 2026-11-12
    - [NorthCUA：以规模化经验加速计算机操作智能体](../../updates/2026-11-04/#northcua) · 2026-11-04
    - [百度搜索通过在线反馈闭环实现递归自我进化](../../updates/2026-11-01/#item-1) · 2026-11-01
    - [MemSteer：从用户历史生成监督信号以优化智能体记忆](../../updates/2026-10-30/#memsteer) · 2026-10-30
11. **自动闭环编排数据**：数据选择、配比与训练配方不宜静态全量重训；可用评测闭环重编排并在线校准代理，同时设机会配额，防止弱能力被效率反馈循环持续饿死。
    - [FEAST：公平高效自适应采样](../../updates/2026-11-26/#feast) · 2026-11-26
    - [DAiSy：自适应效用估计选数](../../updates/2026-11-25/#daisy) · 2026-11-25
    - [Piccolo：模型数据协同自进化](../../updates/2026-11-20/#piccolo) · 2026-11-20
    - [OptiMer：分布向量最优合并](../../updates/2026-11-16/#optimer) · 2026-11-16
    - [No Second Run：预训练RSI炼出801-30B-A3B模型](../../updates/2026-11-14/#no-second-run-rsi-801-30b-a3b) · 2026-11-14
    - [AutoSFT：多智能体自动配置 SFT 训练数据](../../updates/2026-11-04/#autosft-sft) · 2026-11-04
12. **推理数据去冗余**：从自生成轨迹中保留最短正确路径，或构造状态条件停止偏好，可在基本不降准确率时压缩推理开销。
    - [Concise-9B：去除推理轨迹中的冗余思考](../../updates/2026-11-06/#concise-9b) · 2026-11-06
    - [LoCo：基于本地偏好学习的推理压缩](../../updates/2026-11-05/#loco) · 2026-11-05
13. **先修监督分布失配**：稀缺或蒸馏监督应先落在学生可恢复的分布；可用相关易题、前置变换任务、可教前缀或环境校准，提高少样本学习效率。
    - [ThinkMorph-SSL：前置任务扩展交错推理](../../updates/2026-11-26/#thinkmorph-ssl) · 2026-11-26
    - [STONE：踏脚石式无标签自蒸馏](../../updates/2026-11-17/#stone) · 2026-11-17
    - [B-OPSD：自生成简报蒸馏](../../updates/2026-11-17/#b-opsd) · 2026-11-17
    - [ECOS：环境校准的智能体在策略自蒸馏](../../updates/2026-11-12/#ecos) · 2026-11-12
    - [BOPD：自举式在策略蒸馏](../../updates/2026-11-12/#bopd) · 2026-11-12
    - [TOPSD：从可教前缀进行多语言推理蒸馏](../../updates/2026-11-08/#topsd) · 2026-11-08
14. **训练样本归因审计**：数据审计不能只看难度或最终正确率：先用执行证据核验奖励标签，再结合梯度归因、中间过程探测与跨模型副作用回溯责任样本。
    - [SWE-Gym-Verified：执行证据式数据审计](../../updates/2026-11-25/#swe-gym-verified) · 2026-11-25
    - [自幻觉记忆：后训练固化错误事实](../../updates/2026-11-23/#item-49) · 2026-11-23
    - [视觉语言模型中的潜意识学习与隐性偏好迁移](../../updates/2026-11-13/#item-14) · 2026-11-13
    - [批量生成具有意外副作用的训练数据](../../updates/2026-11-08/#item-46) · 2026-11-08
    - [SimpleLoRIF：沿梯度追溯安全性退化的训练数据](../../updates/2026-11-03/#simplelorif) · 2026-11-03
15. **失败驱动反向供数**：把可诊断弱项或失败步骤转成定向分叉、扰动样本或修复轨迹；回灌前核验标签与捷径，回灌后用独立分布检查真实修复和跨任务退化。
    - [VFR：验证式失败驱动修复](../../updates/2026-11-26/#vfr) · 2026-11-26
    - [DART：不确定性引导轨迹改写](../../updates/2026-11-26/#dart) · 2026-11-26
    - [BuggyMLE：可控注错扩展工程难度](../../updates/2026-11-20/#buggymle) · 2026-11-20
    - [DeLoop：重复动作自监督脱环](../../updates/2026-11-17/#deloop) · 2026-11-17
    - [PhysLoop：以 LLM 物理认知驱动视频生成模型自我改进](../../updates/2026-11-14/#physloop-llm) · 2026-11-14
    - [EDGAR：以合成失败样本高效优化高斯化身](../../updates/2026-11-08/#edgar) · 2026-11-08
    - [PROVE：自博弈视觉-语言验证器的组合理解训练](../../updates/2026-11-06/#prove) · 2026-11-06
<!-- experience-seen: 2026-11-19/rsi-prime 2026-11-19/tabdag 2026-11-19/tcp4d-tcp 2026-11-20/automaster 2026-11-20/buggymle 2026-11-20/game2player 2026-11-20/logt 2026-11-20/piccolo 2026-11-21/egocaptioner 2026-11-23/from-acting-to-learning 2026-11-23/item-49 2026-11-24/thrifty 2026-11-25/daisy 2026-11-25/e2l 2026-11-25/glm-5-5-rsi 2026-11-25/item-20 2026-11-25/item-90 2026-11-25/swe-gym-verified 2026-11-25/vade 2026-11-25/veritouch 2026-11-26/3dcodefactory-3d 2026-11-26/dart 2026-11-26/feast 2026-11-26/knowledge-base-gradient-descent 2026-11-26/thinkmorph-ssl 2026-11-26/vfr -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [agents (aiwaves-cn)](https://github.com/aiwaves-cn/agents) — 数据中心的自进化自主语言智能体框架
- [R-Zero](https://github.com/Chengsong-Huang/R-Zero) — 零数据自进化推理
- [autosynth](https://github.com/Ahmad8864/autosynth) — 仿 Meta Autodata 的合成数据生成框架
- [AgentEvolver](https://github.com/modelscope/AgentEvolver) — 阿里 ModelScope 自进化 Agent 系统，支持训练数据自主生成
- [Evol-Instruct](https://github.com/nlpxucan/WizardLM) — WizardLM 的进化指令数据生成方法
- [Self-Rewarding-LM](https://github.com/metaillusion/Self-Rewarding-LM) — 自奖赏语言模型偏好数据生成与迭代
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) — 含数据进化专题的自进化 Agent 合集

**论文**
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — Meta/NYU LLM-as-a-Judge 自我改进（被引 996）
- [Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) — Meta-Rewarding 高层级自我改进（被引 223）
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — LLM 自我进化方法综述（含数据进化模块）
- [Adaptive Data Flywheel: MAPE Control Loops for AI Agent Improvement](https://arxiv.org/abs/2510.27051) — 数据飞轮控制环路
- [Evolving Knowledge: Towards Explanatory Evolution](https://arxiv.org/abs/2405.05122) — 知识进化与数据迭代
- [Self-Evolving Multi-Agent Collaboration Networks (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf) — Agent 影响力驱动的协作进化
