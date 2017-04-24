#coding=utf-8
import MySQLdb
sql="SELECT * FROM user"
try:
    try:
        i = 1/0
    except ArithmeticError,e:
        print e

    '''
    python连接mysql时指定字符集utf8
    抽取的结果是元组
    '''

    conn = MySQLdb.connect(host="172.25.201.58",user="root",passwd="XXXXXX",db="mybatis",charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    for line in [item[1] for item in cur.fetchall()]:
        print line
    print "发生异常根本就不会执行该语句"
except BaseException,e:
    print e
else:
    print "没有发生异常"