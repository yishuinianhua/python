# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:39:17 2017

@author: Administrator
"""

import pandas as pd
import numpy as np

#print np.random.randint(2,10,size=5)
"""
linspace等差数列
参考python range
randn是正态分布
rand随机数
randint是随机整数
"""
print np.linspace(0,20,5)
print np.arange(5)
print np.random.rand()
print np.random.randn()
ss = pd.Series([1,0,np.nan,9,6])
#print ss
"""
将python字典转换为数组
"""
dic = {'name':'zhangsan','age':80,'sex':'M'}
s = pd.Series(dic)
#print s
"""
指定索引
输出索引index
输出值values
打印大于0
"""
s1 = pd.Series([1,-1,0,9,8],index=['z','x','c','v','b'])
#print s1
#print s1.index
#print s1.values
#print s1[s1>0]
"""
按照索引进行排序
按照值进行排序
"""
print s1.sort_index(ascending=False)
print s1.sort_values(ascending=False)