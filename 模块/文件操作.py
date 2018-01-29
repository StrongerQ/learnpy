'''
http://www.cnblogs.com/yuanchenqi/articles/5732581.html
文件一旦创建完成后内容就无法修改,只能新建或者覆盖
'''

# dic = str({"1":"111"})
# f = open('test','w',encoding='utf8')   #打开或创建一个文件,并创建一个该文件的对象
# f.read(num) #num为你像读的字符数
# w/r/a  写(先清空)/读/追加/
# w+/r+/a+  可读写-先写(先清空)再把光标指向最后再读/可读写-读光标指向最后再写/可读写-光标一开始就指向最后写了再读
# f.truncate(size) #内容截断
# f.flush()  #将缓存直接写入文件
# f.write(dic)           #向对象中写入数据
# f.close()
# f = open("test","r")
# date = f.read()
# print(eval(date)["1"])
# with open('path','wb') as f:
#     f.write('content')
# with open('path','wb') as f1, open('path2','rb') as f2:  #同时打开两个对象
# f.readline() #一行一行读
# f.readlines() #一个所有行的列表
# f.tell() #返回一个光标位置
# f.seek(num) #设置光标位置num

'''
文本是不可在原文件里修改的,只能重写一个修改后的新文件
'''



'''
序列化 json(适用于普通数据类型,函数类等高级数据无法序列化)
        def a():
            pass
        date = json.dumps(a) 不可以这样序列
      pickle(python自有的序列化模块,适用一切python数据类型)
        def a():
            pass
        date = pickle.dumps(a) 可以这样序列,但是只是序列化一个函数的内存地址
      dump(),load()与dumps(),loads()区别:
          date = json.dumps(dic)
          date = f.write(date)
          等价于
          date = json.dump(dic,f)

          date = f.read()
          date = json.loads(date)
          等价于
          date = json.load(f)
两种模块方法一样
'''
import json,pickle
# dic = {"name":"alex","age":"18",}
# date = json.dumps(dic)
# f = open("JSON_text","w")
# f.write(date)
# f.close()
#
# f = open('JJSON_text','r')
# date = f.read()
# date = json.loads(date)
# print(date["name"])
# f.close()

'''
shelve 序列化模块,基于pickle 只有一个open函数,返回类似字典的对象,可读写,key字符串,值支持所有python数据类型
字典补充:
    dic.get(key,default) 如果key不存在就返回default
'''
import shelve
f = shelve.open('shelve_text')
f['info'] = {'name':'alex','age':'18'}
f['shopping'] = {'good':'bb','wrong':'aa'}
data = f.get("info")
print(data['name'])
f.close()