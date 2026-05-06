# EconResearchSquad · C5-AG2 submission by 安书伟

一句话定位：基于 AG2 的经济学多智能体研究小队——Coordinator + 3 个并行专员 + 1 个同行评审，输入宏观数据，输出结构化政策简报。

## 🎬 Demo

```bash
python src/econ_research_squad.py
```

运行后依次演示三种 AG2 多智能体模式：
1. Lead + Critic 双 Agent 审查回路
2. Group Chat 自动路由（Coordinator + 增长/物价/外贸三专员）
3. 接力对话流水线（数据分析 → 政策简报）

完整交互日志见 [`docs/demo.md`](docs/demo.md)。

## 🚀 Quick Start

```bash
git clone https://github.com/Anshuwei/ai-x-elite20-teaching-materials.git
cd ai-x-elite20-teaching-materials/challenges/C5-AG2
pip install -r requirements.txt
export ANTHROPIC_AUTH_TOKEN="your-deepseek-key"
bash scripts/reproduce.sh
```

**兼容任意 OpenAI 兼容 API：**
```bash
export OPENAI_API_KEY="sk-..."
# 修改 src/econ_research_squad.py 中的 API_BASE / API_KEY / MODEL
```

## 📊 Results

| Level | 指标 | 达到 |
|---|---|---|
| L1 | 三种 AG2 多智能体模式均可独立运行 | ✅ |
| L2 | Lead+Critic 回路实现迭代修正（实测 P0→P1 三轮全部通过） | ✅ |
| L3 | Group Chat 自动发言人选择 + 接力流水线端到端产出政策简报 | ✅ |

## 🧾 Evidence Ledger

- AI 开发日志：[AI_LOG.md](AI_LOG.md)
- 拿来说明：[REUSE.md](REUSE.md)
- 方案设计：[PROPOSAL.md](PROPOSAL.md)
- 方案草案：[PROPOSAL_DRAFT.md](PROPOSAL_DRAFT.md)
- G1 背书：[G1_ENDORSEMENT.md](G1_ENDORSEMENT.md)

## 🏗 Architecture

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

## 🙏 Acknowledgements

- **Base repo:** [ag2ai/build-with-ag2 beta/parallel-research](https://github.com/ag2ai/build-with-ag2/tree/main/beta/parallel-research) — AG2 Hackathon @ Fordham Gabelli (May 3, 2026) 获奖项目
- **Skills 驱动开发:** 使用 build-with-ag2 的 15 个 `.agents/skills/` 生成代码
- **拿来改造:** Fork 思路来自 [ag2ai/ag2](https://github.com/ag2ai/ag2) AG2 0.9.7 稳定 API

## 📁 Repo 结构

```
C5-AG2/
├── README.md
├── PROPOSAL.md              # 方案设计
├── PROPOSAL_DRAFT.md        # 方案草案（G1输入）
├── G1_ENDORSEMENT.md        # G1 背书
├── AI_LOG.md                # AI 开发日志
├── REUSE.md                 # 拿来说明
├── CHANGELOG.md
├── LICENSE                  # Apache-2.0
├── requirements.txt
├── src/
│   └── econ_research_squad.py
├── tests/
│   └── test_smoke.py
├── scripts/
│   └── reproduce.sh
└── docs/
    └── demo.md
```

## 🛡️ License

Apache License 2.0. 详见 [LICENSE](LICENSE).
