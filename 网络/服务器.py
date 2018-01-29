import  socket  # 网络接口模块,建立连接通讯  类似电话线

sk = socket.socket() #创建socket对象 等待链接用 ,套接字,里面默认值有协议和网络类型
address = ('127.0.0.1',8000)
sk.bind(address) #绑定IP地址和端口
sk.listen(3)  #设置排队人数
print('waiting......')
conn,addr = sk.accept()  #此处的conn就是客户端的socket,用于传输用
# print(conn)
while True:
    inp = input('>>>')
    result = len(inp) #获取数据长度
    conn.send(bytes(str(result),'utf8'))
    rc = conn.recv(1024)  #防止粘包
    print(str(rc,'utf8'))
    conn.send(bytes(inp,'utf8')) #传输的类型必须的bytes类型
    # conn.send(inp.encode("utf-8")) #传输的类型必须的bytes类型
    data = conn.recv(1024)
    print(str(data, 'utf8'))
    if not data:
        conn.close()
        # conn, addr = sk.accept()
        # print(addr)
        try:
            conn, addr = sk.accept()
            print(addr)
        except:
            pass
sk.close()