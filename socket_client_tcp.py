# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:49:30 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:17:34 2017

@author: Administrator
"""

import socket
import time
port=8082
host='localhost'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((host,port))
    while True:
        print "enter something"
        content = raw_input()
        s.send(content)
        time.sleep(1)
        #接受来自服务器的数据
        data = s.recv(1024)
        print "---",data
except socket.error,e:
    print e
except socket.timeout,e:
    print e
s.close()