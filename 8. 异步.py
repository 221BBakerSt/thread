from multiprocessing import Pool
import os, time

def func1():
    print(f'this is func1. pid is {os.getpid()}, ppid is {os.getppid()}')
    for i in range(3):
        print(f'---{i}---')
        time.sleep(1)
    return 'hello'

def func2(args):
    print(f'this is func. pid is {os.getpid()}, ppid is {os.getppid()}')
    print(f'the func2 args: {args}')

p = Pool()
# 子进程首先去执行func函数，完成后主进程立马来执行callback函数
# 如果子进程先结束，主进程被打断立马来执行callback
p.apply_async(func = func1, callback = func2)

t = 2
for _ in range(t):
    # 如果主进程先结束，就不会等着去执行callback了！不信你把t改成2试试看
    print(f'---main process {os.getpid()}---')
    time.sleep(1)