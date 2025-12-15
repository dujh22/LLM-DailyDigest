+++
title = '[模版] 202X-XX-XX科研追新'
date = 2025-12-07T00:00:00+08:00
draft = false
toc = true
+++

# 2025-08-04科研追新

## 1. 源数据

## 1.1 媒体

**From**：量子位、机器之心、新智元、AGI Hunt、小红书、X其他


## 1.2 Huggingface


## 1.3 Arxiv

## 1.3.1 Computation and Language

**From：**[https://papers.cool/arxiv/cs.CL](https://papers.cool/arxiv/cs.CL))

[https://arxiv.org/list/cs.CL/recent](https://arxiv.org/list/cs.CL/recent)

[https://www.arxivdaily.com/cate/20/seq/0](https://www.arxivdaily.com/cate/20/seq/0)

### 文章三级标题

具体内容

### 文章三级标题

具体内容


## 1.3.2 Artificial Intelligence

**From**：[https://papers.cool/arxiv/cs.AI](https://papers.cool/arxiv/cs.AI)

[https://arxiv.org/list/cs.AI/recent](https://arxiv.org/list/cs.AI/recent)

[https://www.arxivdaily.com/cate/21/seq/0](https://www.arxivdaily.com/cate/21/seq/0)


### 文章三级标题

具体内容

### 文章三级标题

具体内容


## 2. 归类后数据


## 3. 其他

正则表达式删除无关字符串

```
#

\[\S*\]\s+\[\S*\]\s+\[\S*\]\s+\[\S*\]

\[PDF\d*\] \[Copy\d*\] \[Kimi\d*\] \[REL\d*\]
\[PDF \d*\] \[Copy\d*\] \[Kimi \d*\] \[REL\d*\]

\[PDF( \d+)? \] \[复制\] \[Kimi( \d+)? \] \[(?:REL|相关)\]
```

图片插入

```
![](https://gitee.com/dujh22/pic/raw/master/logicReason/SLR.png)
```
