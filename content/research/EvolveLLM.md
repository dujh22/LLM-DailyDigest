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

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI / 走向真正的 ASI》承载仓库，含开题材料与综述《大语言模型复杂推理的自我进化机制：研究综述与前沿展望》。
- [Daily-Work-Log-Public](https://github.com/dujh22/Daily-Work-Log-Public) — 公开个人工作日志：每日日志、LLM 学习笔记、工作记录、获奖与运动（中文撰写、英文 kebab-case 目录）。
- [Daily-Work-Log-Private](https://github.com/dujh22/Daily-Work-Log-Private) — 私有科研知识库 / 个人科研操作系统，以 AI 学术研究（LLM 逻辑推理、自进化、评估、RLVR、蒸馏、推理时计算）为主线，含草稿、方法论 SOP 与沟通记录。
- [Dujinhua-wiki](https://github.com/dujh22/Dujinhua-wiki) — 基于 MkDocs 的个人知识库 wiki。
- [Dujinhua-wiki-Source](https://github.com/dujh22/Dujinhua-wiki-Source) — 上述 wiki 的源码仓库。
- [MetaEvaluation](https://github.com/dujh22/MetaEvaluation) — 元评测（meta-evaluation）相关仓库。
- [AutoLLM](https://github.com/dujh22/AutoLLM) — LLM 自动化相关仓库。

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
1. **可审计改进闭环**：递归改进应记录知识状态与失败归因，以受控单变量实验、独立复核和跨周期评估决定合并；即时收益不能代表后续更新后仍有效。
   - [GLM-5.5：多模型后训练汇流式RSI](../../updates/2026-11-25/#glm-5-5-rsi) · 2026-11-25
   - [E2L：梯度对齐经验演化](../../updates/2026-11-25/#e2l) · 2026-11-25
   - [TrainExplorer：规划解耦式后训练探索](../../updates/2026-11-17/#trainexplorer) · 2026-11-17
   - [Post-Training RSI：后训练全栈递归](../../updates/2026-11-17/#post-training-rsi) · 2026-11-17
   - [No Second Run：预训练RSI炼出801-30B-A3B模型](../../updates/2026-11-14/#no-second-run-rsi-801-30b-a3b) · 2026-11-14
   - [Third Eye：递归自我改进的长期效用评估](../../updates/2026-11-12/#third-eye) · 2026-11-12
   - [百度披露 ERNIE Evolve 递归自我改进进展，已用于文心 5.5 Flash 研发](../../updates/2026-11-12/#ernie-evolve-5-5-flash) · 2026-11-12
   - [Recursa：递归自我改进的基础模型系统](../../updates/2026-11-06/#recursa) · 2026-11-06
   - [CARE：面向生产客服智能体的证据驱动递归自我改进](../../updates/2026-11-06/#care) · 2026-11-06
   - [RSI-Master：受控实验驱动的自主模型改进](../../updates/2026-10-30/#rsi-master) · 2026-10-30
   - [RKI：状态感知的递归知识改进框架](../../updates/2026-10-29/#rki) · 2026-10-29
2. **自适应任务刷新**：零数据自训练宜生成可独立验证且位于当前未知边界的任务，并按有效优势与正确率刷新题池；只增加同质样本容易耗尽信号。
   - [The Frontier Must Grow：验证前沿扩展训练](../../updates/2026-11-17/#the-frontier-must-grow) · 2026-11-17
   - [A-RSI：零数据多模态递归自我改进的自适应任务刷新](../../updates/2026-10-31/#a-rsi) · 2026-10-31
3. **奖励准则共演化**：开放任务中固定或仅看结果的奖励容易失真；应让准则随策略演化，用独立标签校准置信度，并审计类别盲点与中间错误固化。
   - [SRO：保真度诊断与投影解耦](../../updates/2026-11-24/#sro) · 2026-11-24
   - [自幻觉记忆：后训练固化错误事实](../../updates/2026-11-23/#item-49) · 2026-11-23
   - [RLCDR：校准式决策奖励](../../updates/2026-11-20/#rlcdr) · 2026-11-20
   - [盲点迁移：评判偏见类别泛化](../../updates/2026-11-20/#item-65) · 2026-11-20
   - [临床AI评估即干预](../../updates/2026-11-16/#item-18) · 2026-11-16
   - [EmoReward：情感视频生成的自进化奖励校准](../../updates/2026-11-06/#emoreward) · 2026-11-06
   - [RcRL：利用生成—验证鸿沟改进开放域强化学习](../../updates/2026-11-05/#rcrl) · 2026-11-05
   - [Self-Evolving Rubrics：自进化准则驱动强化学习](../../updates/2026-11-02/#self-evolving-rubrics) · 2026-11-02
   - [RACE：策略与评分准则的奖励自适应协同演化](../../updates/2026-10-30/#race) · 2026-10-30
4. **跨任务更新隔离**：多任务自迭代中，共享参数会将局部更新耦合成策略坍缩或遗忘；宜先用适配器路由或并行学习器隔离，再受控合并。
   - [CSPD：可组合软提示蒸馏](../../updates/2026-11-25/#cspd) · 2026-11-25
   - [DiVE：小模型多样性递归改进](../../updates/2026-11-24/#dive) · 2026-11-24
   - [奖励范围之外：多语言后训练中的能力漂移](../../updates/2026-11-14/#item-46) · 2026-11-14
   - [Recursa：递归自我改进的基础模型系统](../../updates/2026-11-06/#recursa) · 2026-11-06
   - [跨任务耦合驱动无监督 RLVR 策略坍缩](../../updates/2026-10-29/#rlvr) · 2026-10-29
   - [CaLLM：基于非参数适配器路由的持续适应](../../updates/2026-10-29/#callm) · 2026-10-29
5. **巩固与能力回放**：持续更新前后要用多接口区分读出错配与真实表征漂移；以行为门控、低曲率更新、历史预测或基础回放约束晋升，避免奖励外能力退化。
   - [三接口持续学习诊断](../../updates/2026-11-25/#item-109) · 2026-11-25
   - [InstructReplay：自答回放保留通用能力](../../updates/2026-11-25/#instructreplay) · 2026-11-25
   - [CurvDelta：低曲率约束式学习遗忘](../../updates/2026-11-20/#curvdelta) · 2026-11-20
   - [Model Annealing：历史自我回顾巩固](../../updates/2026-11-16/#model-annealing) · 2026-11-16
   - [G-CAST：治理式持续自训练](../../updates/2026-11-16/#g-cast) · 2026-11-16
   - [RL训练：大模型能力漂移](../../updates/2026-11-15/#item-1) · 2026-11-15
   - [奖励范围之外：多语言后训练中的能力漂移](../../updates/2026-11-14/#item-46) · 2026-11-14
   - [FireGate：持续强化学习微调前的行为变化界定](../../updates/2026-11-12/#firegate) · 2026-11-12
   - [特征干扰视角下的 SFT 普遍能力退化理论与 AEGIS 损失](../../updates/2026-11-06/#sft-aegis) · 2026-11-06
   - [在策略蒸馏用于强化学习后能力巩固的泛化局限](../../updates/2026-11-06/#item-14) · 2026-11-06
   - [Google「睡眠框架」缓解大模型灾难性遗忘](../../updates/2026-10-31/#google) · 2026-10-31
   - [Google 为大模型引入「睡眠」机制，缓解灾难性遗忘](../../updates/2026-10-30/#google) · 2026-10-30
6. **合成数据边界**：递归回用合成数据会先侵蚀稀有知识并造成表征漂移；除多维审计和注入经核验的外部信息外，可在动力学平稳时用单代条件响应预警坍缩。
   - [单代校准预测稀有模式坍缩](../../updates/2026-11-25/#item-90) · 2026-11-25
   - [自消费训练：稀疏特征解释性退化](../../updates/2026-11-18/#item-59) · 2026-11-18
   - [自训练中的有序 Rényi 熵交叉：丰富度不等于均匀度](../../updates/2026-11-12/#r-nyi) · 2026-11-12
   - [谁为模型复制的知识买单？Rogers 悖论下的模型坍缩](../../updates/2026-11-05/#rogers) · 2026-11-05
   - [重新审视合成数据预预训练](../../updates/2026-10-30/#item-52) · 2026-10-30
7. **选择性轨迹蒸馏**：蒸馏与自主后训练宜只监督可教前缀、显著分歧或高质量决策，并用技能上下文过滤成功轨迹中的坏习惯；全量语义对齐未必最优，仍需能力回放。
   - [AutoMaster：技能引导式自主后训练](../../updates/2026-11-20/#automaster) · 2026-11-20
   - [RSI-Prime：决策级损失掩码训练](../../updates/2026-11-19/#rsi-prime) · 2026-11-19
   - [B-OPSD：自生成简报蒸馏](../../updates/2026-11-17/#b-opsd) · 2026-11-17
   - [P²-MOPD：参数先验加速多教师在策略蒸馏](../../updates/2026-11-12/#p-mopd) · 2026-11-12
   - [推测式自蒸馏实现高效知识内化](../../updates/2026-11-12/#item-114) · 2026-11-12
   - [BOPD：自举式在策略蒸馏](../../updates/2026-11-12/#bopd) · 2026-11-12
   - [TOPSD：从可教前缀进行多语言推理蒸馏](../../updates/2026-11-08/#topsd) · 2026-11-08
   - [Shuffled OPSD：语义一致性何时损害在策略自蒸馏](../../updates/2026-11-06/#shuffled-opsd) · 2026-11-06
   - [在策略蒸馏用于强化学习后能力巩固的泛化局限](../../updates/2026-11-06/#item-14) · 2026-11-06
   - [O³PD：仅基于排序的在策略蒸馏](../../updates/2026-11-04/#o-pd) · 2026-11-04
   - [Youtu-Parsing-Omni：统一编码器与模式的全模态解析器](../../updates/2026-10-31/#youtu-parsing-omni) · 2026-10-31
   - [RISE：交错 RLVR 与在策略蒸馏实现递归自我改进](../../updates/2026-10-31/#rise-rlvr) · 2026-10-31
8. **选择性测试时更新**：推理与跨会话适应宜冻结主干，把查询相关更新写入快速权重、持久潜状态或固定容量适配器；临时干预应先验证再版本化。
   - [CLAM：单次前向权重记忆固化](../../updates/2026-11-17/#clam) · 2026-11-17
   - [Recursive SALM：基于持久潜在状态的预训练语言模型适配](../../updates/2026-11-14/#recursive-salm) · 2026-11-14
   - [NCP：验证器引导的权重空间控制策略优化](../../updates/2026-11-12/#ncp) · 2026-11-12
   - [LatentWeave：面向多模态推理的测试时潜变量优化](../../updates/2026-10-30/#latentweave) · 2026-10-30
   - [Select-TTT：查询条件化的选择性快速权重更新](../../updates/2026-10-29/#select-ttt) · 2026-10-29
9. **验证驱动测试扩展**：测试时扩展不能把多数共识等同正确性；优先用独立检查器、校正奖励或易验证任务，并让后续尝试继承已验证推理，避免独立采样锁定早期错误。
   - [TT-RSI：测试时递归自我改进](../../updates/2026-11-25/#tt-rsi) · 2026-11-25
   - [STONE：踏脚石式无标签自蒸馏](../../updates/2026-11-17/#stone) · 2026-11-17
   - [TRUER：面向测试时强化学习的错误感知奖励校正](../../updates/2026-11-12/#truer) · 2026-11-12
   - [实时捕获并纠正 LLM 推理错误](../../updates/2026-11-12/#llm-2) · 2026-11-12
   - [多数投票伪标签在测试时强化学习中的可靠性](../../updates/2026-11-12/#item-176) · 2026-11-12
   - [核定律预测多数投票测试时强化学习的答案锁定](../../updates/2026-11-12/#item-143) · 2026-11-12
   - [Test-Time Self-Play：无需验证器的测试时扩展](../../updates/2026-11-06/#test-time-self-play) · 2026-11-06
   - [验证器引导的自一致性：不完美生成器与验证器下的测试时推理](../../updates/2026-11-06/#item-32) · 2026-11-06
10. **外部语料自主学习**：面对长篇外部语料，仅扩大上下文不足以形成能力；用导航检索配合细粒度过程奖励，才能训练知识定位、吸收与迁移。
    - [强化学习激励大语言模型从长篇教材中自我学习](../../updates/2026-11-13/#item-7) · 2026-11-13
    - [强化学习激励大语言模型自主学习长篇教材](../../updates/2026-10-30/#item-61) · 2026-10-30
11. **生产失败反馈闭环**：真实交互反馈应先判别任务是否真正成功，再做故障归因；每次在策略更新须受累积能力契约和分阶段验证约束，避免噪声与新需求破坏旧行为。
    - [FinEvo：同模自博弈递归改进](../../updates/2026-11-24/#finevo) · 2026-11-24
    - [Learning through Discernment：辨别式反馈学习](../../updates/2026-11-19/#learning-through-discernment) · 2026-11-19
    - [G-CAST：治理式持续自训练](../../updates/2026-11-16/#g-cast) · 2026-11-16
    - [DriveFoundry：数据与模型协同演化的自动驾驶闭环框架](../../updates/2026-11-12/#drivefoundry) · 2026-11-12
    - [CARE：面向生产客服智能体的证据驱动递归自我改进](../../updates/2026-11-06/#care) · 2026-11-06
    - [百度搜索通过在线反馈闭环实现递归自我进化](../../updates/2026-11-01/#item-1) · 2026-11-01
12. **多模态可靠自教学**：无标签多模态自教学应估计各生成链的可靠性，或采用扰动—验证—修复闭环，避免多数投票和单向伪轨迹放大错误。
    - [PROVE：自博弈视觉-语言验证器的组合理解训练](../../updates/2026-11-06/#prove) · 2026-11-06
    - [Prism：统一多模态模型的双向自教学](../../updates/2026-11-06/#prism) · 2026-11-06
    - [Timbre：面向无标签多模态测试时强化学习的可靠性感知调和共识](../../updates/2026-10-30/#timbre) · 2026-10-30
13. **权重编辑需可回滚**：直接改写少量权重可低成本固化外部能力或修复故障，但收益可能来自数值痕迹或偶然搜索；应报告数值格式、做舍入对照与独立验证，并保留回滚版本。
    - [Weight Coding：智能体直接编辑模型权重](../../updates/2026-11-25/#weight-coding) · 2026-11-25
    - [SELFWRITE：无梯度自写权重编辑](../../updates/2026-11-25/#selfwrite) · 2026-11-25
    - [Self-WSP：权重空间自我编程](../../updates/2026-11-24/#self-wsp) · 2026-11-24
    - [Weight-Space Programming：无梯度写入ICL](../../updates/2026-11-23/#weight-space-programming-icl) · 2026-11-23
    - [Keel：智能体改权消除视觉循环](../../updates/2026-11-20/#keel) · 2026-11-20
    - [BaseRSI：免训练脚手架内化](../../updates/2026-11-20/#basersi) · 2026-11-20
    - [Weight Space Programming：低位痕迹引导权重修复](../../updates/2026-11-19/#weight-space-programming) · 2026-11-19
    - [Self-Rewriting：无梯度自改权重](../../updates/2026-11-18/#self-rewriting) · 2026-11-18
    - [Tree-Ising：基于位级 Ising 编辑的语言模型修复](../../updates/2026-11-12/#tree-ising-ising) · 2026-11-12
    - [权重空间编程的能力、泛化与局限](../../updates/2026-11-12/#item-192) · 2026-11-12
    - [机制干预：AI动态改写Transformer架构实现自我改进](../../updates/2026-11-12/#ai-transformer) · 2026-11-12
14. **生命周期可监控性**：能力提升、架构变更和自生成数据蒸馏会改变思维链与特征的可观测性；不能沿用旧监控器，须跨版本重测规避与解释失效。
    - [自消费训练：稀疏特征解释性退化](../../updates/2026-11-18/#item-59) · 2026-11-18
    - [OpenAI：模型生命周期因素如何影响 CoT 可监控性](../../updates/2026-11-12/#openai-cot) · 2026-11-12
15. **模型脚手架共演化**：智能体改进不应只更新权重或固定脚手架；应联合迭代模型、训练数据与执行框架，并用升级后系统的反馈继续评估，稳定增益再内化。
    - [CoEvoBench：模型与脚手架协同演化](../../updates/2026-11-23/#coevobench) · 2026-11-23
    - [Piccolo：模型数据协同自进化](../../updates/2026-11-20/#piccolo) · 2026-11-20
    - [Evo²：权重与Harness协同进化](../../updates/2026-11-20/#evo-harness) · 2026-11-20
<!-- experience-seen: 2026-10-29/35b-apex-35b-v1-0 2026-10-29/callm 2026-10-29/item-35 2026-10-29/oxr-1-3b-rsi 2026-10-29/rki 2026-10-29/rlvr 2026-10-29/select-ttt 2026-10-30/google 2026-10-30/item-52 2026-10-30/item-61 2026-10-30/latentweave 2026-10-30/mid-training 2026-10-30/race 2026-10-30/rsi-master 2026-10-30/timbre 2026-10-31/a-rsi 2026-10-31/google 2026-10-31/rise-rlvr 2026-10-31/youtu-parsing-omni 2026-11-01/item-1 2026-11-01/item-13 2026-11-02/self-evolving-rubrics 2026-11-03/astra-qwen 2026-11-04/o-pd 2026-11-05/801-30b-rsi 2026-11-05/rcrl 2026-11-05/rogers 2026-11-06/care 2026-11-06/compressionbench-llm 2026-11-06/emoreward 2026-11-06/item-116 2026-11-06/item-14 2026-11-06/item-22 2026-11-06/item-32 2026-11-06/prism 2026-11-06/prove 2026-11-06/recursa 2026-11-06/sft-aegis 2026-11-06/shuffled-opsd 2026-11-06/test-time-self-play 2026-11-06/weightloop 2026-11-08/topsd 2026-11-12/ai-transformer 2026-11-12/bopd 2026-11-12/drivefoundry 2026-11-12/ernie-evolve-5-5-flash 2026-11-12/firegate 2026-11-12/item-114 2026-11-12/item-143 2026-11-12/item-176 2026-11-12/item-192 2026-11-12/llm-10 2026-11-12/llm-2 2026-11-12/looped-ced-kv 2026-11-12/ncp 2026-11-12/openai-cot 2026-11-12/p-mopd 2026-11-12/r-nyi 2026-11-12/rsi 2026-11-12/third-eye 2026-11-12/tree-ising-ising 2026-11-12/truer 2026-11-13/item-14 2026-11-13/item-7 2026-11-14/item-46 2026-11-14/no-second-run-rsi-801-30b-a3b 2026-11-14/recursive-salm 2026-11-15/item-1 2026-11-16/g-cast 2026-11-16/item-18 2026-11-16/model-annealing 2026-11-17/b-opsd 2026-11-17/clam 2026-11-17/post-training-rsi 2026-11-17/stone 2026-11-17/the-frontier-must-grow 2026-11-17/trainexplorer 2026-11-18/item-59 2026-11-18/self-rewriting 2026-11-19/item-48 2026-11-19/learning-through-discernment 2026-11-19/rsi-prime 2026-11-19/toaster 2026-11-19/weight-space-programming 2026-11-20/automaster 2026-11-20/basersi 2026-11-20/curvdelta 2026-11-20/evo-harness 2026-11-20/item-65 2026-11-20/keel 2026-11-20/piccolo 2026-11-20/rlcdr 2026-11-20/self-replicating-language-models 2026-11-23/coevobench 2026-11-23/item-49 2026-11-23/openai-ai 2026-11-23/structure-over-scale 2026-11-23/weight-space-programming-icl 2026-11-24/dive 2026-11-24/finevo 2026-11-24/pbpt 2026-11-24/self-wsp 2026-11-24/sro 2026-11-25/cspd 2026-11-25/e2l 2026-11-25/elgo 2026-11-25/glm-5-5-rsi 2026-11-25/instructreplay 2026-11-25/item-109 2026-11-25/item-90 2026-11-25/selfwrite 2026-11-25/tt-rsi 2026-11-25/weight-coding -->
<!-- research-experience:end -->

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
