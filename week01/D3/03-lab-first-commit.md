# Day 3 实验 — 你的第一次提交

**时长：** 30分钟 | **轨道：** T3 + T2

---

## 学生指令（逐步骤、大字投影）

### Step 1 — Fork 课程仓库（5分钟）

1. 浏览器打开课程仓库：`github.com/ai-x-elite/elite20-starter` ⚠️实际URL以你的为准
2. 点击右上角 **Fork** 按钮
3. Owner 选你自己的 GitHub 账号
4. 点 "Create fork"

✅ 检查：浏览器地址栏变成 `github.com/<你的用户名>/elite20-starter`

---

### Step 2 — Clone 到本地 + 配置认证（10分钟）

> ⚠️ 这一步最容易卡。拿出 SSH/PAT 速查表。

**如果你用 SSH（推荐）：**

```bash
cd ~/Desktop
git clone git@github.com:<你的用户名>/elite20-starter.git
cd elite20-starter
```

**如果你用 gh CLI（备选）：**

```bash
cd ~/Desktop
gh repo clone <你的用户名>/elite20-starter
cd elite20-starter
```

如果卡在认证这一步 **超过5分钟**，举手找 TA。

---

### Step 3 — 放入 Day 2 的截图（5分钟）

**方式A — 终端：**
```bash
mkdir -p students/<你的名字>
cp ~/Desktop/Elite20_<你的名字>/screenshots/D2-hello.png students/<你的名字>/
```

**方式B — 文件管理器：**
1. 在 `elite20-starter` 文件夹里找到 `students/` 目录
2. 如果里面没有你的名字的文件夹，新建一个
3. 把 Day 2 的 `D2-hello.png` 复制进去

---

### Step 4 — 第一次提交（5分钟）

```bash
git add students/<你的名字>/
git commit -m "D3: 添加 Day 2 工作坊截图 - hello.md 烟雾测试通过"
git push
```

> 📝 **Commit message 格式：** `D3: <你做了什么改动>`
> 就像在实验笔记本上写日期和内容一样。

---

### Step 5 — 验证（5分钟）

1. 浏览器打开 `github.com/<你的用户名>/elite20-starter`
2. 点 "commits"（在代码页面上方）
3. 你应该看到自己刚做的 commit，写着 `D3: ...`
4. **截个图，发到班级群**

---

## Close — "欣赏你自己的提交"

> "打开 GitHub，点进 Commits 页面。那一条绿色的记录，有你的名字，有时间戳，有你的改动。这是你在这个项目里的第一页实验笔记。保存这个页面——Week 10 回头看，你会惊讶。"
