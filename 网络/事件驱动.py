"""
http://www.cnblogs.com/yuanchenqi/articles/5722574.html
事件驱动编程是一种编程范式，这里程序的执行流由外部事件来决定。它的特点是包含一个事件循环，当外部事件发生时使用回调机制来触发相应的处理
"""
# import socket,select #select监听
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',8000))
# sk.listen(3)
# # sk.setblocking(False)   #设置IO非阻塞

# sk2 = socket.socket()
# sk2.bind(('127.0.0.1',8080))
# sk2.listen(3)
#
# while 1:
#     # conn,addr = sk.accept()
#     r,w,e = select.select([sk,sk2,conn],[],[],1) #监听,返回活动的socket对象列表,水平触发.最后一个参数代表监听时间
#     # 水平触发(有高电平或者低电平触发)  边缘触发(电平变化触发)
#     for obj in r:
#         conn, addr = obj.accept()
#         print('conn',conn)
#
#     print(r)


#***********************server.py
import socket
import select
sk=socket.socket()
sk.bind(("127.0.0.1",8801))
sk.listen(5)
inputs=[sk,]  #创建一个socket对象列表
while True:
    r,w,e=select.select(inputs,[],[],)  #阻塞监听,如果是客户端链接服务器导致sk电平变高,就给r的列表中返回一个sk对象
    #阻塞监听,如果监听到列表中有对象电平变高,就给向的返回列表中添加该对象,并通知进程将数据从系统层copy用户层从而获取到数据,并将电平恢复.
    print(len(r))
    for obj in r:
        if obj==sk:
            conn,add=obj.accept()  #sk接收数据,将电平变低并给该客户端生成一个socket对象
            print(conn)
            inputs.append(conn) #把客户端socket对象添加到列表
        else:
            data_byte=obj.recv(1024)  #接收客户端发来的数据,将客户端对象电平变低
            print(str(data_byte,'utf8'))
            inp=input('回答%s号客户>>>'%inputs.index(obj))
            obj.sendall(bytes(inp,'utf8')) #发送数据给客户端

    print('>>',r)

#***********************client.py

import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8801))

while True:
    inp=input(">>>>")
    sk.sendall(bytes(inp,"utf8"))
    data=sk.recv(1024)
    print(str(data,'utf8'))