import threading
import time
count = 1


class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        tmp = count + 1
        time.sleep(0.001)
        count = tmp


threads = []
for _ in range(1000):
    t = myThread()
    t.start()
    threads.append(t)
for j in threads:
    j.join()

print(count)




# import threading
# import time
#
#
# def myThread(second):
#     print(threading.current_thread().name, 'running...')
#     print(threading.current_thread().name, 'sleep  {}s'.format(second))
#     time.sleep(second)
#     print(threading.current_thread().name, 'sleep end')
#     print(threading.currentThread().name, "threading.currentThread().name")
#
#
# l = [1, 5]
# print(threading.current_thread().name, "running...")
# for i in l:
#     thread = threading.Thread(target=myThread, args=[i])
#     thread.start()
#     # thread.setDaemon()
#     thread.join()
# print(threading.current_thread().name, "end!")





