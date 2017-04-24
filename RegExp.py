#coding=utf-8
import re
'''
match 尝试从字符串的起始位置匹配一个模式
python 的None等价于java NULL
'''
print re.match("zhongj1","zhongj1huarenmingonghezhong1guo").span()

print re.match("zhongj1","zhongj1huarenmingonghezhong1guo").groups()

'''
re.search 扫描整个字符串并返回第一个成功的匹配。
'''
print re.compile("zhong1guo").search("111zhonghuarenmingonghezhong1guo")

print re.search("\w","zhonghuarenmingonghezhongguo")

print re.compile("[a-zA-Z]").findall("yishipeng1990@163.com")
'''
search 若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，只返回第一个。
span返回第一个匹配的位置
findall 返回string中所有与pattern相匹配的全部字串，返回形式为数组。
group()返回结果

'''
list01 = re.compile("\wajax").findall("1_ajaxjavapython2pajax0013aajax")
search01 = re.compile("(\w)(\S)").search("1_ajaxjavapython2pajax0013+ajax")
print len(list01)
print search01.span()
print search01.group()
print list01

#----------------------------------------------------------------------------------
print r'\n'
print '\n'

'''
python里的原生字符串很好地解决了这个问题，这个例子中的正则表达式可以使用r”\\”表示。同样，匹配一个数字的”\\d”可以写成r”\d”。
有了原生字符串，妈妈也不用担心是不是漏写了反斜杠，写出来的表达式也更直观勒。

'''

"""
group(n) 这个1-n是以括号为分界的，group(0)会输出整体,group(1)输出第一个匹配的括号的内容
group(2) 输出第二个匹配括号的内容

"""

a = "123abc456"
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456
for item in range(1,5):
    print re.compile(r'^Port(.*)(\d{4,5})(.*)\ (\d+\.\d+\.\d+\.\d+)').search('Port 8009 is unreachable on 172.25.172.59').group(item)

