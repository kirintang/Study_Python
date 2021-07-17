# request.get() 同步的代码 -> 异步操作使用aiohttp
# pip install aouhttp

import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2021/0714/fd3341a4980829583f09ddee0f0ac85a.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0714/a5a239c8a3d0a3ff15300dd527b52732.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0714/fe8cdb7653350a8e04c1a2d7c50568a4.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0714/8a42a2ffb755555a69f449b43dd11de3.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0713/61b1df71f18779d0c969a265b4d7cb33.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0713/b177e0b96a47bd10b4d5a16f46fc6879.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0714/024df8f38e263fe18dc5b9452b59f5e6.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0712/224396e21ab83520140447e7c8cb70e8.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0713/a0be8414df21eb196ea4059bd438b8b6.jpg",
]


async def aiodownload(url):
    # with带有上下文
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:  # 相当于requests
        async with session.get(url) as resp:
            # 写入文件
            # 这里可以使用aiofile模块
            with open("./images/" + name, mode="wb") as f:
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
    print(name + " over!")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
