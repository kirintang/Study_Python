import re
import requests
import csv

url = 'https://movie.douban.com/top250'

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

resp = requests.get(url, headers=headers)

page_content = resp.text

obj = re.compile(
    r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>.*?<span>(?P<evaluate_num>.*?)人评价</span>.*?<p class="quote">.*?<span class="inq">(?P<inq>.*?)</span>', re.S)


result = obj.finditer(page_content)

f = open('./douban_top250.csv', mode='w')
csvwriter = csv.writer(f)

for it in result:
    # print(it.group('name'))  # 电影名
    # print(it.group('year').strip())  # 年份
    # print(it.group('rating_num'))  # 评分
    # print(it.group('evaluate_num'))  # 评价数
    # print(it.group('inq'))  # 描述
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print('over')
