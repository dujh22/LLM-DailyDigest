+++
title = 'JevEvolve'
proposer = '杜晋华'
since = '2026-09-24'
date = 2026-09-24T00:00:00+08:00
draft = false
toc = true
+++

# JevEvolve

> 研究方向：**快决策模型自进化**——以 Jev 为代表的低延迟结构化判断 / 决策模型，及其在智能体中"快决策—慢思考"分工的持续进化。

## 研究范畴

快决策模型（Jev-style fast decision models）不生成开放式文本，而是对有限候选（动作、选项、路由目标）直接返回评分或概率，把单次决策压到百毫秒乃至几十毫秒级、成本压到普通推理调用的百分之一以下。本方向关注这类模型自身及其使用方式的自进化：如何从智能体交互日志中持续校准判断质量、如何自动学习"哪些决策交给快模型、哪些升级到慢思考推理模型"的路由边界、如何在动作选择 / 工具路由 / 上下文压缩 / 风险检查 / 结果评判等高频环节嵌入并迭代。社区关注的核心问题包括：跳过自回归 Decode、直接利用 Prefill 隐状态打分的推理脚手架设计，快决策与实时环境闭环（观察—决策—执行）的时延预算分配，以及"不生成候选外内容"与"判断正确"之间的评估鸿沟。

## 研究挑战

- 评分稳定性与任务泛化：低幻觉表述不等于高准确率，需与强模型评判独立对标。
- 候选集构造是新瓶颈：动作空间的枚举、剪枝与动态生成决定了判断上限。
- 快 / 慢分工的路由边界如何从反馈中自动学习，而非手工规则固化。
- 无开放文本输出导致可解释性与可调试性差，错误决策难以归因。
- 判断模型的持续校准：交互日志噪声大、奖励信号稀疏，易累积系统性偏差。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。
- [LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest) — 本站日报系统，持续追踪快决策模型热点并按本研究方向聚合条目。

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
1. **闭集直接评分**：输出可结构化时优先单次前向直接评分；候选空间过大则按查询证据收缩菜单，高频判断可显著降低延迟和成本。
   - [Prefill1：固定前缀单词元判决](../../updates/2026-11-25/#prefill1) · 2026-11-25
   - [EEG-Jev：单次前向统一脑电决策](../../updates/2026-11-25/#eeg-jev) · 2026-11-25
   - [Decision Models：类型化决策能力评测](../../updates/2026-11-25/#decision-models) · 2026-11-25
   - [MolReJev：上下文分子候选评分](../../updates/2026-11-24/#molrejev) · 2026-11-24
   - [多语言情绪分类：决策模型零样本评测](../../updates/2026-11-23/#item-26) · 2026-11-23
   - [交通类型化决策模型：结构化低成本决策](../../updates/2026-11-19/#item-54) · 2026-11-19
   - [决策模型：低成本联络中心判别](../../updates/2026-11-19/#item-53) · 2026-11-19
   - [Karpo Decision：单次前向并行决策](../../updates/2026-11-18/#karpo-decision) · 2026-11-18
   - [AdaMenu：查询自适应候选菜单](../../updates/2026-11-17/#adamenu) · 2026-11-17
   - [UltraBERT-JEV：单次前向候选决策](../../updates/2026-11-16/#ultrabert-jev) · 2026-11-16
   - [小型决策模型在消费级 GPU 上规模化发现内存安全漏洞](../../updates/2026-11-14/#gpu) · 2026-11-14
   - [Google 发布多模态决策模型 Gemini Decision 1](../../updates/2026-11-13/#google-gemini-decision-1) · 2026-11-13
   - [TrialJev：单次前向传播的开放权重临床试验资格评分器](../../updates/2026-11-12/#trialjev) · 2026-11-12
   - [Google 发布 Gemini Decisions API：单次前向批量判断千题](../../updates/2026-11-12/#google-gemini-decisions-api) · 2026-11-12
   - [Drex：迈向基础决策模型](../../updates/2026-11-08/#drex) · 2026-11-08
   - [ECGJev：面向12导联心电图解读的条件选项评分框架](../../updates/2026-11-06/#ecgjev-12) · 2026-11-06
   - [EarthJev：面向 Sentinel-2 土地覆盖问答的校准式非生成模型](../../updates/2026-11-06/#earthjev-sentinel-2) · 2026-11-06
   - [Decision Models：可扩展且保留人类差异的经济代理](../../updates/2026-11-06/#decision-models) · 2026-11-06
   - [开放视觉语言模型在放射学任务中的零样本 System 1 决策评测](../../updates/2026-11-03/#system-1) · 2026-11-03
   - [面壁智能开源 MiniCPM-OCR 高效可信文档解析模型](../../updates/2026-10-30/#minicpm-ocr) · 2026-10-30
   - [决策模型作为幻觉检测评判器](../../updates/2026-10-29/#item-65) · 2026-10-29
   - [GUI-JEPA：基于候选条件潜变量的移动端 GUI 智能体快速动作策略](../../updates/2026-10-29/#gui-jepa-gui) · 2026-10-29
2. **共享状态摊销**：同一上下文含多候选或多问题时，应共享预填充与中间表征并精确分叉；候选间交互仅在任务依赖关系且经定向训练时启用。
   - [Voyag：多意图与执行关系联合判定](../../updates/2026-11-25/#voyag) · 2026-11-25
   - [Tree Attention：消除决策顺序敏感性](../../updates/2026-11-25/#tree-attention) · 2026-11-25
   - [决策模型：候选比较的任务边界](../../updates/2026-11-17/#item-44) · 2026-11-17
   - [小头部也能强决策：Typed-Decision 模型受控研究](../../updates/2026-11-14/#typed-decision) · 2026-11-14
   - [Google 发布 Gemini Decisions API：单次前向批量判断千题](../../updates/2026-11-12/#google-gemini-decisions-api) · 2026-11-12
   - [Flide：以精确状态分叉加速决策推理](../../updates/2026-11-12/#flide) · 2026-11-12
   - [Q64：共享上下文候选评分与联合适配读出网络](../../updates/2026-11-06/#q64) · 2026-11-06
   - [Glance：生成器即重排器](../../updates/2026-10-30/#glance) · 2026-10-30
3. **轻量读出与蒸馏**：冻结或复用生成骨干，再训练轻量读出或蒸馏多教师软分布，可把推理收益压入单遍评分并减少模型驻留。
   - [GLiDE：推理蒸馏单遍决策](../../updates/2026-11-20/#glide) · 2026-11-20
   - [System 1决策模型：冻结编码器对比答题](../../updates/2026-11-19/#system-1) · 2026-11-19
   - [Marimba：冻结ASR特征的语音决策](../../updates/2026-11-16/#marimba-asr) · 2026-11-16
   - [小头部也能强决策：Typed-Decision 模型受控研究](../../updates/2026-11-14/#typed-decision) · 2026-11-14
   - [TrialJev：单次前向传播的开放权重临床试验资格评分器](../../updates/2026-11-12/#trialjev) · 2026-11-12
   - [ECGJev：面向12导联心电图解读的条件选项评分框架](../../updates/2026-11-06/#ecgjev-12) · 2026-11-06
   - [Zuse：面向欧洲语言的决策模型](../../updates/2026-11-05/#zuse) · 2026-11-05
   - [Glance：生成器即重排器](../../updates/2026-10-30/#glance) · 2026-10-30
   - [GUI-JEPA：基于候选条件潜变量的移动端 GUI 智能体快速动作策略](../../updates/2026-10-29/#gui-jepa-gui) · 2026-10-29
4. **逐域校准验证**：准确率与校准随任务和部署分布变化；阈值须在真实日志上按方言、字段和候选数分层重测，不能沿用平均指标或考试集结论。
   - [Lost in Translation：多语言决策校准](../../updates/2026-11-26/#lost-in-translation) · 2026-11-26
   - [Jev分诊评测：概率式急诊早识别](../../updates/2026-11-25/#jev-2) · 2026-11-25
   - [OmniDecisionBench：多模态决策可靠性评测](../../updates/2026-11-24/#omnidecisionbench) · 2026-11-24
   - [多语言情绪分类：决策模型零样本评测](../../updates/2026-11-23/#item-26) · 2026-11-23
   - [Sirius-Tiamat：决策保持式压缩评测](../../updates/2026-11-20/#sirius-tiamat) · 2026-11-20
   - [Rigel-Ladon：选项数准确率定律](../../updates/2026-11-20/#rigel-ladon) · 2026-11-20
   - [交通类型化决策模型：结构化低成本决策](../../updates/2026-11-19/#item-54) · 2026-11-19
   - [决策模型：低成本联络中心判别](../../updates/2026-11-19/#item-53) · 2026-11-19
   - [决策模型：带置信度的临床字段抽取](../../updates/2026-11-17/#item-86) · 2026-11-17
   - [Laya 类型决策模型置信度再校准实操指南](../../updates/2026-11-14/#laya) · 2026-11-14
   - [Jev 是优秀的多语言评判模型吗？](../../updates/2026-11-13/#jev) · 2026-11-13
   - [Jev式System 1决策模型的置信度与可解释性审计](../../updates/2026-11-12/#jev-system-1) · 2026-11-12
   - [Jev 阿拉伯语任务与方言能力评测](../../updates/2026-11-12/#jev) · 2026-11-12
   - [结构化临床记忆提升概率决策表现：Jev 合成评测](../../updates/2026-11-06/#jev) · 2026-11-06
   - [Zuse：面向欧洲语言的决策模型](../../updates/2026-11-05/#zuse) · 2026-11-05
   - [开放视觉语言模型在放射学任务中的零样本 System 1 决策评测](../../updates/2026-11-03/#system-1) · 2026-11-03
   - [Decision 与 System One 模型的风湿病学准确率和校准评测](../../updates/2026-10-30/#decision-system-one) · 2026-10-30
   - [决策模型作为幻觉检测评判器](../../updates/2026-10-29/#item-65) · 2026-10-29
5. **按需快慢路由**：快慢路由不应固定：用校准置信度、停滞行为、中间状态与续推净收益决定升级，并按任务成功、轨迹长度、成本和延迟联合优化。
   - [JevAgentHarness：Jev嵌入式快速决策](../../updates/2026-11-25/#jevagentharness-jev) · 2026-11-25
   - [层级执行控制：中间状态驱动计算分配](../../updates/2026-11-25/#item-128) · 2026-11-25
   - [ADAPT：成本感知求助后训练](../../updates/2026-11-24/#adapt) · 2026-11-24
   - [LoopRoute：循环触发式策略路由](../../updates/2026-11-20/#looproute) · 2026-11-20
   - [Vanguard：截图感知式草稿判别](../../updates/2026-11-19/#vanguard) · 2026-11-19
   - [FLCVA：全账本反事实推理审计](../../updates/2026-11-19/#flcva) · 2026-11-19
   - [AnyS1：技能编译式快速决策](../../updates/2026-11-19/#anys1) · 2026-11-19
   - [LuthorSQL：单遍置信路由](../../updates/2026-11-16/#luthorsql) · 2026-11-16
   - [小语言模型能力路由：容量与提示优化对质量和效率的影响](../../updates/2026-11-14/#item-30) · 2026-11-14
   - [思考的价值：混合决策模型学习何时推理](../../updates/2026-11-14/#item-22) · 2026-11-14
   - [PISA-E：面向提示自适应与成本感知推理的集成路由](../../updates/2026-11-13/#pisa-e) · 2026-11-13
   - [Scout 路由：用小模型预填充预测任务成功率与 Token 成本](../../updates/2026-11-12/#scout-token) · 2026-11-12
   - [AgentBaton：长程智能体任务中的高效模型接力](../../updates/2026-11-12/#agentbaton) · 2026-11-12
   - [StartLux-Decision：按需推理与概率校准](../../updates/2026-11-06/#startlux-decision) · 2026-11-06
   - [Route Anything：通用人工智能系统的模型与策略路由](../../updates/2026-11-05/#route-anything) · 2026-11-05
   - [实时全双工语音模型的后训练专家路由](../../updates/2026-11-03/#item-41) · 2026-11-03
   - [System-1 门控 System-2：以条件交互提升 AGI 扩展效率](../../updates/2026-10-30/#system-1-system-2-agi) · 2026-10-30
   - [单一紧凑解码器联合决策辅助时机与记忆提示生成](../../updates/2026-10-30/#item-31) · 2026-10-30
6. **异步分层控制**：实时智能体应让低延迟控制持续运行，仅在边界事件触发高层规划，并以共享预算协调两层，避免等待慢推理。
   - [System-One RSI：引导练习式肌肉记忆](../../updates/2026-11-20/#system-one-rsi) · 2026-11-20
   - [DRIFT：可拆卸语言推理驾驶](../../updates/2026-11-20/#drift) · 2026-11-20
   - [JevRSI：递归改进决策脚手架](../../updates/2026-11-18/#jevrsi) · 2026-11-18
   - [Omni-JEV：文本与双流语音交互决策](../../updates/2026-11-12/#omni-jev) · 2026-11-12
   - [REA：异步脑-小脑控制的路由式具身智能体运行时](../../updates/2026-11-03/#rea) · 2026-11-03
   - [TaskFrame：连接任务级规划与帧级控制的游戏智能体框架](../../updates/2026-10-30/#taskframe) · 2026-10-30
7. **后果预测决策**：安全关键动作不宜只做静态分类；先用世界模型预测各候选的短期后果再评分，可在保持低延迟时降低事故风险。
   - [Jev-AD：基于语言世界模型的安全自动驾驶](../../updates/2026-11-06/#jev-ad) · 2026-11-06
8. **决策平面强化**：动作集合已知时可直接优化选项概率；稀疏奖励可由轨迹评判或通用决策器的逐步概率补充信用，但作为奖励前后须复验高置信安全盲区。
   - [DM-PRM：决策模型零样本过程奖励](../../updates/2026-11-23/#dm-prm) · 2026-11-23
   - [Jev-as-a-Reward：概率安全评判验证](../../updates/2026-11-18/#jev-as-a-reward) · 2026-11-18
   - [行动者、评判者还是教师？长时程智能体中的决策模型](../../updates/2026-11-14/#item-11) · 2026-11-14
   - [RLiD：在决策平面强化学习语言智能体](../../updates/2026-11-06/#rlid) · 2026-11-06
9. **呈现与注入鲁棒**：答案表征应保留集合、顺序或距离等真实结构，同时隔离展示顺序、标签、修辞和追加文本；用结构匹配编码与来源隔离复判抵抗操控。
   - [Tree Attention：消除决策顺序敏感性](../../updates/2026-11-25/#tree-attention) · 2026-11-25
   - [DeciForm：答案空间结构感知决策](../../updates/2026-11-25/#deciform) · 2026-11-25
   - [Antares-Smaug：未见攻击泛化评测](../../updates/2026-11-25/#antares-smaug) · 2026-11-25
   - [LEVER：事实不变决策操纵](../../updates/2026-11-23/#lever) · 2026-11-23
   - [MM-SystemOneBias：多模态决策偏差评测](../../updates/2026-11-20/#mm-systemonebias) · 2026-11-20
   - [S1-Evo：面向类型化 System-1 决策模型的证据竞争攻击](../../updates/2026-11-14/#s1-evo-system-1) · 2026-11-14
   - [Maya a1 非自回归决策模型的选项顺序敏感性](../../updates/2026-11-12/#maya-a1) · 2026-11-12
   - [Jev式System 1决策模型的置信度与可解释性审计](../../updates/2026-11-12/#jev-system-1) · 2026-11-12
   - [数字助推能否操控快速非生成式决策智能体？](../../updates/2026-11-12/#item-197) · 2026-11-12
   - [标签措辞增强提升陌生词路由，但对缩写与代码无效](../../updates/2026-11-08/#item-27) · 2026-11-08
   - [Drex：迈向基础决策模型](../../updates/2026-11-08/#drex) · 2026-11-08
   - [JevBreak：固定答案集无法阻止决策操控](../../updates/2026-11-06/#jevbreak) · 2026-11-06
   - [主观文本评估中类型化决策模型的呈现敏感性](../../updates/2026-11-05/#item-25) · 2026-11-05
10. **混合语料保通用**：窄域微调及事后参数合并都可能造成能力坍缩或冲突；持续进化宜优先混合联合训练，并分别监控域内、通用与真实决策准确率。
    - [Altair-Nidhogg：单通决策模型合并审计](../../updates/2026-11-23/#altair-nidhogg) · 2026-11-23
    - [Piccolo：模型数据协同自进化](../../updates/2026-11-20/#piccolo) · 2026-11-20
    - [金融小型决策模型：专业化坍缩与混合语料修复](../../updates/2026-11-06/#item-102) · 2026-11-06
11. **显式边界与拒答**：运行时风险门应按真实错误成本设置阈值，并把执行、追问和拒答建模为统一可比较动作，以兼顾风险召回、信息增益和误拦截。
    - [Jev分诊评测：概率式急诊早识别](../../updates/2026-11-25/#jev-2) · 2026-11-25
    - [CATWAY：成本敏感三路决策](../../updates/2026-11-25/#catway) · 2026-11-25
    - [SO-Arena：能力可靠性双维评测](../../updates/2026-11-23/#so-arena) · 2026-11-23
    - [决策模型：低成本联络中心判别](../../updates/2026-11-19/#item-53) · 2026-11-19
    - [Microsoft-Decision-1.1：校准置信度与弃权](../../updates/2026-11-18/#microsoft-decision-1-1) · 2026-11-18
    - [ZeroPoint：轻量级能量决策模型](../../updates/2026-11-12/#zeropoint) · 2026-11-12
    - [决策模型充当编程智能体策略门：显式边界提升风险检测并减少误报](../../updates/2026-11-06/#item-131) · 2026-11-06
12. **结构化语义输入**：记忆应按决策效用检索，长期任务按事件谱系保留时序证据并抽象程序；标签、原子问题、工具返回及变长标识须显式建模语义、长度与内容。
    - [Procedure Memory：情节驱动的程序记忆](../../updates/2026-11-26/#procedure-memory) · 2026-11-26
    - [Needwise：免生成需求级决策](../../updates/2026-11-25/#needwise) · 2026-11-25
    - [DKnown-Jev-2：篇章级答案证据分类](../../updates/2026-11-25/#dknown-jev-2) · 2026-11-25
    - [Jetriever：效用驱动记忆检索](../../updates/2026-11-18/#jetriever) · 2026-11-18
    - [TDM-Gauntlet：类型决策替换微调分类器](../../updates/2026-11-17/#tdm-gauntlet) · 2026-11-17
    - [S1Mal：原子问答与嵌入集成](../../updates/2026-11-17/#s1mal) · 2026-11-17
    - [Beyond Plain MCP：代码模式压缩工具上下文](../../updates/2026-11-17/#beyond-plain-mcp) · 2026-11-17
    - [标签措辞增强提升陌生词路由，但对缩写与代码无效](../../updates/2026-11-08/#item-27) · 2026-11-08
    - [结构化临床记忆提升概率决策表现：Jev 合成评测](../../updates/2026-11-06/#jev) · 2026-11-06
    - [JevRec：生成式推荐的变长语言编码与决策建模](../../updates/2026-10-29/#jevrec) · 2026-10-29
13. **系统级能力评测**：不能只报单题准确率；还应测缺失答案、联合分布、证据定位、决策稳定性及运行栈噪声，否则会掩盖系统性错误。
    - [S1Arena-MM：多模态快慢决策评测](../../updates/2026-11-25/#s1arena-mm) · 2026-11-25
    - [JevBench：无标签变形一致性测试](../../updates/2026-11-25/#jevbench) · 2026-11-25
    - [GeoDecisions：空间感知与地理偏差评测](../../updates/2026-11-25/#geodecisions) · 2026-11-25
    - [EEGJev：单遍候选答案决策](../../updates/2026-11-25/#eegjev) · 2026-11-25
    - [OmniDecisionBench：多模态决策可靠性评测](../../updates/2026-11-24/#omnidecisionbench) · 2026-11-24
    - [SO-Arena：能力可靠性双维评测](../../updates/2026-11-23/#so-arena) · 2026-11-23
    - [Sirius-Tiamat：决策保持式压缩评测](../../updates/2026-11-20/#sirius-tiamat) · 2026-11-20
    - [MM-SystemOneBias：多模态决策偏差评测](../../updates/2026-11-20/#mm-systemonebias) · 2026-11-20
    - [RagHarnessDebugger：Jev引导的修复审计](../../updates/2026-11-19/#ragharnessdebugger-jev) · 2026-11-19
    - [Deciding Without Pointing：揭示检测与定位解耦](../../updates/2026-11-18/#deciding-without-pointing) · 2026-11-18
    - [SO-Arena：System One 模型能力谱系与决策可靠性基准](../../updates/2026-11-14/#so-arena-system-one) · 2026-11-14
    - [Jev 调查模拟的条件预测与联合有效性评估](../../updates/2026-11-14/#jev) · 2026-11-14
    - [量化比较的噪声下限：引擎、重启、批处理与内核漂移](../../updates/2026-11-14/#item-60) · 2026-11-14
    - [PolyRoute：十二语言及代码混合文本的类型化决策路由基准](../../updates/2026-11-12/#polyroute) · 2026-11-12
    - [MMDM：大规模多任务决策能力评测基准](../../updates/2026-11-12/#mmdm) · 2026-11-12
    - [TandemBench：多智能体协作决策模型评测基准](../../updates/2026-11-06/#tandembench) · 2026-11-06
14. **自适应计算深度**：计算深度应按特定续推的预期净收益而非当前错误概率分配；可用中间状态或轻量控制器早停，并联合核算校准、成本和尾延迟。
    - [层级执行控制：中间状态驱动计算分配](../../updates/2026-11-25/#item-128) · 2026-11-25
    - [FLCVA：全账本反事实推理审计](../../updates/2026-11-19/#flcva) · 2026-11-19
    - [Conserved Verdicts：承诺-裁决差识别过度思考](../../updates/2026-11-18/#conserved-verdicts) · 2026-11-18
    - [通过自适应计算将 LLM 转化为高效 System One 决策模型](../../updates/2026-11-14/#llm-system-one) · 2026-11-14
    - [Lev循环决策模型：按难度自适应计算，准确率提升13个百分点](../../updates/2026-11-12/#lev-13) · 2026-11-12
    - [RELOAD：通过层循环扩展类型化决策模型推理](../../updates/2026-11-08/#reload) · 2026-11-08
15. **日志反馈校准**：只有已选动作反馈时，应采用适合日志化Bandit的评分规则训练决策头，避免把未观测候选当负例，并同步监控校准与选择性风险。
    - [基于日志化 Bandit 反馈学习校准决策头](../../updates/2026-11-13/#bandit) · 2026-11-13
<!-- experience-seen: 2026-11-19/anys1 2026-11-19/flcva 2026-11-19/item-53 2026-11-19/item-54 2026-11-19/ragharnessdebugger-jev 2026-11-19/system-1 2026-11-19/vanguard 2026-11-20/agnes-harness 2026-11-20/drift 2026-11-20/glide 2026-11-20/item-80 2026-11-20/looproute 2026-11-20/mm-systemonebias 2026-11-20/piccolo 2026-11-20/rigel-ladon 2026-11-20/sirius-tiamat 2026-11-20/system-one-rsi 2026-11-23/altair-nidhogg 2026-11-23/dm-prm 2026-11-23/item-26 2026-11-23/jevrisk 2026-11-23/lever 2026-11-23/so-arena 2026-11-24/adapt 2026-11-24/molrejev 2026-11-24/omnidecisionbench 2026-11-25/antares-smaug 2026-11-25/catway 2026-11-25/deciform 2026-11-25/decision-models 2026-11-25/dknown-jev-2 2026-11-25/eeg-jev 2026-11-25/eegjev 2026-11-25/geodecisions 2026-11-25/item-128 2026-11-25/jev-2 2026-11-25/jevagentharness-jev 2026-11-25/jevbench 2026-11-25/needwise 2026-11-25/prefill1 2026-11-25/s1arena-mm 2026-11-25/tree-attention 2026-11-25/voyag 2026-11-26/lost-in-translation 2026-11-26/procedure-memory -->
<!-- research-experience:end -->

## 相关工作

**代码 / 框架**
- [fast-browser-use (APUS-AI-Lab)](https://github.com/APUS-AI-Lab/fast-browser-use) — 基于 Qwen3.5 / Gemma 复现 Jev 快决策工作流：保留 Prefill 隐状态、跳过逐 Token Decode、直接对候选动作算概率，9B 模型单次决策 79ms
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — 用 Jev 做 Claude Code 上下文压缩的低成本方案
- [RouteLLM](https://github.com/lm-sys/RouteLLM) — 学习式模型路由框架，按查询难度在强弱模型间分配

**论文**
- [FrugalGPT: How to Use LLMs While Reducing Cost](https://arxiv.org/abs/2305.05176) — 级联式成本感知调用策略，快慢分工的早期形态
- [RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665) — 偏好数据训练路由器
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) — LLM-as-a-Judge 自我改进（被引 996），判断信号自迭代的代表工作

**报道 / 博客**
- [独家｜撬开 Jev 黑箱，对话全球首批复现者：9B 小模型跑通 79 毫秒"快决策"](https://mp.weixin.qq.com/s/IMrdXJooIEBPpbldvmDdIw) — AI前线对 APUS 复现团队的访谈
- [刚刚，Jev 全网解禁！1.2 亿 Token 限时免费用](https://mp.weixin.qq.com/s/i6w4GVq2NV-mL4IzsDRtVw) — TypeSafe AI 开放 Jev：动作判断（Minecraft 中 Astra 规划 + Jev 判断 + 确定性执行）、模型评判（单次 0.44s / $0.00035）等应用形态
