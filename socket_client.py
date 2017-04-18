# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:17:34 2017

@author: Administrator
"""

import socket
import time
port=8081
host='localhost'
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    
    s.sendto(b'172.24.138.82 the volue is less than 9.98%',(host,port))
    time.sleep(3)