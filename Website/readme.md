# 更新到在线系统

## 1. 项目构建

```
hugo --theme=FixIt --baseURL="https://dujh22.github.io/LLMDailyDigest.github.io/" --buildDrafts
```

## 2. 运行测试

```text
hugo server -D
```

## 3. 上传部署

首先下载仓库https://github.com/dujh22/LLMDailyDigest.github.io

然后执行如下操作

```
cp -rf ./public/* /Users/djh/Documents/备份/一般/工作/代码/LLM/github/LLMDailyDigest.github.io/

cd /Users/djh/Documents/备份/一般/工作/代码/LLM/github/LLMDailyDigest.github.io

git add *

git commit -m "20250804"

git push -u origin master
```
