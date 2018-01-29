'''
http://www.cnblogs.com/yuanchenqi/articles/5828233.html
'''
'''
深浅拷贝
'''
# s = [[1,2],"laex","elon"]
# s2 = s.copy()   #浅拷贝数据,只拷贝第一层的数据,第二层通过指针指向原来的数据
# s2[1] = "haha"  #修改第一层的数据
# print(s)     #s1数据未改变
# s2[0][0] = 2 #修改s2的数据
# print(s)  #s1的数据被改变

'''
函数 封装一组代码实现一个功能,通过名字调用 
     代码重用,可扩展,保持一致
'''
# def func(*args,**kwargs): #创建函数,传入参数要按顺序
#     pass
# func()   #调用函数
# func(name)# 形式参数
# func(name='good')# 指定/默认参数
'''
函数返回值
'''
# def func():
#     return 'ok'  #函数执行完成返回一个结果
# obj = func()   #获取函数返回值
'''
作用域 (函数,类,模块可以创建)
按照 LEGB 规则寻找 本地/局部/全局/内建 优先级从左到右降低
'''
# x = int(2.9)  #BBBBBBBB
# g_count = 0   #GGGGGGGG
# def outer():
#     o_count = 2 #EEEEEEE
#     def inner():
#         i_count = 2 # LLLLLLL
#         print(i_count)
# #   print(i_count) #往外找,找不到

count = 10
def outer():
    global count  # 声明为全局变量
    print(count) # 需要先声明局部count再print,否则会报错
    count = 5
outer()

