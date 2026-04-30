# Day 3 速查表 — SSH Key & PAT 配置

**打印出来，人手一份。这是 D3 最大的瓶颈。**

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
# 一路按 Enter 即可（不设密码也可以）
```

### 3. 复制公钥

**Mac:**
```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

**Windows (Git Bash):**
```bash
cat ~/.ssh/id_ed25519.pub | clip
```

### 4. 添加到 GitHub

1. 浏览器打开 https://github.com/settings/keys
2. 点击绿色 "New SSH key"
3. Title 写 `教室电脑`
4. Key 粘贴（Cmd+V 或 Ctrl+V）
5. 点 "Add SSH key"

### 5. 测试

```bash
ssh -T git@github.com
```

看到 `Hi <你的用户名>! You've successfully authenticated` 就成功了。

---

## 方案 B — Personal Access Token（如果 SSH 5分钟内搞不定）

### 如果你已经用 `gh auth login` 登录了 GitHub CLI

```bash
# 配置 git 用 gh 作为凭证助手
gh auth setup-git

# 验证
gh auth status
```

之后 `git push` / `git pull` 会自动用 token，**不用再做任何事**。

### 如果 gh CLI 也没配置好

1. 浏览器打开 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. Note 写 `Elite20教室`
4. 勾选 `repo`（全部）和 `workflow`
5. 生成，**复制 token（离开页面后就看不到了）**
6. 在终端：
```bash
git config --global credential.helper osxkeychain   # Mac
# 或
git config --global credential.helper manager       # Windows
```
7. 下次 `git push` 时输入用户名和刚才的 token（token 当作密码输入）

---

## 常见错误速查

| 错误信息 | 原因 | 解决 |
|----------|------|------|
| `Permission denied (publickey)` | SSH key 没加到 GitHub | 重新执行方案A第3-5步 |
| `remote: Invalid username or password` | 用密码而不用 token | GitHub 已经不支持密码——必须用 token |
| `fatal: not a git repository` | 你在错误的文件夹里 | `cd` 到 clone 下来的仓库文件夹 |
| `remote: Repository not found` | 仓库名拼错或没权限 | 检查 fork 是否成功，仓库 URL 是否正确 |
| `fatal: unable to access ... SSL certificate problem` | 学校网络有代理 | 找 TA 帮配置 `http.proxy` |
