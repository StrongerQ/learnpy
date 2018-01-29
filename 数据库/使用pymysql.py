'''
http://www.cnblogs.com/wupeiqi/articles/5713330.html
'''
import pymysql #刚把文件名字取成pymysql了,报错没发现,弄了好久,搞笑了


# 创建连接
conn = pymysql.connect( host='127.0.0.1', port=3306, user='root', passwd='rq123456', db='test1',charset='utf8')
# 创建游标
# cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)  #自定义字典数据类型游标
cursor = conn.cursor()
# inp = input('>>>: ')
# sql = 'insert into class(caption) VALUE ("%s")'%inp  #增  字符串拼方式
# r = cursor.execute(sql)  #这种操作是禁止,会造成SQ注入 ,非常不安全  例如加入注释--
# r = cursor.execute('insert into class(caption) VALUE (%s)',inp)  #参数形式
# l = [('女','2','静静1'),
#      ('女','2','静静2'),
#      ('女','2','静静3')]
# r = cursor.executemany('insert into student(gender,class_id,sname) VALUE (%s,%s,%s)',l)  #多参数形式
# r = cursor.execute('insert into student(gender,class_id,sname) VALUE (%s,%s,%s)',('女','2','静静'))  #参数形式
r = cursor.execute('insert into class(caption) VALUE ("引号不能一样")')
# r = cursor.execute('update student set sname=%s where sid=%s',('马打狗',1))  #改
# r = cursor.execute('delete from score where sid=%s',(49,))  #删
# print(r) #返回收影响行数
# 提交，不然无法保存新建或者修改的数据
conn.commit()
new_id = cursor.lastrowid  #获取最后一条增加的的自增id
print(new_id)
# r = cursor.execute('select * from student')  #查不用commit
# result = cursor.fetchall() #取全部
# result = cursor.fetchone() #取一个
# result = cursor.fetchmany(3) #取指定条
# cursor.scroll(0,"absolute") #绝对位置移动
# cursor.scroll(1,"relative") #相对位置移动
# print(result)
# r = cursor.execute('delete from score where sid=%s',(49,))  #删

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
