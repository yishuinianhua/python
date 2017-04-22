# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:10:38 2017

@author: Administrator
"""

import socket
import re
port=8081
"""
AF_INET表示ipv4
SOCK_DGRAM表示UDP协议
"""
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#从指定的端口，从任何发送者，接收UDP数据
#绑定ip，端口
s.bind(('',port))
print('正在等待接入...')
while True:
    #接收一个数据
    data,addr=s.recvfrom(1024)
    print re.compile(r'\d+\.\d+\.\d+\.\d+').search(data).group()
    #将客户端信息原封不懂的发回去
    s.sendto(data,addr)
    #print('Received:',data,'from',addr)
s.close()