import pandas as pd
from datetime import datetime
import argparse
import os
from collections import defaultdict
import textwrap
import ast
import csv

# 配置参数
DAILY_REPORT_DIR = "/Users/djh/Documents/GitHub/LLM-DailyDigest/updates"
TOP_N_TRENDING = 5 # 显示最热门论文的数量
THEME_KEYWORDS_OR = {
    "大模型": [
        "大模型", "语言模型", "LLM", "生成式模型", "自监督学习", "Transformer", 
        "预训练", "微调", "强化学习", "多模态"
    ],
    "推理": [
        "推理", "o1", "数学", "代码"
    ],
    "测评": [
        "测评", "评估", "评测", "验证"
    ],
    "泛化": [
        "泛化", "迁移学习", "领域适应", "多任务学习", "多模态学习", "自回归学习"
    ],
    "数据": [
        "数据增强", "数据", "标注", "多模态数据", "清洗"
    ],
    "人工智能伦理与社会": [
        "伦理", "可解释性", "公平性", "算法偏见", "自动化决策", "隐私保护", 
        "社会影响", "AI治理", "算法透明度"
    ],
    "多模态": [
        "多模态", "视觉", "语音", "图像", "视频", "音频", "图谱"
    ]
}
THEME_KEYWORDS_AND = {
    "大模型推理": [
        {"大模型", "推理"}, 
        {"语言模型", "推理"}, 
        {"LLM", "推理"},
    ],
    "大模型数学推理": [
        {"大模型", "数学", "推理"},
        {"语言模型", "数学", "推理"},
        {"LLM", "数学", "推理"}
    ],
    "大模型代码推理": [
        {"大模型", "代码", "推理"},
        {"语言模型", "代码", "推理"},
        {"LLM", "代码", "推理"}
    ],
    "大模型类o1推理": [
        {"大模型", "o1", "推理"},
        {"语言模型", "o1", "推理"},
        {"LLM", "o1", "推理"}
    ],
    "大模型数学推理的泛化性": [
        {"大模型", "数学", "推理", "泛化"},
        {"语言模型", "数学", "推理", "泛化"},
        {"LLM", "数学", "推理", "泛化"}
    ],
}

# 预先读入分类
father_categories = {}
with open('category.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        if row['所属学科'] not in father_categories:
            father_categories[row['所属学科']] = [row['学科（中文）']]
        else:
            father_categories[row['所属学科']].append(row['学科（中文）'])

def load_data(file_path):
    """
    加载并预处理数据

    参数:
    file_path (str): 数据文件的路径

    返回:
    DataFrame: 预处理后的数据框
    """
    # 从CSV文件中读取数据，指定分隔符为制表符，并将日期列解析为日期类型
    df = pd.read_csv(file_path, sep=',', parse_dates=['Publish Date', 'Update Date'])
    
    # 将Stars列转换为数值类型，错误值填充为0
    df['Stars'] = pd.to_numeric(df['Stars'], errors='coerce').fillna(0)
    
    # 返回预处理后的数据框
    return df

def classify_theme(summary):
    """通过关键词匹配进行主题分类"""
    # 定义一个空列表，用于存储匹配到的主题
    themes = []
    # 遍历THEME_KEYWORDS_OR字典，获取主题和关键词
    for theme, keywords in THEME_KEYWORDS_OR.items():
        # 如果summary中包含任意一个关键词，则将主题添加到themes列表中
        if any(kw in summary for kw in keywords):
            themes.append(theme)
    # 遍历THEME_KEYWORDS_AND字典，获取主题和关键词对
    for theme, keyword_pairs in THEME_KEYWORDS_AND.items():
        # 如果summary中包含所有关键词对中的关键词，则将主题添加到themes列表中
        if any(all(kw in summary for kw in pair) for pair in keyword_pairs):
            themes.append(theme)
    # 如果themes列表为空，则返回["其他"]
    return themes if themes else ["其他"]

def generate_daily_report(target_date, df, is_summary=False):
    """生成日报核心内容"""
    # 将目标日期格式化为字符串
    date_str = target_date.strftime("%Y-%m-%d")
    
    # 筛选当日发布的新论文
    new_papers = df[df['Publish Date'].dt.date == target_date.date()]
    # 筛选当日更新的论文
    updated_papers = df[
        (df['Update Date'].dt.date == target_date.date()) & 
        (df['Publish Date'].dt.date != target_date.date())
    ]
    if is_summary == False:
        # df = new_papers + updated_papers
        df = pd.concat([new_papers, updated_papers], ignore_index=True)
    
    # 生成趋势分析，按星星数和更新日期排序，取前TOP_N_TRENDING篇
    trending = df.sort_values(by=['Stars', 'Update Date'], ascending=False).head(TOP_N_TRENDING)
    
    # 主题分类统计和arxiv分类统计
    theme_dist = defaultdict(list) # 数据结构：{主题: [论文1, 论文2, ...]}
    arxiv_theme_dist = defaultdict(list)
    for _, row in df.iterrows():
        # 对每篇论文的摘要进行主题分类
        themes = classify_theme(row['Summary'])
        arxiv_themes = ast.literal_eval(row['Categories'])
        for theme in themes:
            # 将论文添加到对应的主题列表中
            theme_dist[theme].append(row)
        for arxiv_theme in arxiv_themes:
            # 将论文添加到对应的arxiv分类列表中
            arxiv_theme_dist[arxiv_theme].append(row)
    
    # 构建Markdown内容
    content = []
    # 添加日报标题
    content.append(f"# 学术日报 {date_str}\n")
    
    # 当日概览
    content.append("## 📊 当日概览")
    # 添加新增论文数量
    content.append(f"- 新增论文: {len(new_papers)} 篇")
    # 添加更新论文数量
    content.append(f"- 更新论文: {len(updated_papers)} 篇")
    # 添加最热门论文标题和星星数
    content.append(f"- 最热门论文: {trending.iloc[0]['Title'][:30]}... (⭐{trending.iloc[0]['Stars']})\n")

    # 获取最早的时间
    earliest_date = df['Publish Date'].min().date()
    # 获取最晚的时间
    latest_date = df['Publish Date'].max().date()
    # 添加总结信息
    content.append(f"## 📅 总结 {earliest_date} 至 {latest_date}")

    # 主题分布
    content.append("## 🧩 主题分布")
    # 获取这一句话的序号
    seq = content.index("## 🧩 主题分布")
    for theme, papers in sorted(theme_dist.items(), key=lambda x: len(x[1]), reverse=True):
        # 添加主题标题和论文数量
        content.append(f"### {theme} ({len(papers)}篇)")
        # 同时插入到seq之前
        content.insert(seq, f"  -- {theme} ({len(papers)}篇)")

        # 添加代表性论文标题
        content.append(f"**代表性论文**: {papers[0]['Title'][:50]}...")
        # 添加最新进展
        content.append("**最新进展**:")
        # 添加摘要的第一行
        content.append(textwrap.wrap(papers[0]['Summary'], width=200)[0] + "...\n")
        # 全部论文标题
        content.append("**全部论文**:")
        for paper in papers:
            # 格式化主题论文信息
            content.append(f"- {paper['Title']} ({paper['First Author']}) [跳转]({paper['URL']})")

    # arXiv分类分布
    content.append("## 🗂 arXiv分类分布")
    for arxiv_father_theme in father_categories.keys():
        content.append(f"### {arxiv_father_theme}")
        for arxiv_theme in father_categories[arxiv_father_theme]:
            papers = arxiv_theme_dist.get(arxiv_theme, [])
            if not papers:
                continue
            # 添加arXiv分类标题和论文数量
            content.append(f"#### {arxiv_theme} ({len(papers)}篇)")
            # 添加代表性论文标题
            content.append(f"**代表性论文**: {papers[0]['Title'][:50]}...")
            # 添加最新进展
            content.append("**最新进展**:")
            # 添加摘要的第一行
            content.append(textwrap.wrap(papers[0]['Summary'], width=200)[0] + "...\n")
            # 全部论文标题
            content.append("**全部论文**:")
            for paper in papers:
                # 格式化arXiv分类论文信息
                content.append(f"- {paper['Title']} ({paper['First Author']}) [跳转]({paper['URL']})")

    # 趋势论文
    content.append("## 📈 趋势论文")
    for _, paper in trending.iterrows():
        # 格式化趋势论文信息
        content.append(format_paper(paper, "热门"))

    # 新增论文
    if not new_papers.empty:
        # 添加新增论文标题
        content.append("## 🆕 新增论文")
        for _, paper in new_papers.iterrows():
            # 格式化新增论文信息
            content.append(format_paper(paper, "新论文"))
    
    # 更新论文
    if not updated_papers.empty:
        # 添加更新论文标题
        content.append("## 🔄 更新论文")
        for _, paper in updated_papers.iterrows():
            # 格式化更新论文信息
            content.append(format_paper(paper, "更新")) 

    # 将内容列表转换为字符串并返回
    return "\n".join(content)

def format_paper(paper, badge):
    """格式化单篇论文信息"""
    code_link = f"[代码]({paper['Code URL']})" if pd.notna(paper['Code URL']) else "无代码"
    return f"""
### {paper['Title']}
**{badge}** ⭐{paper['Stars']} | {paper['Publish Date'].date()} | {code_link}  
**作者**: {paper['First Author']}  
**摘要**: {textwrap.shorten(paper['Summary'], width=200, placeholder='...')}  
[阅读全文]({paper['URL']})
"""

def arxiv_to_daily_report():
    """主函数，生成学术日报"""
    parser = argparse.ArgumentParser(description="生成学术日报")
    parser.add_argument("--data_file", help="输入数据文件路径", required=True)
    parser.add_argument("--date", help="指定日期 (YYYY-MM-DD)", default=datetime.today().date())
    parser.add_argument("--is_summary", help="是否总结之前的日报", default=False)
    parser.add_argument("--dairy_report_dir", help="日报保存目录", default=DAILY_REPORT_DIR)
    args = parser.parse_args()

    df = load_data(args.data_file)
    report_content = generate_daily_report(pd.to_datetime(args.date), df, args.is_summary)
    
    # 创建输出目录
    os.makedirs(args.dairy_report_dir, exist_ok=True)
    
    # 保存文件
    if args.is_summary:
        filename = f"arxiv_daily_report_summary_{args.date}.md"
    else:
        filename = f"arxiv_daily_report_{args.date}.md"
    with open(os.path.join(args.dairy_report_dir, filename), 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"日报已生成：{os.path.join(args.dairy_report_dir, filename)}")

if __name__ == "__main__":
    arxiv_to_daily_report()