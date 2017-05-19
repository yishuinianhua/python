# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:54:52 2017

@author: Administrator
"""

import numpy as np
import pandas as pd

"""
产生一个连续的时间序列
"""
datas = pd.date_range('20170410',periods=6)
#print datas
#df = pd.DataFrame(np.random.randn(10,4),index=datas,columns=list('ABCD'))
"""
通过字典的方式创建DataFrame
index表示行,columns表示列
"""
df = pd.DataFrame([[1,0,9,8],[2,3,4,5],[0,9,8,7],[4,1,2,0],[6,7,1,3],[0,-1,-2,-6]],index=datas,columns=list('ZXCV'))
print df
"""
sum求和函数
"""
print df.sum()
"""
将一个 lambda 表达式应用到每列数据里
"""
#print df.drop['Z']
fun = lambda x : x + 2
print df.apply(fun)
"""
显示head,tail,
index:索引,即行
columns:列名
values:值,
T:转置,按值进行排序,按轴进行排序
sort_index按照行索引排序
sort_index(axis=1)按照列名排序
"""
#print df
#print df.head
#print df.tail(2)
#print df.index
#print df.columns
#print df.values
#print df.T
#print df.sort_index() 
#print df.sort_values(by='X')
#print df.sort_index(axis=1,ascending=True) #按照C V X Z排序
#print df.sort_values(by='B') #按照B这一列进行排序
"""
选择,切片
"""
#print df['B'] <==> df.B
#print df[0:1] #这个输出的是行
#print df['20170412':'20170413']
#print df.loc[datas[0]]
#print df.loc[:,['A','C']]
"""
[]表示任选其一
"""
#print df.loc['20170412':'20170415',['C','D']]
#print df.loc[datas[0],'B']
#print df.at[pd.Timestamp('20170522'),'B'] #at必须使用时间戳的形式，否则会报错的
"""
通过数值进行切片
"""
#print df.iloc[[1,3,5],[2]]
#print df.iloc[2] #行数据
#print df.iloc[:,1:3] # 对行进行切片
#print df.iloc[1:2,:] # 对列进行切片
#print df.iloc[0,0]
#print df.iat[1,1] #iat效率泌iloc效率高得多
"""
布尔
"""
#print df[df.A>0]
#print df[df>0]
"""
DataFrame按照值和索引进行排序
"""
