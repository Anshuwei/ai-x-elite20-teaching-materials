# 拿来说明 · EconResearchSquad

> 按 Elite20 挑战提交总则 v1.3 要求，说明"拿来"了哪些、怎么改造的。

## 拿来源

**Base repo:** [ag2ai/build-with-ag2 · beta/parallel-research](https://github.com/ag2ai/build-with-ag2/tree/main/beta/parallel-research)

- AG2 Hackathon @ Fordham Gabelli (2026-05-03) 获奖项目
- License: Apache 2.0
- 原始代码：`main.py` (~230 行)

## 拿来的具体元素

| # | 元素 | 来源文件 | 用途 |
|---|---|---|---|
| 1 | Coordinator + 多专员并行架构 | `main.py` L191-235 | 结构参考，改为经济学场景 |
| 2 | Agent 角色分工思路 | README.md 架构图 | 启发增长/物价/外贸三专员划分 |
| 3 | `initiate_chat` 用法 | AG2 0.9.7 官方文档 | Mode 1/3 核心 API |
| 4 | `AutoPattern` + `initiate_group_chat` | AG2 0.9.7 官方文档 | Mode 2 自动路由 |
| 5 | `LLMConfig` OpenAI 兼容配置 | AG2 0.9.7 示例 | DeepSeek API 配置模式 |
| 6 | `summary_method="reflection_with_llm"` | AG2 0.9.7 API | Mode 3 接力交接 |

## 改造内容

| # | 改造项 | 说明 |
|---|---|---|
| 1 | **API 降级** | Beta Agent → ConversableAgent（因 0.10 未发布） |
| 2 | **场景迁移** | 通用网络调研 → 经济学宏观分析 |
| 3 | **新增 Peer Reviewer** | 三维审查（因果推断 / 数据准确性 / 政策约束条件） |
| 4 | **新增 Policy Writer** | 将技术分析转为非技术决策者能看懂的简报 |
| 5 | **三专员垂直化** | 从通用 Researcher 改造为增长/物价/外贸领域专家 |
| 6 | **语言切换** | 英文 → 中文（适配中国经济政策场景） |
| 7 | **模块化** | 从单一脚本 → 模块化入口 + argparse CLI + 测试 |
| 8 | **并行方式切换** | Beta subagent_tool → GroupChat AutoPattern |

## 未使用的外部依赖

Base repo 使用以下外部服务，EconResearchSquad **均未使用**：
- Tavily Search API（Beta repo 用于网络搜索）
- Google Gemini API（Beta repo 的 LLM 后端）
- `MemoryStream` / `StreamFactory`（Beta 流式功能）

EconResearchSquad 是纯 LLM 多智能体协作，不需要任何外部 API 除 LLM 本身。

## 许可兼容性

- Base repo: Apache 2.0
- EconResearchSquad: Apache 2.0
- 兼容，无冲突
