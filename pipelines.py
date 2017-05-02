# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import MySQLdb

#class FirstprojectPipeline(object):
#   # 该函数必须返回一个具有数据的dict或者item对象
#    def process_item(self, item, spider):
#        DBS = spider.settings.get('DBS')
#        con = MySQLdb.connect(**DBS)
#        # 下面这行代码表示设置MySQL使用的字符集为utf8
#        con.set_character_set('utf8')
#        cur = con.cursor()
#        insert_sql = (
#            "insert into proxy (ip, port, position, type, speed, last_check_time) "
#            "values (%s,%s,%s,%s,%s,%s);"
#        )
#        values = (item['ip'], item['port'], item['position'], item['type'], item['speed'], item['last_check_time'])
#        # 插入数据库
#        try:
#            cur.execute(insert_sql, values)
#        except Exception, e:
#            print "插入失败: ", e
#            con.rollback()
#        else:
#            con.commit()
#        cur.close()
#        con.close()
#        return item
#
#
#
#
#        return item
    
import urllib2
import os
 
class PicPipeline(object):
    def process_item(self, item, spider):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        req = urllib2.Request(url=item['addr'],headers=headers)
        res = urllib2.urlopen(req)
        file_name = os.path.join(r'D:\my',item['name']+'.jpg')
        with open(file_name,'wb') as fp:
            fp.write(res.read())


#class MoviePipeline(object):
#     def process_item(self, item, spider):
#        with open("D:\\my\\my_meiju.txt",'a') as fp:
#            fp.write(item['iname'].encode('utf-8') + '\n')