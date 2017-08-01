# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:52:52 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
"""
股票：收益 波动情况
adj除权后价格
resample对数据进行重新采样
(最高价-最低价)/最低价是波动幅度
mean求平均值
plot 画图很容易看出股票的波动幅度
(最高价-最低价)/最低价 

read_csv('',header=3)跳过头三行
"""
df = pd.read_csv('yahoo-data/002001.csv',index_col='Date',parse_dates=True)
adj_price = df['Adj Close']
readj_price = adj_price.resample('m').ohlc()
#print readj_price
ripple = (readj_price.high - readj_price.low)/readj_price.low
#print ripple.mean()
#print adj_price.plot(figsize=(8,6))
print (adj_price.max() - adj_price.min())/adj_price.min()
#上市时买入，一直到现在卖出，增长的倍数
total_growth = adj_price.ix[0]/adj_price.ix[-1]
#最开始的年 结束的年
print adj_price.index[-1],adj_price.index[0]
print adj_price.index[-1].year,adj_price.index[0].year
#每年的增加率，开平方
print total_growth ** (1.0/(adj_price.index[0].year-adj_price.index[-1].year))
#to_period('A')年  groupby(level=0)以索引分组
price_in_year = adj_price.to_period('A').groupby(level=0).first()
#图形展示
#print price_in_year.plot(figsize=(8,6))
#diff
diff = price_in_year.diff()
print diff
#计算每一年的增长率
rate = diff/(price_in_year-diff)
print rate
#柱状图
print rate.plot(kind='bar')
