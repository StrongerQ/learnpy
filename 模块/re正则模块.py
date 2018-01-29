import hashlib,re
# m = hashlib.md5()
# m.update('hello '.encode('utf8'))
# n = m.hexdigest()

'''
    RE模块    正则(贪婪)    元字符

.   任意一个字符,除了换行符(\n)
^   开始去匹配(^a)
$   在结尾来匹配(a$)
*   [0,无穷) 重复匹配，零到多次(.*)
+   [1,无穷) 重复匹配，一到多次(b+)
?   [0,1] 只匹配零或一次(a?b)
{}  匹配固定或者区间次数,{1,}默认到正无穷(a{5},a{1,5})
[]  匹配指定区间的一个字符(a[cdw]x,[a-z])  
    特殊功能：取消元字符特殊功能[*]
    除了(\ ^ -)之外 
    -：范围
    ^：取反(括号内所有)
\   1.后面跟元字符去除特殊功能。 2.后面跟普通字符实现特殊功能。
        \D  ：匹配任意非数字字符
        \d  ：匹配任意数字字符
        \S  ：匹配任意非空白字符
        \s  ：匹配任意空白字符
        \W  ：匹配任意非字母数字字符
        \w  ：匹配任意字母数字字符
        \b  ：匹配一个单词边界，也就是只单词与特殊字符间的位置
()  匹配括号中整体((ab)+)    
|   或,匹配管道符左右其一((ab)|2)
(?P<name>\d)    取名匹配

findall()   所以结果返回一个列表
search()    返回匹配到的第一个对象,可以调用group()
match()     返回匹配到的第一个对象,也可以调用group(),只在字符串开始匹配
split()     按顺序与规则拆分,返回列表
sub()       按规则替换字符
compile()   将规则编译为obj,然后可以使用obj.func()

'''
# ret = re.findall('s.*b','sdasfasfasfssfb')
# x = re.search('s.*b','sdasfasfasfssfb').group()
# x1 = re.findall('\\\\','a\dc')
# x2 = re.findall(r'\\','a\dc')
# x3 = re.search('\\bblow','blow').group()
# x3 = re.search(r'\bblow','blow').group()
# x = re.search('(?P<GG >\w)','sdasfasfasfssfb')
# x = re.split('[k,s]','sdasfasfasfssfb')
# x = re.finditer('\d','dasalbbd5jdb43ed21xfsf')
# x = re.sub('a.+x','ssbb','dasalbbjbexfsf')
# obj = re.compile('\\\\')
obj = re.compile(r'\\')
# x = obj.findall('\dsad\d')
# b1='asdadascasc'
# b=b1.replace('a','1')
# print(x.group('GG'))
# print(b1)
x = next(x).group()
print(x)