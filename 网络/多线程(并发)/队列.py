"""
多线程利器(queue)  一种数据结构类型 默认FIFI
内部自己就有一把锁
"""
# import  queue
# #FIFI 先进先出
# d = queue.Queue(2)  #创建队列,可加入参数>>>最大队列数,默认值为0代表无限大
# d.put("rq")
# d.put("qw")
# # d.put("we",False)   #第二个参数为是否阻塞
# b = d.get()
# b = d.get()
# # b = d.get(False)    #参数为是否阻塞
# print(b)
# b.qsize() 返回队列的大小
# b.empty() 如果队列为空，返回True,反之False
# b.full() 如果队列满了，返回True,反之False
# b.join() 实际上意味着等到队列为空，再执行别的操作

# import threading,time
# li=[1,2,3,4,5]  #线程不安全,可能同时取到一个值
# def pri():
#     while li:
#         a=li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except:
#             print('----',a)
#
# t1=threading.Thread(target=pri,args=())
# t1.start()
# t2=threading.Thread(target=pri,args=())
# t2.start()


import threading,queue
from time import sleep
from random import randint
class Production(threading.Thread):
    def run(self):
        while True:
            r=randint(0,100)
            q.put(r)
            print("生产出来%s号包子"%r)
            sleep(1)
class Proces(threading.Thread):
    def run(self):
        while True:
            re=q.get()
            print("吃掉%s号包子"%re)
if __name__=="__main__":
    q=queue.Queue(10)
    threads=[Production(),Production(),Production(),Proces()]
    for t in threads:
        t.start()