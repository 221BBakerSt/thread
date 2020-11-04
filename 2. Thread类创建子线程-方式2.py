import threading
import time

class NewThread(threading.Thread):

    # 此处方法必须命名为run，且带self，其他随意命名都不行，因为父类的start()会自动调用子类重写的run()
    def run(self):
        
        # Call parent class' run() method
        threading.Thread.run(self)
        # Call parent class' run() method
        # super().run()
        print(f"I'm {self.name}")
        time.sleep(1)
    
if __name__ == '__main__':

    start = time.perf_counter()

    for _ in range(5):
        t = NewThread()
        t.start()
    t.join()

    end = time.perf_counter()
    print(round(end - start, 5))