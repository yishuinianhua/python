# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 10:35:03 2017

@author: yishipeng
"""

from numpy import random,mat,zeros,ones,eye,diag
import numpy as np
data1=mat(zeros((3,3)));
#创建一个3*3的零矩阵，矩阵这里zeros函数的参数是一个tuple类型(3,3)
data2=mat(ones((2,4)));
#创建一个2*4的1矩阵，默认是浮点型的数据，如果需要时int类型，可以使用dtype=int
data3=mat(random.rand(2,2));
#这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，需要将其转换成#matrix
data4=mat(random.randint(10,size=(3,3)));
#生成一个3*3的0-10之间的随机整数矩阵，如果需要指定下界则可以多加一个参数
data5=mat(random.randint(2,8,size=(2,5)));
#产生一个2-8之间的随机整数矩阵
data6=mat(eye(2,2,dtype=int));
#产生一个2*2的对角矩阵

a1=[1,2,3];
a2=mat(diag(a1));
#生成一个对角线为1、2、3的对角矩阵
"""
T矩阵转置
I矩阵求逆
"""
list1 = [[20,5],[15,10],[40,30]]
mat01 = mat(list1)
print mat01.I
print mat01.T

print "计算矩阵的最大值"
print mat01.max()
print "计算第二列的最大值"
print mat01[:,1].max()
print "计算第二行的最大值"
print mat01[1,:].max()