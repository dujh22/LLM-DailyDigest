+++
title = '{{ replace .Name "-" " " | title }} 科研追新'
date = {{ .Date }}
draft = false
toc = true
+++

> 当日综述（可选，正文会显示在日报顶部）。

[[items]]
id = 'change-me'
title = '消息标题'
subtopic = '子主题（决定在主题页的栏目）'
topics = ['主题名']            # 须与 content/topic/ 文件名一致
research = []                  # 归属研究项目，可多选或留空；取值见 content/research/（如 LogicEvolve）
source = '来源'
summary = '一句话摘要'
paper = ''
code = ''
dataset = ''
link = ''
content = '''
- **问题**：……
- **旧法为何失效**：……
- **方法**：……
- **实验**：……
'''
purpose = '用途：一句话，用在哪里 / 如何用'
insight = '启示：一句话，最核心的新洞见'
notes = '''                # 可选：原始逐字笔记（迁移脚本自动填，保留原文不浓缩）
'''

[[items]]
id = 'change-me-2'
title = '第二条消息标题'
subtopic = '另一子主题'
topics = ['主题名']
source = '来源'
summary = '一句话摘要'
paper = ''
code = ''
dataset = ''
link = ''
content = '''
正文。
'''
