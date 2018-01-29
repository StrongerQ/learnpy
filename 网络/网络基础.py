'''
http://www.cnblogs.com/linhaifeng/articles/5937962.html
http://www.cnblogs.com/linhaifeng/articles/5951486.html
'''
ord() #数字与ascii值互转
chr() #数字与ascii值互转
'''
ip地址分成两部分

网络部分：标识子网
主机部分：标识主机

ip地址    172.16.10.1：10101100.00010000.00001010.000000001  

子网掩码  255.255.255.0:11111111.11111111.11111111.00000000  #1为网络0为主机

AND运算得网络地址结果：10101100.00010000.00001010.000000001->172.16.10.0>>>网段
syn 请求连接
ack 确认
fin 关闭连接

TCP协议  连接:三次握手
            去吃饭吗么?
            吃啊 走吗?
            走
     断开连接:四次挥手
十三个根DNS地址封装在UDP协议中
根DNS服务器发送数据通过UDP
DNS 翻译官:将域名翻译为ip
     www.baidu.com.
根域: . >>>>顶级域: com >>>>一级域: baidu >>>>二级域: www
'''


'''
arp协议
'''

'''
已知:本机ip,网关ip,本机mac,目标ip

同网段发送数据:

先根据以太网协议打包数据
[源mac(本机mac):目标mac(FF:FF:FF:FF:FF:FF)[源ip(本机ip):目标ip(目标ip)[数据部分]]
广播到子网里,所有服务器接收到,打开第一层查看到mac为FF:FF:FF:FF:FF:FF,继续打开第二层,查看到目标IP不是自己就扔掉包,
是自己就继续打开包,知道是来拿自己mac地址的,就返回自己的MAC地址,做一个返回包:
[源mac(目标mac):目标mac(FF:FF:FF:FF:FF:FF)[源ip(目标ip):目标ip(本机ip)[目标mac数据]],同样广播到子网里,
所有服务器接收到,打开第一层查看到mac为FF:FF:FF:FF:FF:FF,继续打开第二层,查看到目标IP是本机,本机打开获取到目标mac地址,
然后再打包
[源mac(本机mac):目标mac(目标mac)[源ip(本机ip):目标ip(目标ip)[数据部分]]
广播到子网里,所有服务器接收到,目标服务器打开第一层查看到mac是自己,继续打开第二层,查看到目标IP也是自己就继续打开包,获取到数据

不同网段:

先根据以太网协议打包数据
[源mac(本机mac):目标mac(FF:FF:FF:FF:FF:FF)[源ip(本机ip):目标ip(网关ip)[数据部分]]
,广播到子网里,所有服务器接收到,打开第一层查看到mac为FF:FF:FF:FF:FF:FF,继续打开第二层,查看到目标IP不是自己就扔掉包,
网关拿到包打继续打开,知道是来拿自己mac地址的,就返回自己的MAC地址,做一个返回包:
[源mac(网关mac):目标mac(FF:FF:FF:FF:FF:FF)[源ip(网关ip):目标ip(本机ip)[网关mac数据]],同样广播到子网里,
所有服务器接收到,打开第一层查看到mac为FF:FF:FF:FF:FF:FF,继续打开第二层,查看到目标IP不是自己就扔掉包,
本机获取到包,继续打开获取到网关mac数据.然后继续打包:
[源mac(本机mac):目标mac(网关mac)[源ip(本机ip):目标ip(目标ip)[数据部分]]
同样广播到子网里,所有服务器接收到,打开第一层查看到mac不是自己就扔掉,网关拿到后继续打开第二层,查看到真正需要的目标IP,
然后通过路由发送数据到目标ip的网关.
'''