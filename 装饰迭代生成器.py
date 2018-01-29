'''
http://www.cnblogs.com/yuanchenqi/articles/5830025.html
http://www.cnblogs.com/yuanchenqi/articles/5769491.html
'''
'''
闭包
def outer():
    x=10
    def inner():
        print(x)
    return inner
outer()()
'''

'''
装饰器

def decrators(func): #函数func无参数
    def wrapper():
        print('ok1')
        func()
        return print('ok2')
    return wrapper
func = decrators(func) # ==  @decrators 

def decrators(func): #函数func有参数
    def wapper(*args,*kwargs):
        print('ok1')
        func(*args,*kwargs)
        return print('ok2')
    return wapper
@decrators #== func == decrators(func)

def loger(flag): #给装饰器传递了一个参数
    def decrators(func): 
        def wapper(*args,*kwargs): #函数func有参数
            print('ok1')
            func(*args,*kwargs)
            return print('ok2')
        return wapper
    :return decrators
@logger(flag) == @decrators 但是给装饰器传递了一个参数
'''

'''
生成器   # 值都不存在,要一个生成一个 
创建的两种方法:
1:   s = (x*2 for x in range(10)) #生成一个生成器
     next(s)  # == s.__next__() #返回生成一个值,next()取值,取完了就报错
     a,b = (1,2)  #next()是生成器的方法

2:  def f():
        count = yield 2  #生成一个生成器
        print("ok")
    x = f()            #启动生成器,生成一个生成器对象
    next(x)            #执行函数,到yield阻塞,并返回一个值
    x.send(num)        #取消阻塞继续执行,并把参数传递给yield前面的变量赋值
                       #但是send不能第一次进入生成器就用,除非send(None)

'''
# def fb(max): #斐波拉切
#     n,s,e = 0,0,1
#     while n < max:
#         print(s)
#         s,e = e,s+e
#         n += 1
# fb(10)

def fb(max): #斐波拉切
    n,s,e = 0,0,1
    while n < max:
        yield s
        s,e = e,s+e
        n += 1
# print(next(fb(10))) 这样不对 ,每次都会从新生成一个生成器对象
# print(next(fb(10))) 这样不对 ,每次都会从新生成一个生成器对象
x = fb(10)
print(next(x))
print(next(x))
print(next(x))



'''    
迭代器: 
生成器都是迭代器,迭代器不一定是生成器
满足:
1.内部有next()
2.内部有iter()方法 #iter(list) 返回一个列表生成的迭代器对象
for x in i:          
        print(i)
for循环后面接的可迭代对象
    可迭代对象:内部有iter的
for循环内部做了三件事:
    1.调用可迭代对象iter方法返回一个迭代器对象
    2.迭代器对象调用next方法
    3.异常处理

'''
from collections import Iterable
i = [1,2,3]
x=isinstance(i,Iterable)
print(x)