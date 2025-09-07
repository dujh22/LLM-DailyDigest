# 更新到在线系统

```
rm -r ./public
```

## 1. 项目构建

```
hugo --theme=FixIt --baseURL="https://dujh22.github.io/LLMDailyDigestWeb/" --buildDrafts
```

## 2. 运行测试

```text
hugo server -D
```

## 3. 上传部署

首先下载仓库https://github.com/dujh22/LLMDailyDigestWeb

然后执行如下操作

```
find ./public -type f -name '*.cfg' -delete

cp -rf ./public/* /Users/djh/Documents/备份/一般/工作/代码/LLM/github/LLMDailyDigestWeb/

cd /Users/djh/Documents/备份/一般/工作/代码/LLM/github/LLMDailyDigestWeb

find ./ -type f -name '*.cfg' -delete

git add *

git commit -m "20250815"

git push -u origin master
```
