# 更新到在线系统

> 线上地址：https://dujh22.github.io/LLMDailyDigestWeb/
>
> - 源仓库（Hugo 源码）：`dujh22/LLM-DailyDigest`
> - 部署仓库（GitHub Pages 托管构建产物）：`dujh22/LLMDailyDigestWeb`

---

## ✅ 自动部署（推荐，已配置）

已通过 **GitHub Actions** 实现全自动部署，无需手动构建或拷贝。

**工作原理**：当你把改动 push 到源仓库 `LLM-DailyDigest` 的 `main` 分支时（任一台电脑均可），GitHub 会自动：

1. 拉取源码 → 用 Hugo 构建（`--theme=FixIt --buildDrafts`）
2. 生成 `.nojekyll`（**关键**：跳过 GitHub Pages 默认的 Jekyll 构建，否则会因主题资源文件报 `Page build failed`）
3. 用 SSH deploy key 把 `public/` 推送到部署仓库 `LLMDailyDigestWeb:master`
4. GitHub Pages 自动发布上线（约几十秒）

**日常更新只需**：

```bash
# 改完 content/ 、layouts/ 、hugo.toml 等
git add -A
git commit -m "update xxx"
git push
# 几十秒后网站自动更新
```

- 触发范围见 `.github/workflows/deploy.yml`：`content/`、`layouts/`、`assets/`、`archetypes/`、`static/`、`themes/`、`hugo.toml`、工作流本身的改动才会触发（改 `backend/`、`tools/`、`README` 等不会）。
- 也可在 GitHub 仓库 → **Actions** → **Deploy site** → **Run workflow** 手动触发。
- 查看运行状态：源仓库的 **Actions** 标签页。

---

## 💻 在另一台电脑上使用（如个人机）

**不需要重新配置自动部署**。Actions 工作流、SSH deploy key、secret 都存在 GitHub 上，与本地电脑无关。任何能 push 到源仓库 `main` 的机器都会触发自动部署。

个人机上的准备：

1. **克隆源仓库**（注意是源仓库，不是部署仓库）：

   ```bash
   git clone git@github.com:dujh22/LLM-DailyDigest.git
   ```

2. **本地预览（可选）**：安装 [Hugo extended](https://gohugo.io/installation/)（版本 ≥ 0.148.2），然后：

   ```bash
   hugo server -D
   ```

   预览**非必须**；即使不装 Hugo，直接 push 也会由 GitHub 自动构建发布。

3. 改完直接 `git push`，网站自动更新。

> 旧的手动流程（下方）已不再需要，**包括本地 `LLMDailyDigestWeb` 目录的拷贝**。个人机上原本 `cp` 到 `LLMDailyDigestWeb` 的步骤可以完全省略。

---

## 📎 附：自动部署的一次性配置（仅供参考，已完成）

如需在新仓库复刻这套自动部署，按以下步骤（本项目已完成，无需重复）：

1. 生成 SSH 密钥对（仅用于部署，最小权限）：

   ```bash
   ssh-keygen -t ed25519 -C "gha-deploy" -f deploy_key
   ```

2. 公钥加到**部署仓库** `LLMDailyDigestWeb` 作为**可写** deploy key：

   ```bash
   gh repo deploy-key add deploy_key.pub \
     --repo dujh22/LLMDailyDigestWeb \
     --title "gha-deploy" --allow-write
   ```

3. 私钥作为 secret 加到**源仓库** `LLM-DailyDigest`：

   ```bash
   gh secret set ACTIONS_DEPLOY_KEY --repo dujh22/LLM-DailyDigest < deploy_key
   rm -f deploy_key deploy_key.pub   # 本地副本用完即删
   ```

4. 在源仓库添加 `.github/workflows/deploy.yml`（见仓库实际文件）。

---

## ⚠️ 手动部署流程（已弃用，保留备查）

> 以下手动流程已被上方的「自动部署」取代。**仅在自动部署出问题、或想本地验证时参考。** 正常情况下请直接用上面的 `git push` 自动部署。

```
rm -r ./public
```

### 1. 项目构建

```
hugo --theme=FixIt --baseURL="https://dujh22.github.io/LLMDailyDigestWeb/" --buildDrafts
```

> 注意：手动部署时记得在 `public/` 下手动 `touch .nojekyll`，否则 GitHub Pages 的 Jekyll 构建会失败。

### 2. 运行测试

```text
hugo server -D
```

### 3. 上传部署（已弃用）

首先下载仓库 https://github.com/dujh22/LLMDailyDigestWeb

然后执行如下操作

公司机：

```bash
find ./public -type f -name '*.cfg' -delete
cp -rf ./public/* /Users/djh/Documents/备份/一般/工作/代码/LLM/github/LLMDailyDigestWeb/
cd /Users/djh/Documents/备份/一般/工作/代码/LLM/github/LLMDailyDigestWeb
find ./ -type f -name '*.cfg' -delete
git add *
git commit -m "new"
git push -u origin master
```

个人机：

```bash
find ./public -type f -name '*.cfg' -delete
cp -rf ./public/* /Users/pika/Documents/pika/备份/Code/Github/LLMDailyDigestWeb/
cd /Users/pika/Documents/pika/备份/Code/Github/LLMDailyDigestWeb/
find ./ -type f -name '*.cfg' -delete
git add *
git commit -m "new"
git push -u origin master
```
