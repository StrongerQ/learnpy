# BoundedSemaphore(num) 信号量也是一把锁,可以同时进多个线程(看似)
import threading,time,random
class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            times = random.randint(0,3)
            time.sleep(times)
            semaphore.release()
if __name__ == "__main__":
    semaphore = threading.BoundedSemaphore(5)   #可以进5个线程
    thrs = []
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()