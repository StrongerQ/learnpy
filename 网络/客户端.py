import socket

sk = socket.socket() #创建socket对象,用于与服务器之间数据传递用的
address = ('127.0.0.1',8000) # 服务器的IP地址与端口号
sk.connect(address) # 建立连接
while True:
    data_len = sk.recv(1024) #1024是每次接收最大值
    data_len = int(str(data_len,'utf8'))
    sk.send(bytes("ok","utf8"))
    data = bytes()  #创建一个空数据
    while len(data) != data_len: #按要求循环获取数据直到获取完
        rev = sk.recv(1024) #1024是每次接收最大值
        data += rev
    print(str(data,'utf8')) #接收数据进行编码
    # print(data.decode('utf-8')) #接收数据进行编码
    inp = input('>>>')
    sk.send(bytes(inp, 'utf8'))
    if inp == 'exit':break
