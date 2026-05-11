# Demo 视频录制脚本 · EconResearchSquad

> 目标时长：80-90 秒 | 语言：中文 | 格式：Loom 录屏 + 语音

---

## 录制前准备

```bash
# 1. 确认环境正常
cd ~/Documents/Elite20_Anshuwei/challenges/C5-AG2
python src/econ_research_squad.py --mode 1   # 预跑一次，确保 API 正常

# 2. 清屏，调整终端字体大小（建议 14pt+，Loom 观看者手机居多）

# 3. 关闭通知、清理桌面、准备好计时器
```

---

## 逐秒脚本

### 0:00–0:10 | 开场：项目定位

**画面**: 终端 + README.md 滚动

**口播**:
> "EconResearchSquad——基于 AG2 的经济学多智能体研究小队。输入宏观数据，输出政策简报。演示三种 AG2 多智能体协作模式。"

**操作**: 
```bash
cat README.md | head -15
```

---

### 0:10–0:30 | Mode 1: Lead + Critic 双 Agent 审查回路

**画面**: 运行 Mode 1，展示审查过程

**口播**:
> "模式一：Lead 经济学评论员撰写评论，Critic 同行评审从因果推断、数据准确性、政策约束条件三个维度审查。看——初始审查三个维度全部不通过，评论员拿到反馈后自动修正，第二轮三个维度全部通过。这就是迭代修正回路。"

**操作**:
```bash
python src/econ_research_squad.py --mode 1
```

**关键画面**: 命令行输出中高亮以下内容（在终端中自然滚动即可）：
```
1. 因果推断：不通过 → ...修正后... 通过
2. 数据引用：通过
3. 政策建议：不通过 → ...修正后... 通过
```

---

### 0:30–0:55 | Mode 2: Group Chat 自动路由

**画面**: 运行 Mode 2，展示五个 Agent 自动协作

**口播**:
> "模式二：Group Chat 自动路由。首席经济学家协调增长、物价、外贸三个专员并行分析中国 2026 Q1 宏观数据。注意——发言人完全由 LLM 自动选择，不需要人工调度。最后 Coordinator 整合三位专员的分析，输出宏观经济总览。"

**操作**:
```bash
python src/econ_research_squad.py --mode 2
```

**关键画面**: 滚动展示每个 Agent 的发言（growth_specialist → price_specialist → trade_specialist → chief_economist）

---

### 0:55–1:15 | Mode 3: 接力流水线

**画面**: 运行 Mode 3，展示三阶段接力

**口播**:
> "模式三：接力对话流水线。数据分析师提取关键趋势、政策撰稿人转为通俗简报、同行评审最后把关。三阶段链式传递，每个阶段拿到上一棒的输出继续加工。最终产出——面向非经济学决策者的 100 字政策简报。"

**操作**:
```bash
python src/econ_research_squad.py --mode 3
```

**关键画面**: 三段输出依次出现（数据摘要 → 政策简报 → 同行评审结论）

---

### 1:15–1:25 | 架构总结

**画面**: 切回 README 架构图部分

**口播**:
> "总共 6 个 Agent——Coordinator + 三个垂直专员 + Policy Writer + Peer Reviewer。拿来自 AG2 Hackathon 获奖项目 parallel-research，用 AG2 0.9.7 稳定 API 重写。仓库公开，README 有 Quick Start，5 分钟可复现。"

**操作**:
```bash
cat README.md | grep -A 20 "Architecture"
```

---

### 1:25–1:30 | 结束

**画面**: GitHub repo 页面

**口播**:
> "安书伟，C5-AG2，multi-agent 赛道。谢谢。"

---

## 总时长控制

| 段落 | 时间 | 累计 |
|------|------|------|
| 开场 | 0:00–0:10 | 10s |
| Mode 1 | 0:10–0:30 | 30s |
| Mode 2 | 0:30–0:55 | 55s |
| Mode 3 | 0:55–1:15 | 75s |
| 架构总结 | 1:15–1:25 | 85s |
| 结束 | 1:25–1:30 | 90s |

---

## 备用简化版（75 秒，如果终端输出慢）

如果担心 LLM 响应慢导致超时，可以预跑并录制终端回放：

```bash
# 预跑，保存完整输出
python src/econ_research_squad.py 2>&1 | tee /tmp/demo_output.txt

# 录制时用 cat 分段展示（保证节奏可控）
cat /tmp/demo_output.txt | head -40    # Mode 1
sleep 1
cat /tmp/demo_output.txt | sed -n '41,80p'   # Mode 2
sleep 1
cat /tmp/demo_output.txt | tail -40    # Mode 3
```

**简化口播** (75s):
- 0:00–0:08 开场
- 0:08–0:24 Mode 1
- 0:24–0:44 Mode 2
- 0:44–1:04 Mode 3
- 1:04–1:10 总结
- 1:10–1:15 结束

---

## Loom 上传清单

- [ ] 标题: `C5-AG2: EconResearchSquad — AG2 经济学多智能体研究小队`
- [ ] 权限: **"Anyone with the link can view"**（必须，否则评审判无效）
- [ ] 描述中粘贴 repo URL: `https://github.com/Anshuwei/ai-x-elite20-teaching-materials/tree/main/challenges/C5-AG2`
- [ ] 录制后回看一次，确认音频清晰、终端字体可读
