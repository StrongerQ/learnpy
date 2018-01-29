#Rlock()递归锁
#锁可以确保数据安全
#死锁,锁没释放,别的线程就阻塞
import threading
class mythread(threading.Thread):
    def doA(self):
        # lockA.acquire()
        lock.acquire()
        print(self.name,'lockA')
        lock.acquire()
        # lockB.acquire()
        print(self.name,"lockB")
        # lockB.release()
        lock.release()
        # lockA.release()
        lock.release()
    def doB(self):
        lock.acquire()
        # lockB.acquire()
        print(self.name,'lockB')
        lock.acquire()
        # lockA.acquire()
        print(self.name,"lockA")
        lock.release()
        # lockA.release()
        # lockB.release()
        lock.release()
    def run(self):
        self.doA()
        self.doB()

if __name__ == "__main__":
    # lockA = threading.Lock() #获取一个锁对象A
    # lockB = threading.Lock() #获取一个锁对象B
    lock = threading.RLock() #获取一个递归锁对象,可以重用,防止死锁
    threads = []
    for i in range(5):
        threads.append(mythread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
