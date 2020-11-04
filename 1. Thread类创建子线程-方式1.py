from threading import Thread, current_thread
# from multiprocessing import Process
import time

# 进程是资源分配的单位，线程是OS调度的单位
# processes are for resource allocation, threads are for OS schedule
def func():
    print('---func---by', current_thread().name)
    time.sleep(1)

if __name__ == '__main__':
    print(current_thread().name)
    
    start = time.perf_counter()

    for _ in range(5):

        # 多线程共享全局变量
        t = Thread(target = func)
        # 多进程不会影响全局变量
        # t = Process(target = func)
        t.start()
    # join()意思是等这个子线程完成了才能继续下面的主线程
    t.join()
        
    end = time.perf_counter()
    print(round(end - start, 5))
