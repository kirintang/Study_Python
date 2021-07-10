# pip install lxml

from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>12.98</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="1">周杰伦</nick>
        <nick id="2">蔡徐坤</nick>
        <nick id="3">王大仙</nick>
        <nick id="4">蔡依林</nick>
        <div>
            <nick>苏大强</nick>
        </div>
        <span>
            <nick id="1">白眉鹰王</nick>
        </span>
    </author>

    <partner>
        <nick id="1">周芷若</nick>
        <nick id="2">张无忌</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)

# result = tree.xpath("/book")  # / 表示层级关系 第一个/是根节点
# result = tree.xpath("/book/name/text()") # text() 获取文本
# result = tree.xpath("/book/author/nick/text()")
# result = tree.xpath("/book/author//nick/text()") # // 获取author下所有的nick
# result = tree.xpath("/book/author/*/nick/text()") # * 表示任意节点，通配符 ['苏大强', '白眉鹰王']
# result = tree.xpath("/book//nick/text()")