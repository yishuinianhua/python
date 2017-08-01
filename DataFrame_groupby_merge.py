# -*- coding: utf-8 -*-
"""
Created on Fri May 19 21:33:02 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
df1 = pd.DataFrame({'A':2,'B':['foo','bar','foo','bar','bar'],'C':[4,5,6,7,8],'D':np.random.randint(1,10,size=5)})
#grouby分组，groupby进行求和
#print df1.groupby('B').sum()

left = pd.DataFrame([['foo',1],['foo',2]],columns=['key','lval'])
right = pd.DataFrame([['foo',4],['foo',5]],columns=['key','rval'])
print left
print right
#select * from left inner join right on left.key = right.key
#合并数据
print pd.merge(left,right,on='key')
#似乎ignore_index并木有生效 索引必须要相同
left1 = left.append(pd.Series(['ajax',6],index=['key','lval']),ignore_index=True)
print left1