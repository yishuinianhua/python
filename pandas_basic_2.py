# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:47:29 2017

@author: yishipeng
"""

import pandas as pd
import numpy as np
data = [[8,9,0],[1,2,3],[6,4,1],[10,30,20],[20,10,0]]
df = pd.DataFrame(data,index=["A","B","C","D","E"],columns=["one","two","three"])

"""
分组并对每个分组执行sum函数
通过多个列进行分组形成一个层次索引，然后执行函数
"""
#print df.groupby(['one','two']).sum()
s = pd.Series([1,1,1,2,3,3,5,6])
"""
统计数量
"""
#print s.value_counts()
"""
fred时间间隔 M:month D:Day 
"""
#print pd.date_range('3/12/2017',periods=10,freq='M')

""""
以下是画图程序
rand 生成均匀分布的伪随机数。分布在（0~1）之间
randn 生成标准正态分布的伪随机数（均值为0，方差为1）
"""

ts = pd.Series(np.random.randn(200),index=pd.date_range('1/1/2017',periods=200))
ts = ts.cumsum()
ts.plot()
"""
后面10表示产生随机数数组的个数

"""
print np.random.randn(10)