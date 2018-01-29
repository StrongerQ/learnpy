'''
http://www.cnblogs.com/yuanchenqi/articles/5692716.html
                网络通信三步
   确认IP地址----确认程序端口----确认通讯协议
                传输协议
udp  不可靠传输协议,直接发信息,不管谁和接受与否,但是速度快
tcp  可靠的三次握手  1.发接受信息 2.对方回确认信息 3.回对方确认知道信息 缺点速度慢

serve下的方法   serve的socket只是绑定端口等待连接
    bind()
    listen()
    accept() #阻塞
    recv()   #阻塞
    send()   #传输的类型必须的bytes类型
    sendall()
    close()  #关闭服务器的接受
    setblocking(bool) #是否阻塞,默认True
client下的方法  clicent的socket是互相通讯用
    connect()
    recv()
    send()
    sendall()
    close() #关闭与服务器之间链接
'''
# import socket

"""
实现服务器的多并发
"""
import socketserver     #里面封装了socket套接字的创建和多线程多进程等功能
class Myserver(socketserver.BaseRequestHandler):   #继承socketserver中的BaseRequestHandler
    def handle(self):                              #继承并重写父类的方法
        conn = self.request  #获取客户端的socket对象
        arddress = self.client_address  # 获取客户端的地址与端口
        pass #正常的逻辑功能代码
        conn.close()
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),Myserver)  #创建socketserver对象,执行__init__
    #ThreadingTCPServer多线程TCP服务器(address,Myclass)
    server.serve_forever()   #启动服务器,执行handle方法
    server.server_close()