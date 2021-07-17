
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}

import asyncio
import requests
import aiohttp
import json
import aiofiles
import time

"""
1, 同步操作，访问getCatalog接口拿到章节id
2, 异步操作：访问getChapterContent下载章节内容
"""


async def getCatelog(url):
    resp = requests.get(url)
    dict = resp.json()
    tasks = []
    for item in dict['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(asyncio.create_task(aiodownload(cid, book_id, title)))
    await asyncio.wait(tasks)


async def aiodownload(cid, book_id, title):
    data = {"book_id": book_id,
            "cid": f"{book_id}|{cid}",
            "need_bookinfo": 1}
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open("./西游记/" + title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


async def main():
    pass

if __name__ == '__main__':
    t1 = time.time()
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+book_id+'"}'
    asyncio.run(getCatelog(url))
    asyncio.run(main())
    t2 = time.time()
    print("耗时", t2 - t1)
