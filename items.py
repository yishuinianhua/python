# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#class FirstprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    ip = scrapy.Field()
#    port = scrapy.Field()
#    position = scrapy.Field()
#    type = scrapy.Field()
#    speed = scrapy.Field()
#    last_check_time = scrapy.Field()
    
#校花网    
class PicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    addr = scrapy.Field()
    name = scrapy.Field()

#抓取最新的美剧   
#class MovieItem(scrapy.Item):
#    iname = scrapy.Field()