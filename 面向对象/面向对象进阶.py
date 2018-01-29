"""
http://www.cnblogs.com/wupeiqi/p/4766801.html
"""

"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self.__age = age # 私有化字段，外部无法直接访问

    def show(self):
        return self.__age


obj = Foo('alex', 19)
print(obj.name)
# obj.age   #无法访问,只能通过内部调用
# print(obj.__age)
ret = obj.show()  #可以间接访问私有字段
print(ret)
"""

"""
class Foo:
    __v = '123'  #私有化静态字段

    def __init__(self):
        pass
    def show(self):
        return Foo.__v
    @staticmethod  #静态方法
    def stat():
        return Foo.__v
# print(Foo.__v)
# ret = Foo().show()
# print(ret)

ret = Foo.stat()
print(ret)
"""

"""
class Foo:
    def __f1(self):
        return 123

    def f2(self):
        r = self.__f1()
        return r

obj = Foo()
ret = obj.f2()  #在外部间接拿到私有方法
print(ret)
"""

"""
class F:
    def __init__(self):
        self.ge = 123
        self.__gene = 123 # 父类的私有无法继承给子类

class S(F):
    def __init__(self,name):
        self.name = name
        self.__age = 18
        super(S, self).__init__()

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.ge)
        print(self.__gene) # 父类的私有无法继承给子类

s = S('alex')
s.show()
"""

"""
class Foo:
    def __init__(self):
        print('init')

    def __call__(self, *args, **kwargs):  #对象的构造函数,对象后面加括号可直接执行
        print('call')

# obj = Foo()
# obj()   #对象后面加括号可以直接执行__call__
Foo()()
"""
# s = "123"
# # s = str('123')
#
# i = int(s)
# print(i,type(i))

"""
class Foo:

    def __init__(self):
        pass

    def __int__(self): # 函数中的特殊方法__int__,int对象时调用
        return 1111

    def __str__(self): # 函数中的特殊方法__str__,str对象时调用
        return 'alex'

obj = Foo()
print(obj, type(obj))

r = int(obj) # int后加对象，自动执行对象中的 __int__方法，并将返回值赋值给int对象
print(r)     #  print字符串时自动执行str()>>>print(str(r))
i = str(obj) # str后加对象，自动执行对象中的 __str__方法，并将返回值赋值给str对象
print(i)     # 相当于print(str(i)),自动会i对象的调用__str__方法,获取返回值

"""

"""
class Foo:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __add__(self, other):
        # self = obj1 (alex,19)
        # other = obj2(eric,66)
        # return self.age + other.age
        #return Foo('tt',99)
        return Foo(obj1.name, other.age)

    def __del__(self):
        print('析构方法') # python在对象未使用时,对象会被销毁（）时，自动执行

obj1 = Foo('alex', 19)
obj2 = Foo('eirc', 66)

r = obj1 + obj2  #执行对象__add__方法,__add__需要自定义
# 两个对象相加时，自动执行第一个对象的的 __add__方法，并且将第二个对象当作参数传递进入
print(r,type(r))
"""


"""
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.n = 123

# obj = Foo('alex', 18)
#
# d = obj.__dict__    #将对象中所有的封装内容通过字典返回
# print(d)

# ret = Foo.__dict__  #将类中所有的成员通过字典返回,可见不可见都展示出来
# print(ret)
"""

# li = [11,22,33,44]
# li = list([11,22,33,44])
#
# li[3]
# #
#
# li[3] = 666
#
# del li[2]

"""
class Foo:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item): 
        return item+10

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)
li = Foo('alex', 18)
r= li[8]           # 自动执行li对象的类中的 __getitem__方法，8当作参数传递给item
li[100] = "asdf"   # 自动执行li对象的类中的 __setitem__方法,100和'asdf'作为参数传入item,value
del li[999]        # 自动执行li对象的类中的 __delitem__方法,999作为参数传入key
"""
"""
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __getitem__(self, item):
        # return item+10
        # 如果item是基本类型：int，str，索引获取
        # slice对象的话，切片
        if type(item) == slice:  #slice类
            print('调用这希望内部做切片处理')
        else:
            print(item.start)    #slice的属性
            print(item.stop)
            print(item.step)
            print('调用这希望内部做索引处理')
    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)

li = Foo('alex', 18)
li[123]
li[1:4:2]
li[1:3] = [11,22]
del li[1:3]
"""
"""
class Foo:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([11,22,33])
li = Foo('alex', 18)
# 如果类中有 __iter__ 方法，对象就叫做可迭代对象
# 对象.__iter__() 的返回值： 迭代器
# for循环遇到迭代器直接执行next
# for循环遇到可迭代对象，先执行对象的__iter__()获取迭代器在执行next
# 1、执行li对象的类F类中的 __iter__方法，并获取其返回值
# 2、循环上一步中返回的对象
for i in li:
    print(i)
"""
# li = [11,22,33,44]
# li= list([11,22,33,44])
# for item in li:
#     print(item)

"""
    # python中一切事物都是对象,类都是type的对象
class MyType(type):
    def __init__(self,*args, **kwargs):
        # self=Foo
        print(123)
        pass

    def __call__(self, *args, **kwargs): #对象后面加(),执行__call__方法
        # self=Foo
        obj = self.__new__(self,*args,**kwargs) #执行类的__new__
        self.__init__(obj) #真正的执行__init__
                
class Foo(object,metaclass=MyType): #修改类由自定义type创建
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):  #执行object的__new__方法返回类的对象
        return object.__new__(cls,*args,**kwargs) #返回类的对象

    def func(self):
        print('hello wupeiqi')

obj = Foo()
class Bar:
    def __init__(self):
        print(123)
obj = Bar()
"""

"""
    #   异常处理 
while True:
    try:
        # 代码块，逻辑
        inp = input('请输入序号：')
        i = int(inp)
    except Exception as e:  #Exception可以捕获所以错误
        # e是Exception对象，对象中封装了错误信息
        # 上述代码块如果出错，自动执行当前块的内容
        print(e)
        i = 1
    print(i)
"""
#li = [11,22]
#li[999] # IndexError
# int('qwe') # ValueError
"""
def fun():
    ret = 0
    try:                     #异常处理
        li = [11, 22]
        li[99]               #执行出错后后面的代码不再执行
        int('w3r')

    except IndexError as e:  # 捕获特定异常
        print('IndexError',e)
    except ValueError as e:
        print('ValueError',e)
    except Exception as e:   #捕获所以异常
        print('Exception',e)
    else:                    #没有异常是执行
        ret = 1
        print('elese')
    finally:                 #最终都要执行
        print('....')

    return ret
r = fun()
if r == 0:
    print('500')
else:
    pass

"""
"""
try:
    # int('asdf')
    # raise Exception('不过了...')  #主动触发异常
except Exception as e:
    print(e)

def db():
    # return True
    return False

def index():
    try:
        r = input(">>")
        int(r)
        result = db()
        if not result:
            r = open('log','a')
            r.write('数据库处理错误')
            # 打开文件，写日志
            #raise Exception('数据库处理错误')
    except Exception as e:
        str_error = str(e)
        print(str_error)
        r = open('log', 'a')
        r.write(str_error)
        # 打开文件，写日志

index()
"""

"""
class OldBoyError(Exception):  #自定义异常

    def __init__(self, msg):
        self.message = msg

    def __str__(self):        #可以让对象直接获取__str__的返回值
        return self.message

# obj = OldBoyError('xxx')
# print(obj)
try:
    raise OldBoyError('我错了...')
except OldBoyError as e:
    print(e)# e对象的__str__()方法，获取返回

"""

# assert 条件,断言，用于强制用户服从，不服从就报错，可捕获，一般不捕获
# print(23)
# assert 1==2  #抛出AssertionError错误
# print(456)


"""
    #   反射
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def show(self):
        return  "%s-%s " %(self.name,self.age)
    def __int__(self):
        return 123
    def __str__(self):
        return 'uuu'
obj = Foo('alex', 18)

r = int(obj) # r = 123
u = str(obj)
b = 'name'
"""
# getattr(obj,'str')  获取一个值
# hasattr(obj,'str')   查看对象中是否存在str
# setattr(obj,'name','value')   设置一个值,放在对象的内存中
# delattr(obj,'name')  删除一个值
# 通过字符串的形式操作对象中的成员

# func = getattr(obj, 'show')
# print(hasattr(obj, 'name'))
# setattr(obj, 'k1', 'v1')
# delattr(obj, 'name')
"""

class Foo:

    stat = '123'

    def __init__(self, name,age):
        self.name = name
        self.age = age

# 通过字符串的形式操作对象中的成员
r = getattr(Foo, 'stat')
print(r)
"""

"""
import s2  #倒入模块s2,s2也是一个对象,python中一切都是对象

# r1 = s2.NAME
# print(r1)
# r2 = s2.func()
# print(r2)
r1 = getattr(s2, 'NAME')
print(r1)
r2 = getattr(s2, 'func')
result = r2()
print(result)
cls = getattr(s2, 'Foo')
print(cls)
obj = cls()
print(obj)
print(obj.name)
"""
"""
import s2
inp = input('请输入要查看的URL：')
if hasattr(s2, inp):
    func = getattr(s2, inp)
    result = func()
    print(result)
else:
    print('404')
"""

# class Foo:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

# obj = Foo() # obj对象，obj也成为Foo类的 实例，（实例化）
# obj1 = Foo()
# obj2 = Foo()
# obj3 = Foo()

# 单例，用于使用同一份实例（对象） 类似于英雄联盟不能双开
class Foo:
    __v = None    #创建私有静态字段
    @classmethod  #类方法
    def get_instance(cls): #创建单例模式方法
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

# 不再使用类()创建对象,使用get_instance()创建单例
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
obj3 = Foo.get_instance()
print(obj3)