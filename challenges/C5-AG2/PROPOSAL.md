# C5-AG2 方案设计 · 安书伟

> 版本：v1.0  |  2026-04-30  |  状态：已提交

## 一句话定位

基于 AG2 的经济学多智能体研究小队——Coordinator + 3 个并行专员 + 1 个同行评审，输入宏观数据，输出结构化政策简报。

## 架构

```
用户输入（宏观数据）
       │
       ▼
┌─────────────────┐
│  Coordinator    │  首席经济学家 — 分析请求、分解任务
└──────┬──────────┘
       │ parallel fan-out (GroupChat AutoPattern)
  ┌────┴────┬────────┐
  ▼         ▼        ▼
┌──────┐ ┌──────┐ ┌──────┐
│Growth│ │Price │ │Trade │  三专员并行分析
│Spec. │ │Spec. │ │Spec. │
└──────┘ └──────┘ └──────┘
  │         │        │
  └────┬────┴────────┘
       ▼
┌─────────────────┐
│ Policy Writer   │  将分析结果转为政策简报
└────────┬────────┘
         ▼
┌─────────────────┐
│ Peer Reviewer   │  因果推断 / 数据准确性 / 政策约束条件 三维审查
└─────────────────┘
```

## 技术选型

| 层级 | 选型 | 理由 |
|---|---|---|
| 框架 | AG2 (AutoGen) 0.9.7 | 稳定版，`ConversableAgent` + `AutoPattern` 成熟 API |
| LLM | DeepSeek-chat (OpenAI 兼容) | 中文能力强，经济学专业术语准确，低成本 |
| 语言 | Python 3.11+ | AG2 最低要求 |
| 并行 | GroupChat AutoPattern | LLM 自动发言人选择，0.9.7 原生支持 |

## 三种多智能体模式

### Mode 1: Lead + Critic 审查回路

```
lead_analyst → peer_reviewer → lead_analyst (修正) → peer_reviewer (终审)
```
- max_turns=2 实现迭代修正
- 实测 P0→P1 三轮：初始三 FAIL → 修改后三 PASS

### Mode 2: Group Chat 自动路由

```
chief_economist (初始发言人)
    │ AutoPattern 自动选择
    ├── growth_specialist
    ├── price_specialist
    └── trade_specialist
    │
    └── chief_economist (整合)
```
- 5 个 Agent 自动协作，无需人工调度
- max_rounds=10 防止无限循环

### Mode 3: 接力对话流水线

```
data_analyst ──(摘要)──→ policy_writer ──(简报)──→ peer_reviewer ──(审查)
```
- 使用 `summary_method="reflection_with_llm"` 实现结构化交接
- 三阶段链式传递，每个阶段拿到上阶段输出

## Base Repo 与改造

**Fork 来源:** [ag2ai/build-with-ag2 · beta/parallel-research](https://github.com/ag2ai/build-with-ag2/tree/main/beta/parallel-research)

| 维度 | Base | 改造后 |
|---|---|---|
| API | Beta Agent (0.10+) | ConversableAgent (0.9.7) |
| 场景 | 通用网络调研 | 经济学宏观分析 |
| Agent 数量 | 4 (1 Lead + 3 Researcher) | 6 (1 Coordinator + 3 专员 + 1 Policy Writer + 1 Peer Reviewer) |
| 审查机制 | 无 | 双审查回路 (Mode 1 同行评审 + Mode 3 接力评审) |
| 输出 | 引用式研究报告 | 结构化政策简报（三段式） |
| 语言 | 英文 | 中文 |

## 新增 Agent 清单

1. **Peer Reviewer Agent** — 三维审查（因果推断 / 数据准确性 / 政策约束条件），在 Mode 1 和 Mode 3 中分别运作
2. **Policy Writer Agent** — 将技术分析转为面向非技术决策者的通俗简报
3. **三个垂直领域专员** — 增长/物价/外贸，每个有专属 domain system_message（base 中为通用 Researcher）

## 验证结果

| Level | 指标 | 状态 |
|---|---|---|
| L1 | 三种 AG2 多智能体模式均可独立运行 | ✅ |
| L2 | Lead+Critic 回路实现迭代修正 | ✅ |
| L3 | Group Chat 自动发言人选择 + 接力流水线端到端产出 | ✅ |
