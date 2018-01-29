'''
http://www.cnblogs.com/yuanchenqi/articles/5938733.html
编码: 把人类认识的明文转换为计算机认识的二进制
     可见的都是unicode
'''

'''
PY2中只有两种数据类型:   str:     按照utf8等规则编码的bytes类型数据 
                        unicode: unicode就是unicode    #utf8,gbk等是unicode的编码规则
                        str>>解码>>unicode>>编码>>str                                  
                        u = u'中文'
                        str1 = u.encode('gbk')
                        str2 = u.encode('utf8')
                        u1 = str1.decode('gbk')
                        u2 = str2.decode('utf8')

PY3中只有两种数据类型:   str:   就是unicode
                        bytes: 按照utf8等规则编码的bytes类型数据
                        可以相互转换
                        str到bytes: 编码
                        bytes到str: 解码

区别在于把str与bytes分出来,取消了unicode这个类型
计算机存储文件时,按照规则把文件编码为二进制存储,操作文件时操作系统会先打开文件的内容(bytes)全部放入内存,
,解释器按照规则解码成unicode,如果规则不同就会乱码,如果要运行文件,再将unicode编码为二进制执行
'''

'''
s = 'sada袁浩'  #所有字符都存为unicode编码,全球通用
print(type(s)) #str数据类型用Unicode编码存储
#编码
bytes(s,'utf8') #编码,将str按照utf8规则编码的bytes类型
b2 = s.encode('utf8') #编码,将str按照utf8规则编码的bytes类型,同上
#解码
str(b2,'utf8') #解码,将十六进制按照utf8规则解码为str类型
s2 = b2.decode('utf8') #解码,将十六进制按照utf8规则解码为str类型
'''


