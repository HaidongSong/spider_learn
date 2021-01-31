import time
from multiprocessing import Pool
from urllib import error, request


def scrape(url):
    print("URL {} secaped.".format(url))
    time.sleep(2)
    print(f'URL {url} not scraped.')


if __name__ == "__main__":
    urls = ['https://www.baidu.com',
            'https://jianshu.com',
            'http://blog.csdn.net',
            'http://www.meituan.com']

    start = time.time()
    pool = Pool(processes=4)
    pool.map(scrape, urls)
    # for i in urls:
    #     pool.apply_async(scrape, args=(i,))
    # print('Main process started')
    pool.close()
    # pool.join()
    # print('Main process ended..')
    print(time.time()-start)
