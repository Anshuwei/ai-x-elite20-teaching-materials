# Appendix A — 工具检查清单

**使用时间：** D1 之前完成初始检查，D5 之前完成二次检查
**参考来源：** 安书伟老师实际配置经验（2026年4月）

---

## D1 之前 — 初始检查（逐人逐项）

| 学生姓名 | GitHub 账号 | gh CLI 就绪 | Claude Code 已安装 | Claude 桌面可用 | 终端可用 | 微信群已加入 | 仓库邀请已接受 | npm 镜像已配置 |
|----------|------------|------------|-------------------|----------------|---------|------------|-------------|--------------|
| | | | | | | | | |
| | | | | | | | | |

### 检查方式
- **GitHub 账号：** 学生是否能登录 github.com
- **gh CLI：** 终端运行 `gh --version` 应输出版本号（推荐 2.x）；`gh auth status` 显示已登录
- **Claude Code：** 终端运行 `claude --version` 应输出版本号（安书伟老师环境: 2.1.123）
- **Claude 桌面：** 打开 Claude 桌面应用，发送一条消息
- **终端：** 运行 `git --version` 和 `node --version` 都能正常输出
- **微信群：** 在群里看到该学生
- **仓库邀请：** GitHub 通知中有 elite20-starter 的邀请
- **npm 镜像：** `npm config get registry` 应输出 `https://registry.npmmirror.com`

### 常见问题速修

| 问题 | 修复方案 |
|------|---------|
| 没装 Claude Code | `sudo npm install -g @anthropic-ai/claude-code`（需先配 npm 镜像） |
| 没装 gh CLI（Mac） | `brew install gh` |
| gh CLI 未认证 | `gh auth login` → 选 GitHub.com → HTTPS → 浏览器登录 |
| npm 下载慢/失败 | `npm config set registry https://registry.npmmirror.com` |
| npm 全局安装权限不足 | 加 `sudo`：`sudo npm install -g @anthropic-ai/claude-code` |
| Windows 无 Git-Bash | 安装 Git for Windows (含 Git-Bash) |
| SSH key 不会生成 | 切到 gh CLI 方案：`gh auth setup-git` 自动配置凭证 |
| 仓库邀请过期 | 在 GitHub 上重新发送 |

### 认证方案优先级

1. **首选：gh CLI** — `brew install gh` → `gh auth login` → `gh auth setup-git`（安书伟老师实际使用方案）
2. **备选：SSH Key** — `ssh-keygen -t ed25519` → 添加公钥到 GitHub → `ssh -T git@github.com` 测试
3. **不推荐：手动 PAT** — 容易输错、容易泄露

---

## D5 之前 — 二次检查（确认全员绿灯）

| 学生姓名 | GitHub fork 有 ≥1 commit | D2 截图已发群 | D4 三个提示词已提交 | D5 Skill 产物可确认 | 整体状态 |
|----------|-------------------------|--------------|-------------------|-------------------|---------|
| | | | | | 🟢/🟡/🔴 |
| | | | | | 🟢/🟡/🔴 |

### 状态含义
- 🟢 全部通过：Week 2 可以正常学习
- 🟡 缺 1 项：微信 DM 提醒，周六补交
- 🔴 缺 ≥2 项：周五晚 TA 1:1 补课

### "没人掉队"行动（周五傍晚）
1. TA 分工，每人负责 5-6 个学生
2. 对照清单逐人检查
3. 🔴 的当下联系，安排当天晚上补课（30-45分钟）
4. 🟡 的发微信："你还差[具体哪项]，周六中午前提交就行，需要帮忙可以找我"
5. 确认全部 🟢 后再开始 Week 2

---

## 教室网络检查（D1 前）

- [ ] GitHub 在教室网络下能正常访问
- [ ] Claude Code / Claude 桌面在教室网络下能正常对话
- [ ] npm registry（npmmirror.com）可访问
- [ ] 投影 / 投屏设备正常
- [ ] 备用热点（手机热点）就绪——以防教室网络挂了

---

## 联系方式

| 角色 | 姓名 | 微信 | 电话 |
|------|------|------|------|
| 主讲教师 | 安书伟 | | |
| TA-1 | | | |
| TA-2 | | | |
| TA-3 | | | |
| 技术支持 | | | |
