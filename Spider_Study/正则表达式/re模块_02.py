import re

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jby'><span id='2'>宋轶</span></div>
<div class='jcy'><span id='3'>郭德纲</span></div>
<div class='jey'><span id='4'>李连杰</span></div>
<div class='jdy'><span id='5'>成龙</span></div>
"""

# (?P<分组名称>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(
    r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S)  # res.S 让.能匹配到换行符

result = obj.finditer(s)  # 迭代器

for it in result:
    print(it.group('id'))
    print(it.group('wahaha'))

"""
郭麒麟
宋轶
郭德纲
李连杰
成龙
"""
