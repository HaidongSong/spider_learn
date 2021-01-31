import multiprocessing
import time


class myProcess(multiprocessing.Process):
    def __init__(self, loop, lock):
        multiprocessing.Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print(f"pid {self.pid}, loopCount {count}")
            self.lock.release()


if __name__ == "__main__":
    process = []
    lock = multiprocessing.Lock()
    for i in range(10, 15):
        # print(i)
        p = myProcess(i, lock)
        p.daemon = True
        p.start()
        process.append(p)

    for j in process:
        p.join()

print("Main process end!!!")