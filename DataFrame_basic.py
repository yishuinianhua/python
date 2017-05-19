# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:26:57 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
hand = ['one','two','three']
lie = ['A','B','C','D']
data = [['q','w','e','r'],[1,2,3,4],['Django','scrapy','pandas','skitlearn']]
d = pd.DataFrame(data,index=hand,columns=lie)

nf = pd.Series([1,4,7,np.nan],index=['Z','X','C','V'])
#print nf.reindex()
df = pd.DataFrame(np.random.randn(6,4),index=list('ABCDEF'),columns=list('qwer'))
#新增gift列
df['gift'] = ['python','django','pandas','scrapy',np.nan,np.nan]
#第一个any会筛选列
pd.isnull(df).any().any()
"""
fillna补全缺失的值
dropna删除缺失的值
规律是对数据的操作都不会更改原来的数据
reindex重新索引
"""
print nf.dropna(how='any')
print nf.fillna(value=10)
nf1 = nf.reindex(['Z','X','C','V','F'],fill_value=100)
print nf1

"""
以下是DataFrmae数据切片
类似字典的方法选择DataFrame列
loc/iloc输出行
"""

print d['B']
print d.loc['one']
print "======================="
print d.iloc[0:3]
print d.C  > 2
print d.C

"""
丢弃一列axis关键字
drop默认后面就是行
drop是拷贝一份数据出来,d保持以前的数据
apply整个DataFrame应用lambda匿名函数
x.max()-x.min()默认是按照列,axis=1转换为按照行
"""
print d.drop('D',axis=1)
print d.drop('three')
df = pd.DataFrame([[1,2,3],[4,5,6]])
print df.apply(lambda x:x+2)
print df.apply(lambda x:x.max() - x.min(),axis=1)


