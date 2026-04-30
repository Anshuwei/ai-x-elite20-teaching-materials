# Day 3 速查表 — SSH Key & PAT 配置

**打印出来，人手一份。这是 D3 最大的瓶颈。**
**参考来源：** 安书伟老师实际配置 Claude Code 的经验（2026年4月）

---

## 前置检查：你的环境就绪了吗？

```bash
git --version      # 应输出 git version 2.x.x
node --version     # 应输出 v25.x 或类似（Claude Code 需要 Node）
```

---

## 方案 A — SSH Key（推荐，一劳永逸）

### 1. 检查是否已有 SSH Key

```bash
ls ~/.ssh/id_ed25519.pub
```

如果文件存在，跳到第3步。如果不存在，继续第2步。

### 2. 生成新的 SSH Key

```bash
ssh-keygen -t ed25519 -C "你的GitHub注册邮箱"
# 一路按 Enter 即可
```

### 3. 复制公钥（Mac）

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

### 4. 添加到 GitHub
浏览器打开 https://github.com/settings/keys → New SSH key → 粘贴

### 5. 测试

```bash
ssh -T git@github.com
# 看到 Hi <用户名>! You've successfully authenticated 即成功
```

---

## 方案 B — GitHub CLI（安书伟老师实际使用方案）

### 安装 gh

```bash
# Mac
brew install gh

# 验证
gh --version
```

### 认证

```bash
gh auth login
# 选择 GitHub.com → HTTPS → 用浏览器登录
# 或使用 token: echo "ghp_xxx" | gh auth login --with-token
```

### 配置 git 使用 gh 作为凭证助手

```bash
gh auth setup-git
```

之后 `git push` / `git pull` / `git clone` 自动使用 token，不用反复输入密码。

### 日常使用

```bash
gh repo clone <用户名>/<仓库名>     # 克隆仓库
gh repo create <仓库名> --public --push  # 创建仓库并推送
gh auth status                      # 检查认证状态
```

---

## 常见错误速查（安书伟老师实际遇到过的）

| 错误信息 | 原因 | 解决 |
|----------|------|------|
| `Permission denied (publickey)` | SSH key 没加到 GitHub | 切到方案B（gh CLI）|
| `remote: Invalid username or password` | 密码登录已不支持 | GitHub 已不支持密码——用 token 或 gh CLI |
| `npm error EACCES: permission denied` | npm 全局安装权限不足 | `sudo npm install -g @anthropic-ai/claude-code` |
| `fatal: not a git repository` | 你在错误的文件夹里 | `cd` 到 clone 下来的仓库 |
| npm 下载慢 | 默认 registry 在国外 | `npm config set registry https://registry.npmmirror.com` |

---

## Claude Code 安装（如需）

```bash
# 设置国内镜像加速
npm config set registry https://registry.npmmirror.com

# 安装
sudo npm install -g @anthropic-ai/claude-code

# 验证
claude --version
# 安书伟老师环境: 2.1.123 (Claude Code)
```
