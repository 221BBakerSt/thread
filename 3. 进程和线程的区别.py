from multiprocessing import Process
from threading import Thread
import time

# a process is a running program
# 进程是资源分配的最小单位，线程是CPU调度的最小单位
# process == train, thread == carriage, coroutine == seat
'''
线程在进程下行进（单纯的车厢无法运行）
一个进程可以包含多个线程（一辆火车可以有多个车厢）
不同进程间数据很难共享（一辆火车上的乘客很难换到另外一辆火车，比如站点换乘）
同一进程下不同线程间数据很易共享（A车厢换到B车厢很容易）
进程要比线程消耗更多的计算机资源（采用多列火车相比多个车厢更耗资源）
进程间不会相互影响，一个线程挂掉将[很可能]导致整个进程挂掉（一列火车不会影响到另外一列火车，但是如果一列火车上中间的一节车厢着火了，将影响到所有车厢）
进程可以拓展到多机，进程最适合多核（不同火车可以开在多个轨道上，同一火车的车厢不能在行进的不同的轨道上）
进程使用的内存地址可以上锁，即一个线程使用某些共享内存时，其他线程必须等它结束，才能使用这一块内存。（比如火车上的洗手间）－"互斥锁"
进程使用的内存地址可以限定使用量（比如火车上的餐厅，最多只允许多少人进入，如果满了需要在门口等，等有人出来了才能进去）－“信号量”
'''

def func():
    global num
    for _ in range(1000000):
        num += 1
    print(f'Num after func becomes {num}')

if __name__ == '__main__':
    num = 0

    p = Process(target = func)
    p.start()
    # wait the child process to be finished, then continue the parent process below
    p.join()
    print(f"Num after child process is still {num}, which means multiprocessing won't change global variables")

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
