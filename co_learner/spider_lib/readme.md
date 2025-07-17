# 爬取智能体

## 公众号爬取

1. 使用gzh.py脚本进行爬取，爬取之前需要设置其中的cookie、fakeid和data["token"]

   1. 获取方式可参考：https://www.jianshu.com/p/545bdd506aeb，https://zhuanlan.zhihu.com/p/379062852，https://github.com/HuaiLiZhi/WeChatCrawler/blob/master/README.md
   2. cookie获取方法： 进入 [https://mp.weixin.qq.com/cgi-bin/appmsg](https://mp.weixin.qq.com/cgi-bin/appmsg) 登录/注册完成 f12 -> 网络 -> 第一个类型为document的 其中能找到cookie
   3. token获取方法： cookie下方referer中能找到token=...
   4. fakeid获取方法： 点开目标公众号，随意点开一篇文章，用浏览器打开（右上角），然后尝试在这篇文章中找到去另外一篇文章的地方，进入另一篇文章之后从网址中找出类似__biz=MzA5MDMwMTIyNQ==的格式（其中的MzA5MDMwMTIyNQ==就是fakeid）
2. 使用url_to_content_to_abstrut.py脚本对内容进行解析，获得对应的信息摘要，使用之前需要配置大模型的访问接口。

   1. 在上级目录的.env中配置API_KEY和API_BASE
   2. 在上级目录的config.py中配置模型名称
   3. 测试上级目录中的llm_chat.py确保可以正常运行
   4. 配置input和output文件名
