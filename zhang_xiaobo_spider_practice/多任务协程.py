import time
import asyncio


async def request(url):
    print('Dowinloading...{}'.format(url))
    await asyncio.sleep(2)
    print('Downloaded{}'.format(url))


urls = ['www.baidu.com',
        'www.sogou.com',
        'www.biying.com',
        'www.google.com']


async def testrequest():
    print('This is test process')
    time.sleep(2)
    print('test ended')


tasks = []
start_time = time.time()
# testc = testrequest()   # 异步任务中混入同步程序，同步程序不会异步执行，也不会干扰其他异步任务
# tasktask = asyncio.ensure_future(testc)
# tasks.append(tasktask)
for url in urls:
    c = request(url)  # 返回协程对象
    task = asyncio.ensure_future(c)  #创建一个任务对象， 将协程对象封装到任务对象中
    tasks.append(task)  # append
loop = asyncio.get_event_loop()   # 创建一个事件循环对象
loop.run_until_complete(asyncio.wait(tasks))  # 将任务列表注册到循环对象，并运行
print(time.time()-start_time)