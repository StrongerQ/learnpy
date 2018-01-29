'''
http://www.cnblogs.com/alex3714/articles/5161349.html
http://www.cnblogs.com/yuanchenqi/articles/5732581.html
'''
#
# import  sys,os,time,datetime,random
# print(os.getcwd())
# print(sys.path)
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_PATH)
# print(BASE_PATH)
# sys.argv #取命令行输入

'''
搜索路径:sys.path

__file__    当前文件相对路径
if __name__ == '__main__':
'''
# time.time()
# time.strftime()
# time.gmtime()
# time.localtime()
# time.ctime()
# datetime.datetime.now()
# #chr() 按编码表转换字符
# import  subprocess
#
# a = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE)  #stdout将标准输出指向主进程,并且封装到a对象中

# import random
# def v_code():
#     code = ''
#     for i in range(5):
#         x = random.randint(1,2)
#         if x == 1:
#             y = random.randint(0,9) #包括8
#             code = code+str(y)
#         else:
#             y = random.randrange(65,91) #不包括8
#             code = code + chr(y)
#     print(code)
# v_code()

import hashlib

m5 = hashlib.md5()  #生成一个MD5算法对象
m5.update('123456'.encode('utf8')) #使用MD5对象对字符进行转换
print(m5.hexdigest()) #获取十六进制的MD5转换值
m5.update('alex'.encode('utf8')) #使用MD5对象对字符进行转换
# print(m5.digest()) #获取十进制的MD5转换值
print(m5.hexdigest()) #获取十六进制的MD5转换值
m2 = hashlib.md5()
m2.update('123456alex'.encode('utf8'))
print(m2.hexdigest())
#说明上面第二层加密是根据第一层加密的基础上再加密得出的
m3 = hashlib.sha256()
m3.update('123456alex'.encode('utf8'))
print(m3.hexdigest())