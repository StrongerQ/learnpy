# b = '谢了啊'
# b = b.encode('utf-8')
# b = b.decode('utf-8')
# print(b)
#
# a = b'asd'
# b = bytes("asd","utf8")
# print(a)
# print(b)

# import os
# b = os.path.abspath(__file__)
# print(b)
# c = os.path.dirname(b)
# print(c)
# import random
# x=random.randint(0,10)
# print(x)
# import threading,os
# event = threading.Event()
# # x = (event.isSet() or event.set())
# x = False or event.set()
# print(x)


# import threading,time
# from random import randint
# class Producer(threading.Thread):
#     def run(self):
#         global L
#         val=randint(0,100)
#         print('生产者',self.name,":Append"+str(val),L)
#         if lock_con.acquire():
#             L.append(val)
#             lock_con.notify()
#             lock_con.release()
# class Consumer(threading.Thread):
#     def run(self):
#         global L
#         for x in range(5):
#                 lock_con.acquire()
#                 if len(L)==0:
#                     lock_con.wait()
#                 print('消费者',self.name,":Delete"+str(L[0]),L)
#                 del L[0]
#                 lock_con.release()
#                 time.sleep(0.25)
#
# if __name__=="__main__":
#     L=[]
#     lock_con=threading.Condition()
#     threads=[]
#     for i in range(5):
#         threads.append(Producer())
#     threads.append(Consumer())
#     for t in threads:
#         t.start()
# x = 5     #作用域
# def f(x):
#     if x == 5:
#         x = 10
#         print('inter>>>>',x)
# f(5)
# print(x)

# s = (x * 2 for x in range(10))
# s.__next__() # ==next(s)

# def fb(max):
#     n,s,e = 0,0,1
#     while n < max:
#         print(s)
#         s,e = e,s+e
#         n += 1
# fb(10)

# def fb(max): #斐波拉切
#     n,s,e = 0,0,1
#     while n < max:
#         yield s
#         s,e = e,s+e
#         n += 1
# x1 = fb(10)
