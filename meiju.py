# -*- coding: utf-8 -*-
#import scrapy
#from firstproject.items import MovieItem
# 
#class MeijuSpider(scrapy.Spider):
#    name = "meiju"
#    allowed_domains = ["meijutt.com"]
#    start_urls = ['http://www.meijutt.com/new100.html']
#    
#    
#    def parse(self, response):
#        
#        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
#        for each_movie in movies:
#            item = MovieItem()
#            #这个返回的是list，所以需要list[0]返回值
#            print each_movie.xpath('./h5/a/@title').extract()[0]
#            item['iname'] = each_movie.xpath('./h5/a/@title').extract()[0]
#            yield item
#            
#        
