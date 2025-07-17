# -*- coding: UTF-8 -*-
import requests
import time
import pandas as pd
import math
import random

# List of user agents to randomize requests
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36',
]

# Target URL and user-specific data
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
# 机器之心
# cookie = "ua_id=6fQ22Ya4jEJabkXnAAAAAOJrs1dsShP-vUqte2kmCRE=; wxuin=20840780394661; mm_lang=zh_CN; pgv_pvid=1721521690181522; _qimei_uuid42=187150b291c100715525f319ff3317dfaba3ce5e3d; pac_uid=0_6KAsj1JXFWkFM; _qimei_q36=; suid=user_0_6KAsj1JXFWkFM; qq_domain_video_guid_verify=0538d3cb62847aff; omgid=0_6KAsj1JXFWkFM; _ga=GA1.1.1996009645.1752720988; _qimei_fingerprint=379b36803aaa262c4c4e73954f30c81d; _qimei_i_3=59e84fd39152568fc292ab63098d20e2f2bdf0a51a585284bc8a29592293263d626664973c89e28fd686; _qimei_h38=; _ga_PF3XX5J8LE=GS2.1.s1752720988$o1$g0$t1752720994$j54$l0$h0; _qimei_i_1=45f824849124; rewardsn=; wxtokenkey=777; _clck=ytda5u|1|fxo|0; uuid=9f8a679a1accaa64ce11b25af053540a; rand_info=CAESIJaGhBSuEh1h5ZCJBAfn0iGuGRVVH8qrNtUHIkwKZMzK; slave_bizuin=3881264596; data_bizuin=3881264596; bizuin=3881264596; data_ticket=IY4S/WYIpTyFnZxN6PdcdQjKETDGwI9+XaAhnQ5g7u3QRbn0/T2cEzIN/UIukyUT; slave_sid=SmQwb0ViSmdJSkN1dDdlbjU3NkFvd0s2eGRIaEt5OU9VcUQ0UnpzcGFCY2E1eW1KcGJFUDVkb1l2c2JwT013dldWY0dxOXpHdFpBRTZYSWc1WFRvR0xNbFFjQUNLQnZnZ3BYN3h1RktPNGgxOFF1RVhXdkUycDVLNDZWamJnNXhEZjdCM1p3a3VMc2ZPV3Zw; slave_user=gh_d02d135b51f8; xid=4e87171af71c9c164c7a5ad461c76d7c; _clsk=vw0ty|1752724821456|18|1|mp.weixin.qq.com/weheat-agent/payload/record"  # Replace with your copied cookie value
# fakeid = "MzA3MzI4MjgzMw=="  # Replace with the required fakeid

# 量子位
# cookie = "ua_id=6fQ22Ya4jEJabkXnAAAAAOJrs1dsShP-vUqte2kmCRE=; wxuin=20840780394661; mm_lang=zh_CN; pgv_pvid=1721521690181522; _qimei_uuid42=187150b291c100715525f319ff3317dfaba3ce5e3d; pac_uid=0_6KAsj1JXFWkFM; _qimei_q36=; suid=user_0_6KAsj1JXFWkFM; qq_domain_video_guid_verify=0538d3cb62847aff; omgid=0_6KAsj1JXFWkFM; _ga=GA1.1.1996009645.1752720988; _qimei_i_3=59e84fd39152568fc292ab63098d20e2f2bdf0a51a585284bc8a29592293263d626664973c89e28fd686; _ga_PF3XX5J8LE=GS2.1.s1752720988$o1$g0$t1752720994$j54$l0$h0; _qimei_i_1=45f824849124; rewardsn=; wxtokenkey=777; _clck=ytda5u|1|fxo|0; uuid=9f8a679a1accaa64ce11b25af053540a; rand_info=CAESIJaGhBSuEh1h5ZCJBAfn0iGuGRVVH8qrNtUHIkwKZMzK; slave_bizuin=3881264596; data_bizuin=3881264596; bizuin=3881264596; data_ticket=IY4S/WYIpTyFnZxN6PdcdQjKETDGwI9+XaAhnQ5g7u3QRbn0/T2cEzIN/UIukyUT; slave_sid=SmQwb0ViSmdJSkN1dDdlbjU3NkFvd0s2eGRIaEt5OU9VcUQ0UnpzcGFCY2E1eW1KcGJFUDVkb1l2c2JwT013dldWY0dxOXpHdFpBRTZYSWc1WFRvR0xNbFFjQUNLQnZnZ3BYN3h1RktPNGgxOFF1RVhXdkUycDVLNDZWamJnNXhEZjdCM1p3a3VMc2ZPV3Zw; slave_user=gh_d02d135b51f8; xid=4e87171af71c9c164c7a5ad461c76d7c; _qimei_fingerprint=a702935bcdc249346e155a379871b4ee; _qimei_h38=3d35a5ee5525f319ff3317df03000006c18715; _clsk=17h0pzw|1752733630510|2|1|mp.weixin.qq.com/weheat-agent/payload/record"
# fakeid = "MzIzNjc1NzUzMw==" 

# 新智元
# cookie = "ua_id=6fQ22Ya4jEJabkXnAAAAAOJrs1dsShP-vUqte2kmCRE=; wxuin=20840780394661; mm_lang=zh_CN; pgv_pvid=1721521690181522; _qimei_uuid42=187150b291c100715525f319ff3317dfaba3ce5e3d; pac_uid=0_6KAsj1JXFWkFM; _qimei_q36=; suid=user_0_6KAsj1JXFWkFM; qq_domain_video_guid_verify=0538d3cb62847aff; omgid=0_6KAsj1JXFWkFM; _ga=GA1.1.1996009645.1752720988; _qimei_i_3=59e84fd39152568fc292ab63098d20e2f2bdf0a51a585284bc8a29592293263d626664973c89e28fd686; _ga_PF3XX5J8LE=GS2.1.s1752720988$o1$g0$t1752720994$j54$l0$h0; _qimei_i_1=45f824849124; rewardsn=; wxtokenkey=777; _clck=ytda5u|1|fxo|0; uuid=9f8a679a1accaa64ce11b25af053540a; rand_info=CAESIJaGhBSuEh1h5ZCJBAfn0iGuGRVVH8qrNtUHIkwKZMzK; slave_bizuin=3881264596; data_bizuin=3881264596; bizuin=3881264596; data_ticket=IY4S/WYIpTyFnZxN6PdcdQjKETDGwI9+XaAhnQ5g7u3QRbn0/T2cEzIN/UIukyUT; slave_sid=SmQwb0ViSmdJSkN1dDdlbjU3NkFvd0s2eGRIaEt5OU9VcUQ0UnpzcGFCY2E1eW1KcGJFUDVkb1l2c2JwT013dldWY0dxOXpHdFpBRTZYSWc1WFRvR0xNbFFjQUNLQnZnZ3BYN3h1RktPNGgxOFF1RVhXdkUycDVLNDZWamJnNXhEZjdCM1p3a3VMc2ZPV3Zw; slave_user=gh_d02d135b51f8; xid=4e87171af71c9c164c7a5ad461c76d7c; _qimei_fingerprint=a702935bcdc249346e155a379871b4ee; _qimei_h38=3d35a5ee5525f319ff3317df03000006c18715; _clsk=17h0pzw|1752736030652|6|1|mp.weixin.qq.com/weheat-agent/payload/record"
# fakeid = "MzI3MTA0MTk1MA=="

# AGI HUNT
cookie = "ua_id=6fQ22Ya4jEJabkXnAAAAAOJrs1dsShP-vUqte2kmCRE=; wxuin=20840780394661; mm_lang=zh_CN; pgv_pvid=1721521690181522; _qimei_uuid42=187150b291c100715525f319ff3317dfaba3ce5e3d; pac_uid=0_6KAsj1JXFWkFM; _qimei_q36=; suid=user_0_6KAsj1JXFWkFM; qq_domain_video_guid_verify=0538d3cb62847aff; omgid=0_6KAsj1JXFWkFM; _ga=GA1.1.1996009645.1752720988; _qimei_i_3=59e84fd39152568fc292ab63098d20e2f2bdf0a51a585284bc8a29592293263d626664973c89e28fd686; _ga_PF3XX5J8LE=GS2.1.s1752720988$o1$g0$t1752720994$j54$l0$h0; _qimei_i_1=45f824849124; rewardsn=; wxtokenkey=777; _clck=ytda5u|1|fxo|0; uuid=9f8a679a1accaa64ce11b25af053540a; rand_info=CAESIJaGhBSuEh1h5ZCJBAfn0iGuGRVVH8qrNtUHIkwKZMzK; slave_bizuin=3881264596; data_bizuin=3881264596; bizuin=3881264596; data_ticket=IY4S/WYIpTyFnZxN6PdcdQjKETDGwI9+XaAhnQ5g7u3QRbn0/T2cEzIN/UIukyUT; slave_sid=SmQwb0ViSmdJSkN1dDdlbjU3NkFvd0s2eGRIaEt5OU9VcUQ0UnpzcGFCY2E1eW1KcGJFUDVkb1l2c2JwT013dldWY0dxOXpHdFpBRTZYSWc1WFRvR0xNbFFjQUNLQnZnZ3BYN3h1RktPNGgxOFF1RVhXdkUycDVLNDZWamJnNXhEZjdCM1p3a3VMc2ZPV3Zw; slave_user=gh_d02d135b51f8; xid=4e87171af71c9c164c7a5ad461c76d7c; _qimei_fingerprint=a702935bcdc249346e155a379871b4ee; _qimei_h38=3d35a5ee5525f319ff3317df03000006c18715; _clsk=17h0pzw|1752738559200|9|1|mp.weixin.qq.com/weheat-agent/payload/record"
fakeid = "MzA4NzgzMjA4MQ=="

# Request payload and headers
data = {
    "token": "1896974313",      # 令牌，用于身份验证
    "lang": "zh_CN",            # 语言设置为中文
    "f": "json",                # 返回数据格式为json
    "ajax": "1",                # ajax请求标志
    "action": "list_ex",        # 操作类型，获取文章列表
    "begin": "0",               # 起始位置，分页用
    "count": "10",               # 每页请求的文章数量
    "query": "",                # 查询关键词，默认为空
    "fakeid": fakeid,           # 公众号的fakeid
    "type": "9",                # 文章类型，9代表图文消息
}
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36",
}

# Initial request to get the total count and calculate the number of pages
try:
    content_json = requests.get(url, headers=headers, params=data).json()
    count = int(content_json["app_msg_cnt"])
    page = int(math.ceil(count / int(data["count"])))
    print(f"Total articles: {count}, Total pages: {page}")
except Exception as e:
    print(f"Error during initial request: {e}")
    exit()

# Scraping loop
content_list = []
for i in range(page):
    data["begin"] = i * int(data["count"])
    user_agent = random.choice(user_agent_list)
    headers["User-Agent"] = user_agent

    try:
        # Request page content
        content_json = requests.get(url, headers=headers, params=data).json()
        
        # Parse and save each item
        for item in content_json["app_msg_list"]:
            items = [
                item["title"],
                item["link"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["create_time"]))
            ]
            content_list.append(items)

        # Periodic save
        if (i > 0) and (i % 10 == 0):
            test = pd.DataFrame(content_list, columns=['title', 'link', 'create_time'])
            test.to_csv("url.csv", mode='a', encoding='utf-8', index=False, header=not bool(i))  # Only add header once
            print(f"Saved after page {i}")
            content_list = []
            time.sleep(random.randint(60, 90))
        else:
            time.sleep(random.randint(15, 25))
        
    except Exception as e:
        print(f"Error on page {i}: {e}")
        time.sleep(5)  # Shorter delay on error and continue

# Final save if there are remaining items
if content_list:
    test = pd.DataFrame(content_list, columns=['title', 'link', 'create_time'])
    test.to_csv("url.csv", mode='a', encoding='utf-8', index=False, header=False)
    print("Final save completed")