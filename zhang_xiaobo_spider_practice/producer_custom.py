from multiprocessing import Process, Lock, Queue, Semaphore
import time
from random import random

buffer = Queue(10)
empty = Semaphore(2)  # 缓存空余数
full = Semaphore(0)  # 缓存占用数
lock = Lock()


class Consumer(Process):

    def run(self):
        global empty, buffer, full, lock
        while True:
            full.acquire()
            lock.acquire()   # 占用空间先acquire
            num = buffer.get()
            time.sleep(1)
            print(f"Consumer remove an element..{num}")
            lock.release()
            empty.release()


class Producer(Process):

    def run(self):
        global empty, full, buffer, lock
        while True:
            empty.acquire()
            lock.acquire()
            num = random()
            buffer.put(num)

            time.sleep(1)
            print("Producer append an element...  {}".format(num))
            lock.release()
            full.release()


if __name__ == "__main__":
    consumer = Consumer()
    producer = Producer()
    producer.daemon = consumer.daemon = True
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print("Main process ended!!!")