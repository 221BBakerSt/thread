from threading import Thread, current_thread, local

# create global local() object
school = local()

def func1(name):
    # 给全局对象添加一个属性叫student,并赋值
    school.student = name
    func2()

def func2():
    # 打印出的是各自线程中的student属性的值，各线程对此变量的操作互不干扰
    print(f'{school.student} from {current_thread().name}')

if __name__ == '__main__':
    
    t1 = Thread(target = func1, args = ('bob',), name = 'thread*No.1')
    t2 = Thread(target = func1, args = ('tom',), name = 'thread*No.2')
    t1.start()
    t2.start()
