#coding=utf-8
import time,datetime,calendar
import random
'''
输出时间戳
'''
print time.time()
'''
不规则的时间格式
'''
print time.localtime(time.time())
'''
格式化成2016-03-20 11:45:39形式
'''
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

'''
timedelta时间间隔
'''
print (datetime.datetime(2017,3,27) + datetime.timedelta(days = 1)).date()
print (datetime.datetime(2017,3,27) + datetime.timedelta(days = 1)).time()

dt = datetime.datetime(2017,3,27)
print dt.timetuple()
'''
分段详细输出结果
'''
for item in dt.timetuple():
    print item

'''
输出日历
'''
print calendar.month(2017,1)




"""
输出10-20之间的随机数
下面这个5是递增的基数 即返回2+5n
random.random()返回0-1之间的随机数
"""
print random.randrange(2,20,5)
print  random.randint(10,20)
print random.random()


