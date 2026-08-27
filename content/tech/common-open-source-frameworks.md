+++
title = '常用开源框架'
date = 2026-08-27T00:00:00+08:00
draft = true
toc = true
+++

# 常用开源框架

围绕大模型研发全流程（**后训练 → 推理服务 → 评测**）的常用开源框架，以下仓库本站均已 fork，便于跟读源码与二次开发。

| 框架 | 定位 | 上游仓库 | 本站 fork |
| --- | --- | --- | --- |
| verl | LLM 强化学习后训练 | [verl-project/verl](https://github.com/verl-project/verl) | [dujh22/verl](https://github.com/dujh22/verl) |
| SGLang | LLM / 多模态推理服务 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | [dujh22/sglang](https://github.com/dujh22/sglang) |
| SkyThought | 推理模型训练全流程 | [NovaSky-AI/SkyThought](https://github.com/NovaSky-AI/SkyThought) | [dujh22/SkyThought](https://github.com/dujh22/SkyThought) |
| OpenJudge | AI 应用评测与质量奖励 | [agentscope-ai/OpenJudge](https://github.com/agentscope-ai/OpenJudge) | [dujh22/OpenJudge](https://github.com/dujh22/OpenJudge) |

## verl — LLM 强化学习后训练框架

[verl](https://github.com/verl-project/verl)（Volcano Engine Reinforcement Learning for LLMs）由字节跳动 Seed 团队发起、verl 社区维护，是 [HybridFlow](https://arxiv.org/abs/2409.19256)（EuroSys 2025）论文的开源实现，主打灵活、高效、可落地的 LLM RL 后训练。

**核心特性**

- **易扩展的算法表达**：混合控制器（hybrid-controller）编程模型，几行代码即可搭建 GRPO、PPO 等复杂后训练数据流。
- **模块化集成现有基建**：计算与数据依赖解耦，可与 FSDP、Megatron-LM、vLLM、SGLang 等框架无缝组合。
- **灵活的设备映射**：支持把各模型放置到不同 GPU 组合上，适配从单机到大规模集群。
- **高吞吐**：3D-HybridEngine 实现训练 / 生成阶段间 actor 模型的高效重分片，降低显存冗余与通信开销。
- Megatron 后端可支撑 DeepSeek-671B、Qwen3-235B 级别 MoE 模型的 RL 训练；DAPO、Seed-Thinking-v1.5、ReTool 等知名工作均由 verl 训练或提供复现 recipe。

**相关链接**

- 本站 fork：[github.com/dujh22/verl](https://github.com/dujh22/verl)
- 论文：[HybridFlow: A Flexible and Efficient RLHF Framework](https://arxiv.org/abs/2409.19256)
- 文档：<https://verl.readthedocs.io> ｜ 中文介绍：<https://www.volcengine.com/docs/6459/1463942>

## SGLang — 高性能推理服务框架

[SGLang](https://github.com/sgl-project/sglang) 是 LMSYS 旗下高性能 LLM / 多模态推理服务框架，日均产出万亿级 token、全球部署超 40 万块 GPU，已成为开源推理引擎的事实标准之一。

**核心特性**

- **Fast Runtime**：RadixAttention 前缀缓存、零开销 CPU 调度器、Prefill-Decode 分离（PD）、投机解码、连续批处理、PagedAttention、TP/PP/EP/DP 各类并行、结构化输出、chunked prefill、FP4/FP8/INT4/AWQ/GPTQ 量化与 multi-LoRA 批量服务。
- **模型支持广**：Llama、Qwen、DeepSeek、Kimi、GLM、Gemma、Mistral 等，兼覆盖 embedding、reward 与扩散模型；对新模型提供 day-0 支持（DeepSeek-V4、Kimi K3 等）。
- **硬件覆盖全**：NVIDIA、AMD、Intel CPU、Google TPU、昇腾 NPU 等。
- **RL 后训练骨干**：作为 rollout 后端被 verl、slime、AReaL、Tunix 等后训练框架广泛采用——与 verl 组合是当前 RL 训练的主流技术栈。

**相关链接**

- 本站 fork：[github.com/dujh22/sglang](https://github.com/dujh22/sglang)
- 文档：<https://docs.sglang.io> ｜ 官网：<https://www.sglang.io> ｜ 技术博客：<https://lmsys.org/blog/>

## SkyThought — 推理模型训练全流程

[SkyThought](https://github.com/NovaSky-AI/SkyThought) 来自 UC Berkeley NovaSky 实验室，口号是「**用 450 美元训练你自己的 O1 级推理模型**」（Sky-T1），开源了从数据清洗、训练到评测的完整流程代码。

**仓库结构**

- `recipes/`：Sky-T1 系列模型的数据构造步骤与训练策略。
- `skythought/train/`：SFT 训练脚本，基于 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)。
- `skythought/skythought-rl/`：Sky-T1-7B / mini 的 RL 训练代码。
- `skythought/evals/`：数据生成与评测库，提供 CLI 和 `Scorer` API（`pip install skythought`）。

**代表成果**

- [Sky-T1-32B-Preview](https://huggingface.co/NovaSky-AI/Sky-T1-32B-Preview)：仅用 17k 高质量样本 SFT 训练。
- Sky-T1-32B-Flash：缓解 overthinking，在保持精度的同时显著缩短推理序列长度。
- Sky-T1-7B / mini：验证蒸馏之后继续 RL 仍能进一步提升能力。
- S*：面向代码生成的测试时扩展框架（[论文](https://arxiv.org/abs/2502.14382)）。

**相关链接**

- 本站 fork：[github.com/dujh22/SkyThought](https://github.com/dujh22/SkyThought)
- 项目主页：<https://novasky-ai.github.io> ｜ 模型合集：<https://huggingface.co/NovaSky-AI>

## OpenJudge — AI 应用评测与质量奖励

[OpenJudge](https://github.com/agentscope-ai/OpenJudge)（A Unified Framework for Holistic Evaluation and Quality Rewards）是 AgentScope 社区开源的 **AI 应用（Agent / 对话机器人）评测框架**，用于评估应用质量并驱动持续优化。

**核心特性**

- **完整评测工作流**：收集测试数据 → 定义 graders → 大规模评测 → 分析薄弱点 → 快速迭代。
- **50+ 开箱即用 grader**：经过系统化分类与校验，覆盖威胁分析、声明一致性、完整性等多类维度；支持为具体场景自动生成专属评分 rubric。
- **评测即奖励**：打分结果可转换为 reward 信号，直接用于微调优化应用。
- 配套生态：在线试用 [openjudge.me/app](https://openjudge.me/app/)、Streamlit 可视化 UI、[PawBench](https://github.com/agentscope-ai/PawBench)（Model × Harness 联合评测基准，150 任务 × 9 模型 × 3 框架）。

**相关链接**

- 本站 fork：[github.com/dujh22/OpenJudge](https://github.com/dujh22/OpenJudge)
- 文档：<https://agentscope-ai.github.io/OpenJudge> ｜ 官网：<https://openjudge.me> ｜ 安装：`pip install py-openjudge`

## 延伸阅读

更多微调 / RL / 部署框架（LLaMA-Factory、ms-swift、Unsloth、OpenRLHF、ROLL、TRL、vLLM 等）见资源页[《开源框架》](/resources/开源框架/)。
