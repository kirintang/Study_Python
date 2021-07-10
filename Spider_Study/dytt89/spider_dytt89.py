import re
import requests

domain = 'https://www.dy2018.com/'

resp = requests.get(domain, verify=True)
resp.encoding = 'gb2312'  # 指定字符集

# print(resp.text)

# 拿到ul里面li
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
result1 = obj1.finditer(resp.text)
obj2 = re.compile(r"<a href='(?P<url>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie_name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_url>.*?)">', re.S)

sub_list = []

for it in result1:
    ul = it.group('ul')
    # 提取子页面链接
    urls = obj2.finditer(ul)
    for it2 in urls:
        # https://www.dy2018.com/i/103751.html
        sub_url = domain + it2.group('url').strip('/')
        sub_list.append(sub_url)

# 提取子页面
for href in sub_list:
    sub_resp = requests.get(href)
    sub_resp.encoding = 'gb2312'
    movie = obj3.search(sub_resp.text)
    print(movie.group('movie_name'))
    print(movie.group('download_url'))