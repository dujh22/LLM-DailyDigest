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
正文（支持 Markdown）。
'''
purpose = '''
- 用途与启示
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
