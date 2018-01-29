#__author:  Administrator
#date:  2016/10/25
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='666', db='sqlexample', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行存储过程,获取存储过程的结果集，将返回值设置给了  @_存储过程名_序号 =
r1 = cursor.callproc('p11', args=(1, 22, 3, 4))
# set @_p11_0 = 1
# set @_p11_1 = 22
# set @_p11_2 = 3
# set @_p11_3 = 4
# call p11(1, 22, 3, 4)
print(r1)
result1 = cursor.fetchall()
print(result1)

# 获取执行完存储的参数
r2 = cursor.execute("select @_p11_0,@_p11_1,@_p11_2,@_p11_3")
print(r2)
result2 = cursor.fetchall()
print(result2)
conn.commit()
cursor.close()
conn.close()

'''
动态SQL

delimiter \\
DROP PROCEDURE IF EXISTS proc_sql \\
CREATE PROCEDURE proc_sql ()
BEGIN
    declare p1 int;
    set p1 = 11;
    set @p1 = p1;

    PREPARE prod FROM 'select * from tb2 where nid > ?';
    EXECUTE prod USING @p1;
    DEALLOCATE prepare prod; 

END\\
delimiter ;

'''
