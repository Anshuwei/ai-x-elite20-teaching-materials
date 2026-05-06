# Changelog · EconResearchSquad

## [1.0.0] — 2026-04-30

### Added
- Mode 1: Lead + Critic 双 Agent 审查回路（迭代修正，max_turns=2）
- Mode 2: Group Chat 自动路由（Coordinator + 增长/物价/外贸三专员）
- Mode 3: 接力对话流水线（数据分析 → 政策简报 → 同行评审）
- CLI 入口 (`argparse --mode 1/2/3`)
- 烟雾测试 (`tests/test_smoke.py`)
- 一键复现脚本 (`scripts/reproduce.sh`)
- 六件套提交文档 (PROPOSAL / DRAFT / G1_ENDORSEMENT / AI_LOG / REUSE / CHANGELOG)
- Apache 2.0 License

### Changed
- 从 AG2 Beta API (`autogen.beta.Agent`) 迁移到稳定版 (`ConversableAgent` 0.9.7)
- 从英文通用调研场景迁移到中文经济学分析场景
- 从 Beta subagent_tool 并行切换到 GroupChat AutoPattern

### Removed
- Tavily 搜索依赖（原 base repo 用于网络搜索）
- Google Gemini 依赖（原 base repo 的 LLM 后端）
- Beta API 流式功能（`MemoryStream` / `StreamFactory`，不可用）
