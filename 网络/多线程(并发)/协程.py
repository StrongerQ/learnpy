'''
http://www.cnblogs.com/alex3714/articles/5248247.html
协程:用户态轻量级线程

'''
import time
import queue

'''
利用yield实现协程
'''
# def consumer(name):
#     print("--->ready eating baozi...")
#     while True:
#         new_baozi = yield  #利用yeild形成一个协程并发
#         #通过send给new_baozi一个值
#         print("[%s] is eating baozi %s" % (name, new_baozi))
#         # time.sleep(1)
# def producer():
#     r = con.__next__()  #进入迭代器
#     r = con2.__next__() #进入迭代器
#     n = 0
#     while n < 5:
#         n += 1
#         con.send(n)  #send()不但执行__next__还给yield发送一个值
#         con2.send(n)
#         print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
# if __name__ == '__main__':
#     con = consumer("c1")    #生成一个迭代器对象
#     con2 = consumer("c2")   #生成一个迭代器对象
#     p = producer()


'''
利用greenlet实现协程
'''
# from greenlet import greenlet
#
# def test1():
#     print(12)
#     gr2.switch() #切换到gr2
#     print(34)
#     gr2.switch() #切换到gr2
#
# def test2():
#     print(56)
#     gr1.switch() #切换到gr1
#     print(78)
#
# gr1 = greenlet(test1) #创建一个greenlet对象
# gr2 = greenlet(test2) #创建一个greenlet对象
# gr1.switch()  #切换到gr1对象执行

'''
利用gevent实现协程
'''
# import gevent   #第三方库
#
# def func1():
#     print('\033[31;1m李闯在跟海涛搞...\033[0m')
#     gevent.sleep(2)   #阻塞后切换
#     print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')
#
# def func2():
#     print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
#     gevent.sleep(1)
#     print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')
#
# gevent.joinall([                #把两个方法链接起来
#     gevent.spawn(func1),        #spawn启动函数
#     gevent.spawn(func2),
# ])


from gevent import monkey
monkey.patch_all() #补丁,最大程度检测IO阻塞
import gevent,time
from urllib.request import urlopen #建议爬虫模块

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

star = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),  #spawn(func,*args,**kwargs)
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
end = time.time()
print(end - star)