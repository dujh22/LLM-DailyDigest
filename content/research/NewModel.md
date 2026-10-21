+++
title = 'NewModel'
proposer = '杜晋华'
since = '2026-10-21'
date = 2026-10-21T00:00:00+08:00
draft = false
toc = true
+++

# NewModel

> 研究方向：**新模型**——基础模型新版本、新架构与新训练范式的跟踪与剖析，关注"模型本身变了什么"，而非某个自进化机制。

## 研究范畴

新模型（new model watch）是本站的横向跟踪方向，与各 `*Evolve` 方向互补：`*Evolve` 关心"如何让模型自己变强"的方法论，NewModel 关心"新发布的模型在架构、数据、训练配方与能力边界上到底改了什么"。本方向涵盖：开源与闭源基础模型的新版本（通用 / 推理 / 多模态 / 小尺寸端侧）、注意力与序列建模架构创新（线性注意力、稀疏注意力、混合 Mamba-Transformer、循环记忆层）、MoE 稀疏化与专家路由设计、训练配方与优化器（数据配比、课程、Muon 类二阶优化、长上下文训练）、推理模型的后训练范式（RLVR、可验证奖励、测试时扩展），以及扩散语言模型等非自回归路线的进展。社区关注的核心问题包括：新架构的收益能否在同等算力下复现、benchmark 分数与真实能力之间的落差、开源权重与训练细节披露的不对称、模型谱系与蒸馏关系难以追溯，以及新模型发布节奏下如何做有效的横向对比而非简单刷榜。

## 研究挑战

- 可比性缺失：不同模型的评测口径、提示模板、思维链预算与工具权限差异极大，分数不可直接横比。
- 复现成本高：新架构的收益往往依赖未披露的训练数据与算力规模，小规模复现结论常与论文不一致。
- 能力归因困难：架构改动、数据配比与后训练策略同时变化，难以判断收益来自哪一项。
- 过拟合榜单：benchmark 污染与针对性优化使新模型的真实增量被高估。
- 披露不对称：闭源模型只给分数不给细节，开源模型常缺训练配方，横向分析只能停在表面。
- 长上下文与新架构的工程落地：稀疏 / 线性注意力在训练侧可行，但推理框架支持与吞吐收益未必同步。

## 自研项目

- [EvolveLLM](https://github.com/dujh22/EvolveLLM) — 博士课题《Toward True ASI》承载仓库，含自进化机制综述与方法论沉淀。

## 相关工作

**代码 / 框架 / 模型权重**
- [Qwen3](https://github.com/QwenLM/Qwen3) — 阿里通义千问开源系列，含稠密与 MoE 双路线及混合思考模式
- [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) — DeepSeek 开源 MoE 基础模型，MLA + 无辅助损失负载均衡
- [GLM-4](https://github.com/THUDM/GLM-4) — 智谱 GLM 系列开源权重与推理代码
- [vLLM](https://github.com/vllm-project/vllm) — 新模型落地推理的主流服务框架，新架构支持速度是事实上的可用性门槛
- [SGLang](https://github.com/sgl-project/sglang) — 高性能推理框架，常作为新模型论文的对拍基线

**论文**
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — 开源模型少见的完整训练配方披露：数据、缩放律、后训练与长上下文分阶段策略
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — MoE 架构 + MLA + FP8 训练，671B 总参数下激活参数控制
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066) — 细粒度专家切分与共享专家隔离
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) — 纯 RL 激发推理能力，并蒸馏回小模型
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) — 稠密 / MoE 统一系列与思考—非思考模式融合
- [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818) — 早期融合的混合模态 token 化架构
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887) — Transformer 与 Mamba 层交错，兼顾长上下文效率与质量
- [Gated Linear Attention Transformers with Hardware-Efficient Training](https://arxiv.org/abs/2312.06635) — 门控线性注意力的硬件友好并行训练算法
- [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://arxiv.org/abs/2502.11089) — 可原生训练、硬件对齐的稀疏注意力
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663) — 测试时可学习的长期记忆模块，与注意力互补
- [Muon is Scalable for LLM Training](https://arxiv.org/abs/2502.16982) — 二阶优化器在大规模预训练上的可扩展性验证
- [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992) — 扩散式语言模型在规模化下的可行性
- [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) — 用 1000 条样本 + 预算强制实现测试时扩展

**综述 / 报道**
- [arXiv cs.CL / cs.LG 新提交](https://arxiv.org/list/cs.CL/recent) — 新模型类工作的高频来源，本站推荐系统的默认抓取源之一
