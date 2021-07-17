"""
- selenium：自动化测试工具
- 可以打开浏览器，像人一样操作浏览器
- 开发者可以从selenium中直接提取页面上的信息
- 安装

```
pip install selenium -i 源
```
- 下载浏览器驱动chromedriver
`https://npm.taobao.org/mirrors/chromedriver`

- 放到python解释器目录下
"""
from selenium.webdriver import Chrome

# 创建浏览器对象
web = Chrome()
# 打开网站
web.get("https://www.baidu.com")

print(web.title)