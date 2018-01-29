'''
http://www.cnblogs.com/yuanchenqi/articles/5745958.html
    进程:之歌程序执行的实例
    主进程中创建的子进程是完全拷贝的主进程(消耗巨大)
    进程线程区别:
        线程间能资源共享互相通讯和操作,进程互相独立
    多进程process
    不是指令集,而是一个资源整合,一个进程可以包含多个线程
    不可以资源共享    类似于电脑上不同的软件
    I0(有阻塞)密集   使用多线程
    CPU(计算)密集   使用多进程
    GIL全局解释器锁  Cpython同一时刻一个进程里只能有一个线程进入解释器
    multiprocessing模块中大部分方法和threading一样
'''

# from multiprocessing import Process #多进程模块
# import time
# def f(name):
#     time.sleep(1)
#     print('hello', name,time.ctime())
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):  #有几核就能并行多少个进程,多的就切换来
#         p = Process(target=f, args=('alvin',)) #创建子进程对象
#         p_list.append(p)
#         p.start()
#     for p in p_list:
#         p.join()  #进程执行完毕才向下进行
#     print('end')


# from multiprocessing import Process
# import time
#
# class MyProcess(Process):  #自定义类调用多进程
#     def __init__(self,name):
#         super(MyProcess, self).__init__()
#         self.names = name
#
#     def run(self):
#         time.sleep(1)
#         print ('hello',self.names,self.name,time.ctime())
#
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = MyProcess(i)  #创建一个子进程对象
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()
#
#     print('end')

from multiprocessing import Process
import os
import time
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())  #父进程ID
    print('process id:', os.getpid())      #自己的进程ID

def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    time.sleep(10)
    p = Process(target=info, args=('bob',))
    p.start()
    p.join()