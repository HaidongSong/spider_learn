from multiprocessing import Pool
import time

# urls = ['aa', 'bb', 'cc', 'dd']
urls = range(100)

def download(url):
    print(f'Downloading...{url}')
    time.sleep(0.1)
    print(f'Downloaded!!!{url}')


pool = Pool(50)
start_time = time.time()
pool.map(download, urls)
# pool.close()
# pool.join()
end_time = time.time()

print(f'Total time is {end_time-start_time} second!')

