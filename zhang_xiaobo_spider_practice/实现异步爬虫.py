import asyncio
import time
import requests
import aiohttp


async def myrequests(url):
    print('开始发送请求{}'.format(url))
    # headers/params/data/proxy='http://ip:port'
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as res:
            if res.status == 200:
                # 响应对象操作之前一定要await
                text = await res.text()
                print(text)  # text(), json(), read()
            else:
                print('error request!!')

urls = ['dylan', 'bob', 'margan']
tasks = []
start_time = time.time()
for url in urls:
    c = myrequests('http://127.0.0.1:5000/' + url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start_time)