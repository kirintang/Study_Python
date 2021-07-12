from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import csv

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)


def download_one_page(url):
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # tr = table.xpath("./tr")[1:]
    trs = table.xpath("./tr[position()>1]")  # 去除表头
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据做处理 \\ /
        txt = (item.replace("\\", "").replace("/", "").replace("|", ",")
               for item in txt)
        csvwriter.writerow(txt)
    print(url, "提取完毕!")


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page,
                     url=f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("task done!")
