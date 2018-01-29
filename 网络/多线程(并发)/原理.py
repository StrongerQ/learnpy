'''
http://www.cnblogs.com/yuanchenqi/articles/5733873.html
    能让OS工作起来的最小单位就是一个线程
    一个指令集就是一个线程
    资源可以共享  类似一个软件里的不同功能
    I0(有阻塞)密集   使用多线程
    CPU(计算)密集   使用多进程
    多线程是竞争式,协程是商量着来
'''
# import time #一个线程
# def foo():
#     print(1)
#     time.sleep(1)
# def too():
#     print(2)
#     time.sleep(1)
# foo()
# too()

'''子线程主线程不分先后一起执行,主线程结束的等子线程结束后才最终结束'''
# import threading,time  # threading是多线程模块
# def foo(x):
#     print(x)
#     time.sleep(1) #io阻塞
# def too(y):
#     print(y)
#     time.sleep(1)
# t1 = threading.Thread(target=foo,args=(2,))  #创建参数为2的foo方法的一个子线程对象
# t2 = threading.Thread(target=too,args=(2,))  #创建参数为2的too方法的一个子线程对象
# t1.etDaemon(True) #设置t1为守护进程,主线程结束子线程也就结束了不再执行下去,得放置在start前面
# t1.start() #启动子线程
# t2.start() #启动子线程
# t1.join() #t1执行完再往下走
# t2.join() #同上
# print('主线程')  #主线程
'''
join() #哪个线程对象调用,阻塞哪个线程,等待线程执行完成后执行下面的代码
'''
'''
setDaemon()
'''
# threading.current_thread() #查看当前线程
# threading.active_count()    #当前活动线程数
'''通过自定义类MyThread创建多线程'''
import threading
class MyThread(threading.Thread): #自定义一个类继承于Thread
    def __init__(self,num):
        threading.Thread.__init__(self)  #继承父类的__init __
        self.num = num
    def run(self):
        print('%s somethings'%self.num)
t1 = MyThread(1)  #执行构造函数,创建对象
t2 = MyThread(2)
t1.start()
t2.start()