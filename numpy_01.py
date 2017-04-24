# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 09:02:19 2017

@author: yishipeng
"""

import numpy as np
"""
numpy一维数组
astype类型转换
float转换为int时会自动舍弃小数点
string类型强转的过程中会出现错误
anaconda可以通tab键自动补全
"""
data = [1,0,4,2,7,8,9]
int_arr = np.array(data,dtype=np.int32)
print int_arr.astype(dtype=np.float64)

#print np.array(data,dtype=np.float64)
float_data = [1.0,2.0,7.8,0.5]
print np.array(float_data,dtype=int)

string_data = ['1.0','2.0','3','4']
try:
    int_data = np.array(string_data,dtype=int)
    print int_arr
except BaseException,e:
    print e
"""
numpy二维数组
打印数组的维度
生产3*6 的二维数组
arange 类似于python range功能
"""
data = [['a','b','c'],[0,4,1]]
two_array = np.array(data)
#print two_array.shape

#print np.zeros((3,6))

#print np.arange(20)
print "----------------------------------------------"
print "以下是numpy的测试输出："
print np.random.randn()
print np.random.randint(10)
print "创建一个正方的N×N单位矩阵"
print np.eye(5)
print "申明为特定的数据类型" 
print np.array([1,5,6],dtype=np.float64)
print "随机的二维数组"
print np.random.randn(6,5)
print "数组的排序 实际上array把list转化为array"
sort_array = np.array([4,7,1,0,9])
#print sort_array.sort()
print "reshape   dtype:属性"
print np.arange(15).reshape(3,5)
print np.arange(15).dtype
print "打印数组的维度"              
print sort_array.shape       
print "linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终" 
print "linespace等差数列"       
line = np.linspace(10,20,6)
print line
print line[0:-1]
print "size表示总元素的个数 shape表示维度"
print line.size
print line.shape
print line.ndim

print np.random.rand(10) # 产生一个长度为10，元素值为0-1的随机数的数组
print np.random.randint(10) #产生一个随机的整数
"""
NumPy的数组类被称作 ndarray 。通常被称作数组。注意numpy.array和标准Python库类array.array并不相同，后者只处理一维数组和提供少量功能
"""
                       