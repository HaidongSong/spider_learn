from multiprocessing import Process, Pipe


class Consumer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        print("Consumer received...{}".format(self.pipe.recv()))
        self.pipe.send("Consumer words!")


class Producer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        self.pipe.send("Producer words!")  # 需要有一个进程先发送到pipe
        print("Producer received...{}".format(self.pipe.recv()))


if __name__ == '__main__':
    pipe = Pipe()

    p = Producer(pipe[1])
    c = Consumer(pipe[0])
    c.daemon = p.daemon = True
    c.start()
    p.start()
    c.join()
    p.join()
    print("Main process ended...")


