# -*- coding: utf-8 -*-
"""
Created on Sun May 07 21:35:42 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
"""
normalsize 去除后面0:00:00
M:月份 W:星期 BM:最后一个工作日 4H:4个小时
"""
dd = pd.date_range('20170501',periods=10,normalsize=True,freq='4H')
print dd
"""
Period时期
period_range Q:季度
"""
print pd.Period(2010,freq='M')

pp = pd.period_range('2016-10',periods=10,freq='M')
print pp

pp1 = pd.period_range('2016-01','2016-04',freq='M')
print pp1

pp2 = pd.period_range('2016Q1',periods=4,freq='Q')
print pp2

pp3 = pd.Series(np.random.randint(0,50,60),index=pd.date_range('2016-04-01 09:30',periods=60))
print pp3


print pp3.resample('1d').sum()
"""
resample 重新取样
open high low close
"""
print pp3.resample('1d').ohlc()