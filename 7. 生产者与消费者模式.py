from threading import Thread
from queue import Queue
from time import sleep

class Producer(Thread):
    def run(self):
        global queue
        count = 0
        while 1:
            if q.qsize() < 100:
                for i in range(10):
                    count += 1
                    msg = 'Product ' + str(count)
                    q.put(msg)
                    print(msg)
            sleep(1)

class Consumer(Thread):
    def run(self):
        global queue
        while 1:
            if q.qsize() > 10:
                for i in range(3):
                    msg = q.get() + ' is consumed by ' + self.name
                    print(msg)
            sleep(1)

if __name__ == '__main__':
    q = Queue()
    for i in range(50):
        q.put('Original product -- '+str(i))
    for _ in range(3):
        t1 = Producer()
        t1.start()
    for _ in range(4):
        t2 = Consumer()
        t2.start()
