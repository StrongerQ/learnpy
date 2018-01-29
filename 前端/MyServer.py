#email: strongeren@163.com
#_autor: smallqiang

import  socket
sk = socket.socket()
address = ('localhost',8080)
sk.bind(address)
sk.listen()
while 1:
    conn,addr = sk.accept()
    s = conn.recv(1024)
    print(s.decode('utf8'))
    with open('HTML表单.html','rb') as f:
        c = f.read()
        conn.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))
        conn.sendall(c)
        conn.close()
