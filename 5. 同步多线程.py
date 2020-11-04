from threading import Thread, current_thread, Lock
from time import sleep

def task1(times):
    for _ in range(times):
        if mutex1.acquire():
            print(current_thread().name)
            mutex2.release()
            sleep(0.5)

def task2(times):
    for _ in range(times):
        if mutex2.acquire():
            print(current_thread().name)
            mutex3.release()
            sleep(0.5)

def task3(times):
    for _ in range(times):
        if mutex3.acquire():
            print(current_thread().name)
            mutex1.release()
            sleep(0.5)

if __name__ == '__main__':
    mutex1 = Lock()
    mutex2 = Lock()
    mutex3 = Lock()

    mutex2.acquire()
    mutex3.acquire()

    times = 3
    t1 = Thread(target = task1, args = (times,))
    t2 = Thread(target = task2, args = (times,))
    t3 = Thread(target = task3, args = (times,))
    t1.start()
    t2.start()
    t3.start()

'''
# 被死锁跑不动
class Task1(Thread):
    def run(self):
        while 1:
            if mutex1.acquire():
                print(current_thread().name)
                mutex2.release()
                sleep(1)

class Task2(Thread):
    def run(self):
        while 1:
            if mutex2.acquire():
                print(current_thread().name)
                mutex3.release()
                sleep(1)

class Task3(Thread):
    def run(self):
        while 1:
            if mutex3.acquire():
                print(current_thread().name)
                mutex1.release()
                sleep(1)


if __name__ == '__main__':
    mutex1 = Lock()
    mutex2 = Lock()
    mutex3 = Lock()

    mutex2.acquire()
    mutex3.acquire()

    t1 = Task1()
    t2 = Task1()
    t3 = Task1()
    t1.start()
    t2.start()
    t3.start()
'''