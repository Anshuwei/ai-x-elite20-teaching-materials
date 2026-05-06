# Portfolio Entry · C5-AG2

> 状态：已提交  |  日期：2026-04-30  |  作者：安书伟

## 项目名

**EconResearchSquad** — 基于 AG2 的经济学多智能体研究小队

## 一句话定位

Coordinator + 3 并行专员 + 1 同行评审，输入宏观数据，输出结构化政策简报。

## 技术栈

- **框架**: AG2 (AutoGen) 0.9.7 — `ConversableAgent` + `AutoPattern` + `initiate_group_chat`
- **LLM**: DeepSeek-chat（OpenAI 兼容 API）
- **语言**: Python 3.11+
- **并行**: GroupChat AutoPattern（LLM 自动发言人选择）

## 核心能力

1. **三模式多智能体架构**：双Agent审查回路 / GroupChat自动路由 / 接力对话流水线
2. **迭代修正机制**：Lead+Critic 回路实现 P0→P1 审查改善
3. **端到端政策简报**：从宏观数据到结构化政策建议的全自动流水线
4. **垂直领域深度**：增长/物价/外贸三专员各自持有专属 domain prompt

## 新增 Agent

- **Peer Reviewer** — 三维审查（因果推断 / 数据准确性 / 政策约束条件）
- **Policy Writer** — 技术分析 → 通俗政策简报
- **Growth/Price/Trade 三专员** — 从通用 Researcher 改造为垂直领域专家

## Base Repo

[ag2ai/build-with-ag2 · beta/parallel-research](https://github.com/ag2ai/build-with-ag2/tree/main/beta/parallel-research) — AG2 Hackathon @ Fordham Gabelli 获奖项目

## 关键指标

| 指标 | 结果 |
|---|---|
| 多智能体模式数 | 3（均可独立运行） |
| 参与 Agent 数 | 6（Coordinator + 3 专员 + Policy Writer + Peer Reviewer） |
| Lead+Critic 迭代修正 | P0 三 FAIL → P1 三 PASS |
| GroupChat 自动调度 | AutoPattern LLM 自动选择发言人 |
| 接力流水线 | 数据分析 → 政策简报 → 同行评审 三阶段 |
| 代码行数 | ~200（不含文档） |

## 许可

Apache License 2.0

## 仓库

[Anshuwei/ai-x-elite20-teaching-materials](https://github.com/Anshuwei/ai-x-elite20-teaching-materials) → `challenges/C5-AG2/`
