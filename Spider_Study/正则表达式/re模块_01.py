import re

# findall 匹配字符串中所有符合正则的内容
lst = re.findall(r"\d+", "我的电话号码是: 10086")

print(lst)

# finditer 匹配字符串中的所有内容【返回的是迭代器】
# 从迭代器中拿到内容需要.group

it = re.finditer(r"\d+", "我的电话号码是：10086")

for i in it:
    print(i.group())


# search找到一个结果就返回，返回的是一个match，获取内容使用.group
it = re.search(r"\d+", "我的电话号码是：10086")

print(it.group())

# match 是从头开始匹配

it = re.match(r"\d+", "10086, 我的电话号码是：10086")

print(it.group())

# 预加载正则表达式，一个正则表达式被多次使用可以先预加载

obj = re.compile(r"\d+")

obj.findall("我的电话号码是：10086")
obj.finditer("我的电话号码是：10086")