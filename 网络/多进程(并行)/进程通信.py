# from multiprocessing import Process, Queue  #此队列是在multiprocessing下的,与普通Queue不一样
#
# def f(q,n):  #因为进程直接无法资源共享,所以需要把queue传递给子进程
#     q.put(n)
#     print(id(q))
#
# if __name__ == '__main__':
#     q = Queue()
#     print(id(q))
#     p_list=[]
#     for i in range(3):
#         p = Process(target=f, args=(q,i))
#         p_list.append(p)
#         p.start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     for i in p_list:
#             i.join()


from multiprocessing import Process, Pipe  #管道通信,类似于socket
def f(conn):  #接收到子进程对象
    conn.send([42, None, 'hello'])  #发送数据
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe() #获取子进程和父进程的管道对象
    p = Process(target=f, args=(child_conn,)) #发送子进程对象
    p.start()
    print(parent_conn.recv())  #接收子进程发送的数据
    p.join()
                     