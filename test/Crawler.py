# _*_coding:utf-8 _*_

import random
from urllib import request
import urllib
import re  # 正则表达式

url = r"http://www.baidu.com/s?wd=python"
urlPC28 = r"https://kj.pc28.li//"

# 处理GET请求中的中文编码
# http://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC
# wd = {"wd": "北京"}
# wdd = urllib.parse.urlencode(wd)
# print(wdd)

# 反爬虫机制1：判断用户是否是浏览器访问
# 措施：伪装浏览器进行访问,随机选择浏览器,伪装浏览器
agent1 = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 " \
         "Safari/537.36 "
agent2 = "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, " \
         "like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36 "
agent3 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 " \
         "Safari/537.36 Edge/17.17134 "
listAgent = [agent1, agent2, agent3]
agent = random.choice(listAgent)
header = {
    "User-Agent": agent
}

# 反爬虫机制2：判断请求来源的IP地址
# 措施：使用代理IP
proxyList = [
    {"http": "182.34.33.249:808"},
    {"http": "117.30.113.79:9999"},
    {"http": "222.89.32.177:9999"},
    {"http": "120.83.110.189:9999"}
]
proxy = random.choice(proxyList)
print(proxy)
# 构建代理处理器对象
proxyHandler = request.ProxyHandler(proxy)

# 构建请求处理器对象
http_handler = request.HTTPHandler()
# 创建自定义opener
# opener = request.build_opener(http_handler, proxyHandler)
opener = request.build_opener(http_handler)
# 把自定义opener设置为全局，这样用urlopen发送的请求也会使用自定义opener
request.install_opener(opener)

# 创建自定义请求对象
req = request.Request(url, headers=header)
# 发送请求，获取响应信息
# response = request.urlopen(req).read().decode()
response = opener.open(req).read().decode()

pat = r"<title>(.*?)</title>"
data = re.findall(pat, response)

# print(res)
print(data[0])
