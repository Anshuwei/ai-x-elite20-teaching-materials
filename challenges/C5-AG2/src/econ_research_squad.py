"""
EconResearchSquad — 基于 AG2 的经济学多智能体研究小队
Economics Research Squad on AG2 0.9.7

Coordinator + 3 并行专员 + 1 同行评审，输入宏观数据，输出结构化政策简报。
演示三种 AG2 多智能体协作模式：

  Mode 1: Lead + Critic 双 Agent 审查回路（迭代修正）
  Mode 2: Group Chat 自动路由（Coordinator + 增长/物价/外贸三专员）
  Mode 3: 接力对话流水线（数据分析 → 政策简报 → 同行评审）

使用方式:
  python src/econ_research_squad.py              # 运行全部三种模式
  python src/econ_research_squad.py --mode 1     # 仅运行模式 1
  python src/econ_research_squad.py --mode 2     # 仅运行模式 2
  python src/econ_research_squad.py --mode 3     # 仅运行模式 3
"""

import os
import sys
import argparse

from autogen import ConversableAgent, LLMConfig
from autogen.agentchat import initiate_group_chat
from autogen.agentchat.group.patterns import AutoPattern

# ─── 配置：兼容任意 OpenAI 兼容 API ──────────────────────────────────
API_BASE = os.environ.get("OPENAI_API_BASE", "https://api.deepseek.com/v1")
API_KEY = os.environ.get(
    "ANTHROPIC_AUTH_TOKEN",
    os.environ.get("OPENAI_API_KEY", "sk-placeholder"),
)
MODEL = os.environ.get("OPENAI_MODEL", "deepseek-chat")

_llm_config = LLMConfig(
    api_type="openai",
    model=MODEL,
    api_key=API_KEY,
    base_url=API_BASE,
    temperature=0.7,
)


def _section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


# ═══════════════════════════════════════════════════════════════════════
# 模式 1：Lead + Critic 双 Agent 审查回路
# ═══════════════════════════════════════════════════════════════════════

_M1_LEAD_PROMPT = """\
你是一位资深经济学评论员。给定一个经济话题和具体数据，\
撰写一段 120 字以内的中文评论。结构：
1. 一个核心判断
2. 一个数据支撑
3. 一个政策含义
不要使用公式。评论写完后说 TERMINATE。"""

_M1_CRITIC_PROMPT = """\
你是一位经济学同行评审。收到评论后，用中文检查三个维度：
1. 因果推断是否合理（相关 ≠ 因果）
2. 数据引用是否准确
3. 政策建议是否有明确的约束条件
每个维度给出判定（通过/不通过）和一句话理由。\
审查完后说 TERMINATE。"""

_M1_SEED_ARTICLE = """\
请审阅我的经济学评论：

'中国 2026 Q1 高新技术产业投资同比增长 12.3%，\
远超整体固定资产投资增速 4.8%。这表明中国正在经历\
显著的投资结构转型：从传统基建和房地产驱动，\
转向以芯片、新能源、AI 为核心的先进制造业驱动。\
政策含义是，财政刺激应该更精准地投向技术扩散环节，\
而非简单地扩大总量投资。'

请逐维度审查。"""


def run_mode1_lead_critic() -> str:
    """Lead + Critic 双 Agent 审查回路。

    经济学评论员撰写评论 → 同行评审三维审查 → 最多 2 轮迭代修正。
    返回最终审查摘要。
    """
    _section("模式 1: Lead + Critic 双 Agent 审查回路")

    lead = ConversableAgent(
        name="lead_analyst",
        system_message=_M1_LEAD_PROMPT,
        llm_config=_llm_config,
    )
    critic = ConversableAgent(
        name="peer_reviewer",
        system_message=_M1_CRITIC_PROMPT,
        llm_config=_llm_config,
    )

    result = lead.initiate_chat(
        critic,
        message=_M1_SEED_ARTICLE,
        max_turns=2,
    )
    summary = result.summary if result.summary else "（见上方对话）"
    print(f"\n审查结果:\n{summary}")
    return summary


# ═══════════════════════════════════════════════════════════════════════
# 模式 2：Group Chat — Coordinator + 三个经济学专员
# ═══════════════════════════════════════════════════════════════════════

_M2_COORDINATOR_PROMPT = """\
你是首席经济学家。你收到三个专员的分析后，\
整合成一段 150 字以内的中文宏观经济总览。\
总结后说 TERMINATE。"""

_M2_GROWTH_PROMPT = """\
你是经济增长分析师。关注 GDP 增长、消费、投资数据。\
用 60 字以内中文回答，给关键数据 + 一句话判断。"""

_M2_PRICE_PROMPT = """\
你是物价分析师。关注 CPI、PPI、通胀预期。\
用 60 字以内中文回答，判断通缩/通胀压力。"""

_M2_TRADE_PROMPT = """\
你是外贸分析师。关注出口、汇率、资本流动。\
用 60 字以内中文回答，评估外需前景和汇率影响。"""

_M2_DATA_INTRO = """\
我们来分析中国 2026 Q1 宏观经济状况。
数据：GDP 同比 +5.2%，消费贡献率 68%，高新技术投资 +12.3%，\
固定资产投资 +4.8%，CPI +0.8%，PPI -0.9%，出口 +8.3%（对东盟 +15%），\
人民币兑美元 7.10，社会消费品零售 +4.5%，调查失业率 5.1%。

请 growth_specialist 先分析增长驱动力，\
然后 price_specialist 分析物价走势，\
然后 trade_specialist 分析外贸形势。\
最后 chief_economist 整合所有发现给出总览。"""


def run_mode2_group_chat() -> str:
    """Group Chat 自动路由。

    Coordinator + 增长/物价/外贸三专员，AutoPattern 自动选择发言人。
    返回最后发言人名称。
    """
    _section("模式 2: Group Chat — 宏观经济分析三人组")

    coordinator = ConversableAgent(
        name="chief_economist",
        system_message=_M2_COORDINATOR_PROMPT,
        llm_config=_llm_config,
    )
    growth = ConversableAgent(
        name="growth_specialist",
        system_message=_M2_GROWTH_PROMPT,
        llm_config=_llm_config,
    )
    price = ConversableAgent(
        name="price_specialist",
        system_message=_M2_PRICE_PROMPT,
        llm_config=_llm_config,
    )
    trade = ConversableAgent(
        name="trade_specialist",
        system_message=_M2_TRADE_PROMPT,
        llm_config=_llm_config,
    )
    user_proxy = ConversableAgent(
        name="user",
        system_message="你负责发起讨论。",
        human_input_mode="NEVER",
    )

    pattern = AutoPattern(
        initial_agent=coordinator,
        agents=[coordinator, growth, price, trade],
        user_agent=user_proxy,
        group_manager_args={"llm_config": _llm_config},
    )

    _result, _context, last_agent = initiate_group_chat(
        pattern=pattern,
        messages=_M2_DATA_INTRO,
        max_rounds=10,
    )
    label = last_agent.name
    print(f"\nGroup Chat 结束。最后发言人: {label}")
    return label


# ═══════════════════════════════════════════════════════════════════════
# 模式 3：接力对话流水线 — 数据分析 → 政策简报 → 同行评审
# ═══════════════════════════════════════════════════════════════════════

_M3_DATA_ANALYST_PROMPT = """\
你是一位宏观经济数据分析师。给定数据，提取关键趋势，\
识别值得关注的信号。用中文输出结构化数据摘要。\
最后说 TERMINATE。"""

_M3_POLICY_WRITER_PROMPT = """\
你是一位经济政策撰稿人。拿到数据分析师的结构化摘要后，\
撰写一份面向非经济学背景决策者的中文政策简报。
要求：100 字以内，语言通俗，不出现公式，\
包含：总体判断 + 两个关键信号 + 一个可操作的政策建议。\
写完后说 TERMINATE。"""

_M3_PEER_REVIEWER_PROMPT = """\
你是一位经济学同行评审。收到政策简报后，从以下三维审查：
1. 因果推断是否合理
2. 数据引用是否准确
3. 政策建议的约束条件是否明确
用一句话给出审查结论。审查完后说 TERMINATE。"""

_M3_MACRO_DATA = """\
请分析以下 2026 Q1 宏观数据并给出结构化摘要：

- GDP 同比增速：+5.2%
- 消费对 GDP 贡献率：68%
- 固定资产投资增速：+4.8%（高新技术 +12.3%）
- CPI：+0.8%，核心 CPI：+1.1%
- PPI：-0.9%（连续第 18 个月为负）
- 出口增速：+8.3%（对东盟 +15%，对欧盟 -2%）
- 社会消费品零售总额增速：+4.5%
- 全国调查失业率：5.1%（16-24 岁：14.7%）"""


def run_mode3_sequential_pipeline() -> tuple:
    """接力对话流水线。

    数据分析师 → 政策撰稿人 → 同行评审，三阶段接力。
    返回 (数据摘要, 政策简报, 审查结论)。
    """
    _section("模式 3: 接力对话 — 数据分析 → 政策简报 → 同行评审")

    user_proxy = ConversableAgent(
        name="user",
        system_message="你负责发起任务。",
        human_input_mode="NEVER",
    )

    # Stage 1: 数据分析
    data_analyst = ConversableAgent(
        name="data_analyst",
        system_message=_M3_DATA_ANALYST_PROMPT,
        llm_config=_llm_config,
    )
    chat_3a = user_proxy.initiate_chat(
        data_analyst,
        message=_M3_MACRO_DATA,
        max_turns=1,
        summary_method="reflection_with_llm",
    )
    data_summary = chat_3a.summary
    print(f"\n数据摘要:\n{data_summary}")

    # Stage 2: 政策简报
    policy_writer = ConversableAgent(
        name="policy_writer",
        system_message=_M3_POLICY_WRITER_PROMPT,
        llm_config=_llm_config,
    )
    chat_3b = user_proxy.initiate_chat(
        policy_writer,
        message=(
            f"请根据以下数据摘要，撰写政策简报：\n\n"
            f"【数据摘要】\n{data_summary}\n\n"
            f"【读者】非经济学背景的决策者\n"
            f"【要求】100 字以内，不含公式，给一个可操作的政策建议。"
        ),
        max_turns=1,
        summary_method="reflection_with_llm",
    )
    policy_brief = chat_3b.summary
    print(f"\n政策简报:\n{policy_brief}")

    # Stage 3: 同行评审
    peer_reviewer = ConversableAgent(
        name="peer_reviewer_s3",
        system_message=_M3_PEER_REVIEWER_PROMPT,
        llm_config=_llm_config,
    )
    chat_3c = user_proxy.initiate_chat(
        peer_reviewer,
        message=(
            f"请审查以下政策简报：\n\n{policy_brief}\n\n"
            f"审查维度：因果推断、数据准确性、政策约束条件。"
        ),
        max_turns=1,
        summary_method="reflection_with_llm",
    )
    review = chat_3c.summary
    print(f"\n同行评审:\n{review}")

    return data_summary, policy_brief, review


# ═══════════════════════════════════════════════════════════════════════
# 入口
# ═══════════════════════════════════════════════════════════════════════


def main() -> None:
    parser = argparse.ArgumentParser(
        description="EconResearchSquad — AG2 经济学多智能体研究小队"
    )
    parser.add_argument(
        "--mode",
        type=int,
        choices=[1, 2, 3],
        default=0,
        help="运行指定模式 (1/2/3)，默认运行全部三种模式",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  EconResearchSquad · C5-AG2")
    print("  经济学多智能体研究小队 — 基于 AG2 0.9.7")
    print(f"  API: {API_BASE}  Model: {MODEL}")
    print("=" * 60)

    if args.mode == 0 or args.mode == 1:
        run_mode1_lead_critic()

    if args.mode == 0 or args.mode == 2:
        run_mode2_group_chat()

    if args.mode == 0 or args.mode == 3:
        run_mode3_sequential_pipeline()

    _section("全部三种 AG2 多智能体模式演示完毕")


if __name__ == "__main__":
    main()
