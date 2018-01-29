'''
    Conditiom([Lock/Rlock]):条件变量也一把锁,默认为Rlock
    还支持
    acquire()   获取锁,返回一个值
    wait()      不满足条件时调用,释放锁进入等待阻塞
    notify()    条件创造后调用,通知wait()池激活一个线程
    notifyAll() 条件创造后调用,通知wait()池激活所有线程
'''
import threading,time
from random import randint
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            print('生产者',self.name,":Append"+str(val),L)
            if lock_con.acquire(): #获取返回值是是否获得锁,默认为Rlock可重复用
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)
class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
                lock_con.acquire()
                if len(L)==0:
                    lock_con.wait()
                print('消费者',self.name,":Delete"+str(L[0]),L)
                del L[0]
                lock_con.release()
                time.sleep(0.25)

if __name__=="__main__":

    L=[]
    lock_con=threading.Condition()
    threads=[]
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()