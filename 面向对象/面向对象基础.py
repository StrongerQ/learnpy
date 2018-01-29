"""
http://www.cnblogs.com/wupeiqi/p/4493506.html
"""

"""
class Bar:

    def foo(self,arg):
        print(self,arg)  #self就是代表调用方法/函数的对象/实例

z1 = Bar()
print(z1)
z1.foo(111)
print('================')
z2 = Bar()
print(z2)
z2.foo(666)

"""

"""
class Bar:

    def foo(self,arg):
        print(self,self.name,self.age,self.gender, arg)     #self就是z,self.name就是z.name的值

z = Bar()
z.name = 'alex'  #向中间人/实例/对象中封装参数
z.age = 84
z.gender = 'zhong'
z.foo(666)
# 第二个中间人,传入的参数不同.
z1 = Bar()
z1.name = 'eric'
z1.age = 73
z1.gender = 'nv'
z1.foo(666)
"""

# class Bar:
#     def __init__(self,n1,n2,n3): #构造方法,在实例创建是自动调用  self==调用它的实例
#         self.nam1=n1   #将参数封装入实例中
#         self.nam2=n2
#         self.nam3=n3
#         self.nam4=n3
#         self.nam5=n3
#         self.nam6=n3
#
#     def foo(self):
#         print(self.nam1,self.nam2,self.nam3,self.nam4,self.nam5,self.nam6)
#
# z = Bar(1,2,3)
# print(z.nam1)
# z.foo()

"""
class Person:

    def __init__(self, name,age):

        #构造方法，构造方法的特性， 类名() 自动执行构造方法

        self.n = name
        self.a = age
        self.x = '0'
    def show(self):
        print('%s-%s' %(self.n, self.a))
lihuan = Person('李欢', 18)
lihuan.show()

hu = Person('互相林', 73)
hu.show()
"""

"""
# 继承
class F: # 父类/基类

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')

class S(F): # 子类/派生类
    def s1(self):
        print('S.s1')

    def f2(self): # 用自己的f2,不再继承父类的f2
        print('S.f2')
        # super(S, self).f2() # 执行父类（基类）中的f2方法
        # F.f2(self)          # 执行父类（基类）中的f2方法,通过类名执行方法需要传入调用他的对象self

obj = S() # 实例化obj
obj.s1() # s1中的self是形参，此时代指 obj
obj.f1() # 调用继承的f1方法,self用于指调用方法的调用者
"""

"""
# Python可以多继承
class Base:
    def a(self):
        print('Base.a')

class F0(Base):
    def a1(self):
        print('F0.a')

class F1(F0):
    def a1(self):
        print('F1.a')

class F2(Base):
    def a1(self):
        print('F2.a')

class S(F1,F2):  #继承优先级从左到右单链寻找继承,同根时根最后继承
    pass

obj = S()
obj.a()
"""

"""
class BaseReuqest:
    def __init__(self):
        print('BaseReuqest.init')
        
class RequestHandler(BaseReuqest):
    def __init__(self):
        print('RequestHandler.init')
        BaseReuqest.__init__(self)  # 执行父类的__init__方法

    def serve_forever(self):
        print('RequestHandler.serve_forever')
        self.process_request() # self是obj,执行的Minx中的方法

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:
    def process_request(self):
        print('minx.process_request')

class Son(Minx, RequestHandler):
    pass

obj = Son()     # 优先级从左到右单链寻找执行第一个找到的__init__
obj.serve_forever()
"""

# import socketserver
# obj = socketserver.ThreadingTCPServer(1,2) # 创建对象，执行init
# obj.serve_forever()

# class Province:
#     country = '中国'  # 静态字段,属于类,对象和类都可以直接访问
#
#     def __init__(self, name):
#         self.name = name  # 普通字段，属于对象,只能通过对象访问

# henan = Province('河南')
# hebei = Province('河北')
# print(Province.country)
# print(hebei.country)
# print(hebei.name)

"""
class Foo:
    def __init__(self):
        self.name ='a'

    def bar(self):  # 普通方法,保存在类中,至少有一个self参数,由对象调用,self是对象
        print('bar') 

    @staticmethod  # 静态方法,保存在类中,可以没有参数,对象和类都可以直接调用
    def sta():
        print('123')

    @staticmethod
    def stat(a1,a2):
        print(a1,a2)

    @classmethod #类方法,保存在类中,至少有一个cls参数,由类直接调用,cls是当前类名Foo
    def classmd(cls):
        print(cls)
        print('classmd')

# Foo.sta()  #静态方法调用
# Foo.stat(1,2)

Foo.classmd() #类方法调用

# obj = Foo() #普通方法调用
# obj.bar()

# obj = Foo() #普通方法调用
# Foo.bar(obj)
"""

"""
class Foo:
    def __init__(self):
        self.name = 'a'
        self.name_list = ['alex']
        
    def bar(self): # self是对象
        print('bar')
        
    @property  # 创建方法为属性,可以直接通过字段方式执行函数
    def perr(self):
        return 123 
    @perr.setter # 创建方法为属性,可以直接通过设置字段方式传入参数执行函数
    def perr(self, val):
        print(val)
    @perr.deleter # 创建方法为属性,可以直接通过删除字段方式执行函数
    def perr(self):
        print(666)

# obj = Foo()
# r = obj.perr
# obj.perr = 123
# del obj.perr

class Pergination:

    def __init__(self, current_page):
        try: # 异常处理 
            p = int(current_page)
        except Exception as e:
            p = 1

        self.page = p
    @property  # 创建属性
    def start(self):
        val = (self.page-1) * 10
        return val

    @property # 创建属性
    def end(self):
        val = self.page * 10
        return val

li = []
for i in range(1000):
    li.append(i)

while True:
    p = input('请输入要查看的页码：') # 1,每页显示10条
    obj = Pergination(p)
    print(li[obj.start:obj.end])

"""

'''
class Foo:

    def f1(self):
        return 123

    def f2(self,v):
        print(v)
    def f3(self):
        print('del')

    per = property(fget=f1,fset=f2,fdel=f3,doc='adfasdfasdfasdf')  #创建属性的第二种方法

    # @property
    # def per(self):
    #     return 123

# obj = Foo()
# ret = obj.per
# print(ret)
# obj.per = 123456
# del obj.per
'''