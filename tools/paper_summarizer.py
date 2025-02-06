import pandas as pd
from datetime import datetime
import argparse
import os
from collections import defaultdict
import textwrap

# 配置参数
DAILY_REPORT_DIR = "/Users/djh/Documents/GitHub/LLM-DailyDigest/updates"
TOP_N_TRENDING = 5
THEME_KEYWORDS = {
    "大模型": [
        "自回归", "Transformer", "深度神经网络", "模型压缩", "预训练", "微调", 
        "大规模训练", "多模态", "生成式模型", "模型集成", "自监督学习"
    ],
    "推理": [
        "推理", "o1",
        "推理速度", "推理优化", "模型加速", "量化", "低精度推理", "GPU加速", 
        "推理延迟", "边缘计算", "分布式推理", "实时推理", "推理框架", "增量推理"
    ],
    "测评": [
        "准确率", "召回率", "F1分数", "AUC", "混淆矩阵", "性能评估", "性能瓶颈", 
        "模型鲁棒性", "计算复杂度", "对比实验", "泛化能力", "在线评测", "模型验证"
    ],
    "模型部署与应用": [
        "模型部署", "容器化", "云端部署", "边缘计算", "实时推理", "API集成", 
        "微服务", "自动化部署", "持续集成", "跨平台部署"
    ],
    "算法与优化": [
        "优化算法", "梯度下降", "遗传算法", "贝叶斯优化", "超参数调优", "强化学习", 
        "迁移学习", "元学习", "增量学习", "自适应优化", "目标检测", "图像分割"
    ],
    "数据与隐私": [
        "数据增强", "数据隐私", "联邦学习", "差分隐私", "数据安全", 
        "数据标注", "多模态数据", "数据流处理", "数据清洗"
    ],
    "人工智能伦理与社会": [
        "伦理", "可解释性", "公平性", "算法偏见", "自动化决策", "隐私保护", 
        "社会影响", "AI治理", "算法透明度"
    ],
    "自然语言处理": [
        "文本生成", "语音识别", "机器翻译", "命名实体识别", "情感分析", "词向量", 
        "句法分析", "自然语言理解", "对话系统", "语音合成", "语言模型", "文本分类"
    ],
    "计算机视觉": [
        "图像分类", "目标检测", "图像分割", "人脸识别", "姿态估计", "视觉跟踪", 
        "图像生成", "深度图像生成", "图像检索", "视频分析", "3D重建", "视觉感知"
    ]
}

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
    themes = []
    for theme, keywords in THEME_KEYWORDS.items():
        if any(kw in summary for kw in keywords):
            themes.append(theme)
    return themes if themes else ["其他"]

def generate_daily_report(target_date, df):
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
    
    # 生成趋势分析，按星星数和更新日期排序，取前TOP_N_TRENDING篇
    trending = df.sort_values(by=['Stars', 'Update Date'], ascending=False).head(TOP_N_TRENDING)
    
    # 主题分类统计
    theme_dist = defaultdict(list)
    for _, row in df.iterrows():
        # 对每篇论文的摘要进行主题分类
        themes = classify_theme(row['Summary'])
        for theme in themes:
            # 将论文添加到对应的主题列表中
            theme_dist[theme].append(row)
    
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
    
    # 趋势论文
    content.append("## 📈 趋势论文")
    for _, paper in trending.iterrows():
        # 格式化趋势论文信息
        content.append(format_paper(paper, "热门"))
    
    # 主题分布
    content.append("## 🧩 主题分布")
    for theme, papers in sorted(theme_dist.items(), key=lambda x: len(x[1]), reverse=True):
        # 添加主题标题和论文数量
        content.append(f"### {theme} ({len(papers)}篇)")
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

def main():
    parser = argparse.ArgumentParser(description="生成学术日报")
    parser.add_argument("data_file", help="输入数据文件路径")
    parser.add_argument("--date", help="指定日期 (YYYY-MM-DD)", default=datetime.today().date())
    args = parser.parse_args()

    df = load_data(args.data_file)
    report_content = generate_daily_report(pd.to_datetime(args.date), df)
    
    # 创建输出目录
    os.makedirs(DAILY_REPORT_DIR, exist_ok=True)
    
    # 保存文件
    filename = f"daily_report_{args.date}.md"
    with open(os.path.join(DAILY_REPORT_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"日报已生成：{os.path.join(DAILY_REPORT_DIR, filename)}")

if __name__ == "__main__":
    main()