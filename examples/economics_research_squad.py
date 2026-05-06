"""
经济学研究小队 — AG2 0.9.x 多智能体示例
Economics Research Squad — AG2 Multi-Agent Demo

基于 AG2 0.9.7 稳定 API，演示三种多智能体协作模式：
1. 双 Agent 对话 — Lead 撰写 + Critic 审查
2. Group Chat 自动路由 — Coordinator + 三个经济学专员
3. 接力对话 — 数据分析师 → 政策撰稿人 流水线

经济学场景：分析中国 2026 Q1 宏观经济数据，生成政策简报。
"""

import os

from autogen import ConversableAgent, LLMConfig
from autogen.agentchat import initiate_group_chat
from autogen.agentchat.group.patterns import AutoPattern

# ─── 配置：DeepSeek API（OpenAI 兼容） ──────────────────────────────
API_BASE = "https://api.deepseek.com/v1"
API_KEY = os.environ.get("ANTHROPIC_AUTH_TOKEN", "sk-d5df08faf04f4e9d8ee403165565d741")
MODEL = "deepseek-chat"

llm_config = LLMConfig(
    api_type="openai",
    model=MODEL,
    api_key=API_KEY,
    base_url=API_BASE,
    temperature=0.7,
)


def section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


# ═══════════════════════════════════════════════════════════════════
# 模式 1：双 Agent 对话 — Lead + Critic
# Lead 撰写经济学评论，Critic 审查并反馈
# ═══════════════════════════════════════════════════════════════════
section("模式 1: Lead + Critic 双 Agent 审查回路")

lead_analyst = ConversableAgent(
    name="lead_analyst",
    system_message=(
        "你是一位资深经济学评论员。给定一个经济话题和具体数据，"
        "撰写一段 120 字以内的中文评论。结构：\n"
        "1. 一个核心判断\n"
        "2. 一个数据支撑\n"
        "3. 一个政策含义\n"
        "不要使用公式。评论写完后说 TERMINATE。"
    ),
    llm_config=llm_config,
)

critic = ConversableAgent(
    name="peer_reviewer",
    system_message=(
        "你是一位经济学同行评审。收到评论后，用中文检查三个维度：\n"
        "1. 因果推断是否合理（相关 ≠ 因果）\n"
        "2. 数据引用是否准确\n"
        "3. 政策建议是否有明确的约束条件\n"
        "每个维度给出判定（通过/不通过）和一句话理由。"
        "审查完后说 TERMINATE。"
    ),
    llm_config=llm_config,
)

chat_result_1 = lead_analyst.initiate_chat(
    critic,
    message=(
        "请审阅我的经济学评论：\n\n"
        "'中国 2026 Q1 高新技术产业投资同比增长 12.3%，"
        "远超整体固定资产投资增速 4.8%。这表明中国正在经历"
        "显著的投资结构转型：从传统基建和房地产驱动，"
        "转向以芯片、新能源、AI 为核心的先进制造业驱动。"
        "政策含义是，财政刺激应该更精准地投向技术扩散环节，"
        "而非简单地扩大总量投资。'\n\n"
        "请逐维度审查。"
    ),
    max_turns=2,
)
print(f"\n📝 审查结果:\n{chat_result_1.summary if chat_result_1.summary else '（见上方对话）'}")


# ═══════════════════════════════════════════════════════════════════
# 模式 2：Group Chat — Coordinator + 三个经济学专员
# AutoPattern：LLM 自动选择下一个发言人
# ═══════════════════════════════════════════════════════════════════
section("模式 2: Group Chat — 宏观经济分析三人组")

coordinator = ConversableAgent(
    name="chief_economist",
    system_message=(
        "你是首席经济学家。你收到三个专员的分析后，"
        "整合成一段 150 字以内的中文宏观经济总览。"
        "总结后说 TERMINATE。"
    ),
    llm_config=llm_config,
)

growth_specialist = ConversableAgent(
    name="growth_specialist",
    system_message=(
        "你是经济增长分析师。关注 GDP 增长、消费、投资数据。"
        "用 60 字以内中文回答，给关键数据 + 一句话判断。"
    ),
    llm_config=llm_config,
)

price_specialist = ConversableAgent(
    name="price_specialist",
    system_message=(
        "你是物价分析师。关注 CPI、PPI、通胀预期。"
        "用 60 字以内中文回答，判断通缩/通胀压力。"
    ),
    llm_config=llm_config,
)

trade_specialist = ConversableAgent(
    name="trade_specialist",
    system_message=(
        "你是外贸分析师。关注出口、汇率、资本流动。"
        "用 60 字以内中文回答，评估外需前景和汇率影响。"
    ),
    llm_config=llm_config,
)

user_proxy = ConversableAgent(
    name="user",
    system_message="你负责发起讨论。",
    human_input_mode="NEVER",
)

pattern = AutoPattern(
    initial_agent=coordinator,
    agents=[coordinator, growth_specialist, price_specialist, trade_specialist],
    user_agent=user_proxy,
    group_manager_args={"llm_config": llm_config},
)

result, context, last_agent = initiate_group_chat(
    pattern=pattern,
    messages=(
        "我们来分析中国 2026 Q1 宏观经济状况。\n"
        "数据：GDP 同比 +5.2%，消费贡献率 68%，高新技术投资 +12.3%，"
        "固定资产投资 +4.8%，CPI +0.8%，PPI -0.9%，出口 +8.3%（对东盟 +15%），"
        "人民币兑美元 7.10，社会消费品零售 +4.5%，调查失业率 5.1%。\n\n"
        "请 growth_specialist 先分析增长驱动力，"
        "然后 price_specialist 分析物价走势，"
        "然后 trade_specialist 分析外贸形势。"
        "最后 chief_economist 整合所有发现给出总览。"
    ),
    max_rounds=10,
)
print(f"\n📊 Group Chat 结束。最后发言人: {last_agent.name}")


# ═══════════════════════════════════════════════════════════════════
# 模式 3：接力对话 — 数据分析 → 政策撰稿 流水线
# Agent A 分析 → Agent B 拿到结果继续写
# ═══════════════════════════════════════════════════════════════════
section("模式 3: 接力对话 — 数据分析 → 政策简报")

data_analyst = ConversableAgent(
    name="data_analyst",
    system_message=(
        "你是一位宏观经济数据分析师。给定数据，提取关键趋势，"
        "识别值得关注的信号。用中文输出结构化数据摘要。"
        "最后说 TERMINATE。"
    ),
    llm_config=llm_config,
)

policy_writer = ConversableAgent(
    name="policy_writer",
    system_message=(
        "你是一位经济政策撰稿人。拿到数据分析师的结构化摘要后，"
        "撰写一份面向非经济学背景决策者的中文政策简报。\n"
        "要求：100 字以内，语言通俗，不出现公式，"
        "包含：总体判断 + 两个关键信号 + 一个可操作的政策建议。"
        "写完后说 TERMINATE。"
    ),
    llm_config=llm_config,
)

# Step 1: 数据分析
chat_3a = user_proxy.initiate_chat(
    data_analyst,
    message=(
        "请分析以下 2026 Q1 宏观数据并给出结构化摘要：\n\n"
        "- GDP 同比增速：+5.2%\n"
        "- 消费对 GDP 贡献率：68%\n"
        "- 固定资产投资增速：+4.8%（高新技术 +12.3%）\n"
        "- CPI：+0.8%，核心 CPI：+1.1%\n"
        "- PPI：-0.9%（连续第 18 个月为负）\n"
        "- 出口增速：+8.3%（对东盟 +15%，对欧盟 -2%）\n"
        "- 社会消费品零售总额增速：+4.5%\n"
        "- 全国调查失业率：5.1%（16-24 岁：14.7%）\n"
    ),
    max_turns=1,
    summary_method="reflection_with_llm",
)

data_summary = chat_3a.summary
print(f"\n📊 数据摘要:\n{data_summary}")

# Step 2: 政策撰稿，拿到数据摘要后写简报
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

print(f"\n📋 政策简报:\n{chat_3b.summary}")

section("✅ 全部三种 AG2 多智能体模式演示完毕")
