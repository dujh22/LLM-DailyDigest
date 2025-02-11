import arxiv as arx
import requests
import csv
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import os
import argparse
from datetime import datetime

# Function to get the code URL from Papers with Code
# 定义一个函数，用于获取论文的代码链接
def get_paper_code_url(paper_id):
    return None # 该函数需要进一步优化，暂时返回None

    # 定义基础链接
    base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
    # 拼接论文ID，生成完整的链接
    code_url = base_url + paper_id
    try:
        # 发送GET请求，获取论文的代码信息
        code_response = requests.get(code_url, verify=False).json()
        # 判断是否有官方代码链接
        if "official" in code_response and code_response["official"]:
            # 获取官方代码链接
            github_code_url = code_response["official"]["url"]
            # 返回官方代码链接
            return github_code_url
    except:
        # 如果发生异常，返回None
        return None

# Function to get the star count from the GitHub repository
def get_stars(github_code_url):
    return "0" # 该函数需要进一步优化，暂时返回0

    # 尝试获取github代码页面的html内容
    try:
        code_html = requests.get(github_code_url, verify=False)
        # 使用BeautifulSoup解析html内容
        soup = BeautifulSoup(code_html.text, "html.parser")
        # 查找所有a标签，href属性为github代码页面的stargazers链接
        a_stars = soup.find_all("a", href=github_code_url.split("https://github.com")[-1] + "/stargazers")
        # 如果找到了a标签，则获取其文本内容，并去除换行符，取第一个元素
        stars = a_stars[0].text.strip().split("\n")[0] if a_stars else "0"
        # 返回stars
        return stars
    # 如果发生异常，则返回0
    except:
        return "0"

# Function to load already fetched paper IDs
def load_existing_paper_ids(filename):
    if not os.path.exists(filename):
        return set()
    
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        existing_ids = {row[0] for row in reader}
    return existing_ids

# 定义全局变量，用于记录搜索结果的起始位置
pub_start = 0

# Perform the arXiv search and save results to CSV
def fetch_and_save_arxiv_data(query="Large Language Models", max_results=1000, filename="arxiv_papers.csv", start_date=None, end_date=None):    
    """
    参数说明:
    query: 搜索关键词，默认为"Large Language Models"
    max_results: 最大搜索结果数量，默认为1000
    filename: 保存结果的CSV文件名，默认为"arxiv_papers.csv"
    start_date: 起始日期，默认为前一天
    end_date: 终止日期，默认为前一天
    """
    # 定义全局变量，用于记录搜索结果的起始位置
    global pub_start

    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date() # 将字符串转换为日期对象
    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date() # 将字符串转换为日期对象

    # Load existing paper IDs to support resuming
    existing_ids = load_existing_paper_ids(filename)
    
    # Set up the arXiv search with descending date order
    arxiv_search = arx.Search(
        query=query,
        max_results=max_results, 
        sort_by=arx.SortCriterion.SubmittedDate, 
        sort_order=arx.SortOrder.Descending
    )
    
    # Open the file in append mode
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # If file is new, write header
        if not existing_ids:
            writer.writerow([
                "Paper ID", "Title", "URL", "Summary", "First Author", 
                "Publish Date", "Update Date", "Code URL", "Stars", "Categories"
            ])
        
        # Use tqdm for progress tracking
        paper_count = 0  # Initialize a counter for the number of processed papers
        client = arx.Client()
        for result in tqdm(client.results(arxiv_search, offset=pub_start), total=max_results, initial=pub_start, desc="Fetching Papers"):
            paper_id = result.get_short_id()
            
            # Skip if paper has already been processed
            if paper_id in existing_ids:
                continue
            
            # Arxiv学术论文查询接口详解 https://zhuanlan.zhihu.com/p/679538991
            paper_title = result.title
            paper_url = result.entry_id
            paper_summary = result.summary.replace("\n", "")
            paper_first_author = result.authors[0]
            publish_time = result.published.date()
            update_time = result.updated.date()

            print("start_date:", start_date, "end_date:", end_date, "publish_time:", publish_time, "update_time:", update_time)
            # 如果发布时间或者更新时间比终止时间晚，则跳过；如果发布时间或者更新时间比起始时间早，则跳出循环
            if (end_date and publish_time > end_date) or (end_date and update_time > end_date):
                print("发布时间或者更新时间比终止时间晚")
                continue
            if start_date and publish_time < start_date:
                print("发布时间比起始时间早")
                break

            # Get the code URL and stars if available
            # 获取论文的代码链接
            code_url = get_paper_code_url(paper_id)
            # 获取代码的star数量
            stars = get_stars(code_url) if code_url else "N/A"

            paper_categories = result.categories

            # Append paper data to CSV
            writer.writerow([
                paper_id, paper_title, paper_url, paper_summary, 
                paper_first_author, publish_time, update_time, code_url, stars,
                paper_categories
            ])
            
            # Flush the file buffer to ensure data is written
            file.flush()

            # Increment the paper count
            paper_count += 1
            # Update the global pub_start
            pub_start += 1

            # Delay to avoid rate-limiting, adjust based on paper count
            if pub_start > 4000:
                time.sleep(paper_count/1000)
    
    print(f"Data saved to {filename}")
    return True

# Execute the function
def arxiv_search():
    # 获取当前时间戳：年_月_日_时_分_秒
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    # 定义文件名：arxiv_papers_年_月_日_时_分_秒.csv
    filename = "arxiv_papers_" + current_time + ".csv"

    parser = argparse.ArgumentParser(description="爬取arxiv数据")
    parser.add_argument("--query", type=str, default="Large Language Models", help="搜索关键词")
    parser.add_argument("--max_results", type=int, default=4000, help="最大结果数量") # 定义最大结果数：需要注意的是，由于 API 的限制，在多次调用 API 的情况下，建议每次调用的时间间隔为 3 秒。每次调用返回的最大数量为 4000 个。arXiv的硬限制约为 50,000 条记录； 对于与 50,000 多个原稿匹配的查询，无法接收全部结果. 解决这个问题的最简单的解决方案是将中断查询成小块，例如使用的时间片，与一系列日期的submittedDate或lastUpdatedDate 。
    parser.add_argument("--wish_offset", type=int, default=0, help="希望的起始位置") # 定义起始位置
    parser.add_argument("--filename", type=str, default=filename, help="保存结果的CSV文件名") # 定义保存结果的文件名
    # 起始日期和终止日期,默认为当日的前一天
    default_start_date = time.strftime("%Y-%m-%d", time.localtime(time.time() - 3600 * 24))
    parser.add_argument("--start_date", type=str, default=default_start_date, help="起始日期")
    parser.add_argument("--end_date", type=str, default=default_start_date, help="终止日期")
    args = parser.parse_args()

    global pub_start
    pub_start = args.wish_offset
        
    # 调用函数，获取arxiv数据并保存到csv文件中
    # 确保任务完成，如果中途发生错误，可以重新运行而不会重复获取相同的数据
    while True:
        try:
            if fetch_and_save_arxiv_data(query=args.query, max_results=args.max_results, start_date=args.start_date, end_date=args.end_date):
                break
            if pub_start >= args.max_results:
                print("All papers have been fetched.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)

    # 如果用户提供了文件名，则将文件拷贝到用户提供的文件名
    if args.filename:
        filename = args.filename
    # 结束后将文件拷贝到filename，上述逻辑会生成一个临时文件，最后将其保存到filename中
    os.rename("arxiv_papers.csv", filename)


if __name__ == "__main__":
    arxiv_search()