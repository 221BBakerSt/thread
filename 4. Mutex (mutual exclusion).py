from threading import Thread, Lock
import time

'''
Mutual exclusion (mutex) is a mechanism applied in multi-thread program 
to prevent multiple threads from reading/writing a public resource simultaneously.
锁上的越多，越长，越趋近于单任务
Polling(轮询) means CPU actively asks the external devices one by one whether they need service.
'''

def func():
    global num
    # t1和t2线程都抢着对这个锁进行上锁，其中一个线程成功上锁后，其他进程就堵塞直至锁被解开为止
    mutex.acquire()
    for _ in range(1000000):
        num += 1
    # open the lock
    mutex.release()
    print(f'Num after func is {num}')

if __name__ == '__main__':
    num = 0

    # 创建一把互斥锁，默认未上锁
    mutex = Lock()

    t1 = Thread(target = func)
    t1.start()
    # join()意思是等t1子线程完成了才能继续下面的主线程
    # t1.join()

    print('------start to sleep-----')
    # 这时候的睡眠相当于让下面的主线程等上面的子线程
    time.sleep(1)

    t2 = Thread(target = func)
    t2.start()
    # join()意思是等t2子线程完成了才能继续下面的主线程
    # t2.join()

    print('------start to sleep again-----')
    # 这时候的睡眠相当于让下面的主线程等上面的子线程
    time.sleep(0.001)

    print('-----finished multi-thread-----')
    print('Final num is -->', num)
