# C5-AG2 方案草案 · 安书伟

> 状态：草案（待 G1 交叉验证）  |  2026-04-30

## 1. 选题

**EconResearchSquad**：基于 AG2 0.9.7 的经济学多智能体研究小队。

- Coordinator + 3 并行专员（增长/物价/外贸）+ 同行评审
- 输入中国宏观月度数据 → 输出结构化政策简报
- 经济学教授背景决定选题锚点：数据驱动型政策分析的智能化

## 2. 拿来对象

**Base repo:** `ag2ai/build-with-ag2` → `beta/parallel-research`

- AG2 Hackathon @ Fordham Gabelli（2026-05-03）获奖项目
- 核心能力：Lead coordinator 分解问题 → 3 研究员并行搜索 → 综合报告
- 使用 AG2 Beta API (`autogen.beta.Agent` + `subagent_tool` + `MemoryStream`)
- License: Apache 2.0（兼容 Fork 改造）
- 代码量：~230 行，结构清晰可读

## 3. 改造路线

| 维度 | Base（parallel-research） | 改造后（EconResearchSquad） |
|---|---|---|
| 场景 | 通用网络调研 | 经济学宏观分析 |
| Agent 角色 | Lead + 3 通用 Researcher | Coordinator + 增长/物价/外贸三专员 + 同行评审 |
| 工具 | Tavily 搜索 + URL 抓取 | 无外部工具，纯 LLM 协作 |
| 并行 | Beta subagent_tool | 经典 GroupChat AutoPattern（稳定 API） |
| API | Beta Agent (0.10+) | ConversableAgent (0.9.7) |
| 输出 | 引用式研究报告 | 结构化政策简报（三段式） |
| 语言 | 英文 | 中文 |
| 审查 | 无 | 三维同行评审回路 |

关键决策：弃用 Beta API（未发布），改用 0.9.7 稳定 API 实现等价的三种多智能体模式。

## 4. 添加的 Agent

在 base repo 的 Lead + 3 Researcher 结构基础上，新增：

1. **Peer Reviewer Agent**（同行评审）— 三维审查：因果推断 / 数据准确性 / 政策约束条件
2. **Policy Writer Agent**（政策撰稿）— 接力流水线中接收数据摘要 → 产出政策简报
3. 三个专员从通用 Researcher 改造为垂直领域专家（增长/物价/外贸），每个有专属 domain prompt

## 5. 预期效果

- **L1**: 三种 AG2 多智能体模式均可独立运行
- **L2**: Lead+Critic 回路实现迭代修正（P0→P1 三轮全部通过）
- **L3**: Group Chat 自动发言人选择 + 接力流水线端到端产出政策简报

## 6. 风险评估

- **API 兼容性**: DeepSeek 作为 OpenAI 兼容后端已实测通过
- **Beta API 不可用**: 已确认 0.9.7 稳定 API 足够实现全部三种模式
- **中文输出质量**: DeepSeek-chat 中文能力已验证，经济学专业术语准确
