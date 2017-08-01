# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 09:59:59 2017

@author: yishipeng
"""

import numpy as np
list1 = [[20,5],[15,10]]
list2 = [[2,1],[1,4]]
array1 = np.array(list1)
array2 = np.array(list2)

"""
mat转换为矩阵
array转换为数组
单纯从输出的角度讲矩阵和数组木有区别的
价格：A菜市场猪肉20，蔬菜5,B菜市场猪肉15,蔬菜10
二种方案：2斤肉，1斤蔬菜；另一种1斤肉，4斤蔬菜
矩阵能够提供很好的解决方案，得出最低的价格
注意 数组的计算和举证的计算是不通的，数组只是单纯的相乘
"""
mat1 = np.mat(list1)
mat2 = np.mat(list2)


print mat1*mat2

print array1*array2

print "dot用于计算list或者np.array的矩阵乘机"
print np.dot(list1,list2)
print np.dot(array1,array2)

