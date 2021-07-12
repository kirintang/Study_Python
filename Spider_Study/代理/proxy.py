import requests

proxies = {
    "https": "https://59.55.160.234:3256"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
