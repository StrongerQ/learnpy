#Lock()同步锁
import threading,time
num = 100
class mythread(threading.Thread):
    def __init__(self,obj):
        threading.Thread.__init__(self)
        self.obj = obj
    def run(self):
        global num  #声明全局
        l.acquire() #加锁,使局部串行
        # num -= self.obj
        n = num  #任务未执行完成CPU就切换了,所以部分n获取的值一样,线程不安全,加同步锁来解决
        time.sleep(0.000001)
        print(n)
        num = n - self.obj
        l.release() #开锁
        time.sleep(1) #检查是传行还是并行
l = threading.Lock() #获取一个同步锁对象
for i in range(100):
    r = mythread(1)
    r.start()
print(num)