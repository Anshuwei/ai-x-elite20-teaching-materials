#!/usr/bin/env bash
# ─── EconResearchSquad 一键复现 ───────────────────────────────────
# ./scripts/reproduce.sh  将依次运行三种 AG2 多智能体模式
set -euo pipefail

cd "$(dirname "$0")/.."

echo "═══ EconResearchSquad · C5-AG2 复现脚本 ═══"
echo ""

# 检查虚拟环境
if [ ! -d ".venv" ]; then
    echo "[1/3] 创建虚拟环境 ..."
    python3 -m venv .venv
fi

source .venv/bin/activate

echo "[2/3] 安装依赖 ..."
pip install -q -r requirements.txt

echo "[3/3] 运行三种 AG2 多智能体模式 ..."
echo ""
python src/econ_research_squad.py

echo ""
echo "═══ 复现完毕 ═══"
