#coding=utf-8
import json
#from urllib2 import urlopen
'''
dumps 将 Python 对象编码成 JSON 字符串
loads 将已编码的 JSON 字符串解码为 Python 对象
'''
stringJson = "{'zhangsan':{'name':'zhangsan','age':20,'school':'Tsinghua'}}"
json01 = json.dumps(stringJson)
"""
json格式不能直接json[key],字典是可以的dict[key]
如果调用第三方接口，获取的是json格式的数据，必须loads转换为字典才能调用key
"""
#
#print json01['zhangsan']
# print type(json01)
#
jsonData = '{"language":"python","age":20}'
text = json.loads(jsonData)
print type(text)
print text['age']
#jsonResult = urlopen("http://172.25.201.58/validate?username=kaifa&password=kaifa").read()
'''
调用接口后获得的数据是json格式的
loads 将已编码的 JSON 字符串解码为 Python 对象

'''
#print json.loads(jsonResult)["status"]
#print jsonResult
#print type(jsonResult)