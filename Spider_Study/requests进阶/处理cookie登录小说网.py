# 登录得到cookie
# 带着cookie去请求书架获取书架内容

# 使用session请求

import requests


session = requests.session()

data = {
    "loginName": "13261269430",
    "password": "kirintang17k"
}

# 登录
login_url = "https://passport.17k.com/ck/user/login"
resp = session.post(login_url, data=data)

# print(resp.cookies)
# 带着登录信息请求
bookshelf = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(bookshelf.json())
