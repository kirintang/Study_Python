# 妹子图-最新模块
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree


def download_one_page(url):
    proxies = {
        "https": "121.232.148.212:3256"
    }
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://www.mzitu.com/',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, proxies=proxies)
    html = etree.HTML(resp.text)
    li_list = html.xpath('//*[@id="pins"]/li')
    for li in li_list:
        img_src = li.xpath('./a/img/@data-original')[0]
        #print(imgSrc)
        imgName = img_src.split("/")[-1]
        img_resp = requests.get(img_src, headers=headers, proxies=proxies)
        #print(imgName)
        with open('./images/new/' + imgName, mode="wb") as f:
            f.write(img_resp.content)


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(1, 253):
            t.submit(download_one_page, url=f"https://www.mzitu.com/page/{i}")
    print('爬取完成!')
