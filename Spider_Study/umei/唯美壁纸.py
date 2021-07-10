import requests

from bs4 import BeautifulSoup
import time

domain = 'https://www.umei.net/'

url = '/bizhitupian/weimeibizhi/'
resp = requests.get(domain + url.strip("/"))
resp.encoding = 'utf-8'

# print(resp.text)
main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find("div", attrs={"class": "TypeList"}).find_all("a")
# TODO 待优化、分开处理
for a in alist:
    # 拿到子页面
    href = a.get('href')
    # print(href)
    child_page_resp = requests.get(domain + href.strip("/"))
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 解析子页面
    child_page = BeautifulSoup(child_page_text, 'html.parser')
    p = child_page.find("p", attrs={"align": "center"})
    img = p.find("img")
    img_url = img.get("src")
    # 下载图片
    img_resp = requests.get(img_url)
    # img_resp.content # 拿到的是子节
    img_name = img_url.split("/")[-1]  # 获取图片名
    with open('images/' + img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
    print("over!", img_name)
    time.sleep(1)
print("task done!")
