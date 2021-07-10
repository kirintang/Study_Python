from lxml import etree

tree = etree.parse("b.html")
# result = tree.xpath("/html/body/ul/li/a/text()") # ['百度', '谷歌', '必应']
# result = tree.xpath("/html/body/ul/li[1]/a/text()") # ['百度'] []表示索引 索引从1开始
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()") # [@xxx='yyy']表示属性 ['大炮']
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    atext = li.xpath("./a/text()")  # ./相对查找
    print(atext)
    htext = li.xpath("./a/@href")  # 获取属性的值 @属性
    print(htext)

# ['http://www.baidu.com', 'http://www.google.com', 'http://www.bing.com']
print(tree.xpath("/html/body/ul/li/a/@href"))
print(tree.xpath("/html/body/div[1]/text()"))
