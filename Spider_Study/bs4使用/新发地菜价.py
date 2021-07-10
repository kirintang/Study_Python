import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml'

resp = requests.get(url)
# print(resp.text)

f = open('./菜价.csv', 'w')
csvwriter = csv.writer(f)
# 1,把页面源代码交给BueatifulSoup解析
page = BeautifulSoup(resp.text, 'html.parser')  # 指定html解析器
# 2,从bs4对象中查找数据
# find(标签，属性=属性值)
# find_all(标签，属性=属性值)
# table = page.find("table", attrs={"class": "hq_table"}) # class是关键字,使用class_
table = page.find("table", attrs={"class": "hq_table"})
# 3,拿到所有数据行
trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")  # 每行中的数据
    name = tds[0].text  # 菜名
    low_price = tds[1].text  # 最低价
    avg_price = tds[2].text  # 平均价
    higest_price = tds[3].text  # 最高价
    standard = tds[4].text  # 规格
    unit = tds[5].text  # 单位
    pub_date = tds[6].text  # 发布时间
    csvwriter.writerow([name, low_price, avg_price,
                       higest_price, standard, unit, pub_date])
f.close()
print('over!')
