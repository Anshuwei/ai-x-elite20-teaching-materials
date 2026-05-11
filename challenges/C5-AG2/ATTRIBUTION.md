# ATTRIBUTION.md — C5-AG2 Submission by 安书伟

> Elite20 拿来主义 (fork-and-improve) principle: every reused fragment is cited.
> 每一处借鉴都要溯源。

---

## 1. Fork source / Fork 源

| | |
|---|---|
| Base project | build-with-ag2 · beta/parallel-research |
| Base repo URL | https://github.com/ag2ai/build-with-ag2/tree/main/beta/parallel-research |
| Base captain | AG2 Hackathon @ Fordham Gabelli (May 3, 2026) 获奖项目 |
| My repo URL | https://github.com/Anshuwei/ai-x-elite20-teaching-materials/tree/main/challenges/C5-AG2 |
| Fork commit SHA | N/A（未直接 fork，基于其 README 架构图和 main.py 思路重新实现） |
| Track inheritance | base `multi-agent` → mine: `multi-agent` |

Note: 未直接 fork 仓库。借鉴了 beta/parallel-research 的 **Coordinator + 多专员并行架构** 和 **Lead+Citric 审查模式**，使用 AG2 0.9.7 稳定 API 重新实现。

---

## 2. AG2 documentation references / AG2 文档引用

> 每一段从 AG2 文档复制/改编的代码必须注明来源。

| File in your repo | Lines | Source doc | Verbatim / Adapted |
|---|---|---|---|
| `src/econ_research_squad.py` | L14-L18 | AG2 0.9.7 official docs — `ConversableAgent` + `LLMConfig` API | adapted: 改为 DeepSeek API + 中文经济学场景 |
| `src/econ_research_squad.py` | L87-L94 | AG2 0.9.7 `initiate_chat()` API reference | adapted: max_turns=2 审查回路 |
| `src/econ_research_squad.py` | L137-L155 | AG2 0.9.7 `AutoPattern` + `initiate_group_chat` docs | adapted: 5 agent 经济学群聊 |
| `src/econ_research_squad.py` | L206-L235 | AG2 0.9.7 `summary_method="reflection_with_llm"` example | adapted: 三阶段接力流水线 |
| `examples/economics_research_squad.py` | L1-L226 | build-with-ag2 `.agents/skills/` (15 skills) — 架构参考 | adapted: 从 Beta API 降级到稳定 API |

---

## 3. Code reused from sample repos / 借鉴自样本 repo

| Source repo | Source file | Used in my repo | Notes |
|---|---|---|---|
| ag2ai/build-with-ag2 beta/parallel-research | `main.py` L191-L235 | `src/econ_research_squad.py` Mode 2 | 借鉴 Coordinator + 3 researchers 并行架构，改为经济学三专员 + GroupChat AutoPattern |
| ag2ai/build-with-ag2 beta/parallel-research | `main.py` L166-L175 | `src/econ_research_squad.py` Mode 1 | 借鉴 Lead + Critic 审查模式，改为中文经济学评论场景 |
| ag2ai/build-with-ag2 `.agents/skills/ag2-quickstart` | skill prompt | `src/econ_research_squad.py` LLMConfig 配置 | 借鉴 OpenAI 兼容 API 配置模式 |

---

## 4. Prompts and prompt fragments / 提示词与提示词片段

| Used in | Source | Verbatim / Adapted |
|---|---|---|
| `_M1_LEAD_PROMPT` (经济学评论员) | original (mine) — 基于经济学教授领域知识设计 | — |
| `_M1_CRITIC_PROMPT` (三维审查) | original (mine) — 因果推断/数据准确性/政策约束条件 | — |
| `_M2_COORDINATOR_PROMPT` (首席经济学家) | adapted from beta/parallel-research Lead prompt 的"整合+综合"思路 | adapted |
| `_M2_GROWTH/PRICE/TRADE_PROMPT` (三专员) | original (mine) — 宏观经济学三部门框架 | — |
| `_M3_POLICY_WRITER_PROMPT` (政策撰稿) | original (mine) — 面向非技术决策者的通俗化要求 | — |
| `_M3_PEER_REVIEWER_PROMPT` (同行评审) | adapted from Mode 1 Critic prompt | adapted: 简化为单句结论 |

---

## 5. Datasets, assets, and other inputs / 数据集与其它输入

| Asset | Source | License |
|---|---|---|
| 中国 2026 Q1 宏观经济数据（GDP/CPI/PPI/出口/就业） | 模拟数据，基于公开统计口径构造 | N/A（虚构教学数据） |

---

## 6. What I added / created / 我新增的部分

> 必须有这一节。否则不算"改造"，只是"复制"。

- **Peer Reviewer Agent**（同行评审）— 在 Mode 1（Lead+Critic 回路）和 Mode 3（接力审查）中新增三维审查：因果推断合理性、数据引用准确性、政策建议约束条件。`src/econ_research_squad.py` L49-L67, L186-L200.
- **Policy Writer Agent**（政策撰稿人）— 接力流水线第二棒，将技术分析摘要转为面向非经济学背景决策者的 100 字中文政策简报。`src/econ_research_squad.py` L179-L183.
- **三个垂直领域专员**（增长/物价/外贸）— 从 base repo 的通用 "researcher" 改造为各自持有专属 domain system_message 的垂直专家。`src/econ_research_squad.py` L103-L128.
- **三模式统一入口** — argparse CLI (`--mode 1/2/3`)，每种模式可独立运行。`src/econ_research_squad.py` L243-L263.
- **接力对话流水线**（Mode 3）— 三阶段 `initiate_chat` + `summary_method="reflection_with_llm"` 实现数据→简报→审查的结构化交接。Base repo 无此模式。`src/econ_research_squad.py` L170-L235.
- **烟雾测试** — `tests/test_smoke.py` 验证所有模式函数可导入、提示词非空。
- **一键复现脚本** — `scripts/reproduce.sh` 自动创建 venv + 安装依赖 + 运行全部模式。

---

## 7. License compatibility check / 许可证兼容性检查

| Source | Source license | Compatible with my license? |
|---|---|---|
| ag2ai/build-with-ag2 (beta/parallel-research) | Apache 2.0 | ✅ My repo: Apache 2.0 |
| AG2 framework (ag2ai/ag2) | Apache 2.0 | ✅ |
| AG2 0.9.7 official documentation | Apache 2.0 | ✅ |

---

## 8. Self-audit / 自审

- [x] Every code block ≥ 5 lines copied from elsewhere is cited above
- [x] My fork source is identified (or "from scratch" declared explicitly)
- [x] License compatibility checked
- [x] Section 6 ("What I added") is non-trivial (≥ 3 substantive items)
