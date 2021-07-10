import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)

# 解析
html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

for div in divs:
    ori_price = div.xpath(
        "./div/div/a[1]/div[2]/div[1]/span[1]/text()")
    if ori_price:
        price = ori_price[0].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))

    ori_company_name = div.xpath("./div/div/a[2]/div[1]/p/text()")
    if ori_company_name:
        company_name = ori_company_name[1].strip("'\n\n'")
    ori_address = div.xpath("./div/div/a[2]/div[1]/div/span/text()")
    if ori_address:
        address = ori_address[0]
