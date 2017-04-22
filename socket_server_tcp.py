import socket
import re
port=8082
"""
AF_INET表示ipv4
SOCK_DGRAM表示UDP协议
"""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#从指定的端口，从任何发送者，接收UDP数据
#绑定ip和端口
s.bind(('',port))
#开始监听 最大允许多少个客户端连接到服务器，但只能和第一个连接的客户端进行通信
s.listen(5)
#等待客户端连接请求，无请求则一直阻塞
clnt,addr = s.accept()
clnt.settimeout(5)
print "client address:",addr
while True:
    #接收一个数据
    try:
        data = clnt.recv(1024)
        if not data:
            break
    except:
        pass
    print "Recieve data:",data
    
    #服务器端返还客户端信息
    clnt.send(data)

clnt.close()    
s.close()