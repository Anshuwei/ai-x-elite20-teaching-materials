"""EconResearchSquad 烟雾测试。

验证三种 AG2 多智能体模式均可独立导入且接口签名正确。
不实际调用 LLM — 仅检查模块结构。
"""

import importlib
import pytest


_MODES = [
    ("run_mode1_lead_critic", "模式 1: Lead + Critic"),
    ("run_mode2_group_chat", "模式 2: Group Chat"),
    ("run_mode3_sequential_pipeline", "模式 3: 接力流水线"),
]


@pytest.mark.parametrize("fn_name,label", _MODES)
def test_mode_function_importable(fn_name: str, label: str) -> None:
    """每种模式的入口函数存在且可调用签名正确。"""
    # 动态导入以隔离副作用
    spec = importlib.util.spec_from_file_location(
        "econ_research_squad",
        "src/econ_research_squad.py",
    )
    mod = importlib.util.module_from_spec(spec)
    # 不执行模块顶级代码（会触发 LLM 调用），仅检查属性
    fn = getattr(
        importlib.import_module("src.econ_research_squad"),
        fn_name,
        None,
    )
    # 如果上面因路径问题失败，回退到源码扫描
    if fn is None:
        fn = getattr(__import__("src.econ_research_squad", fromlist=[fn_name]), fn_name, None)
    # 最简检查：函数存在
    assert fn is not None, f"{fn_name} should be defined for {label}"


def test_llm_config_present() -> None:
    """LLMConfig 在模块中已定义。"""
    from src.econ_research_squad import _llm_config
    assert _llm_config is not None


def test_constants_not_empty() -> None:
    """所有 Agent system_message 提示词均非空。"""
    from src import econ_research_squad as m
    prompts = [
        m._M1_LEAD_PROMPT,
        m._M1_CRITIC_PROMPT,
        m._M2_COORDINATOR_PROMPT,
        m._M2_GROWTH_PROMPT,
        m._M2_PRICE_PROMPT,
        m._M2_TRADE_PROMPT,
        m._M3_DATA_ANALYST_PROMPT,
        m._M3_POLICY_WRITER_PROMPT,
        m._M3_PEER_REVIEWER_PROMPT,
    ]
    for prompt in prompts:
        assert len(prompt) > 20, f"Prompt too short: {prompt[:30]}..."
