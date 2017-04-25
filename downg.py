# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

"""
scrapy 1.2.0
以下案例是抽取绿软家园软件对应的软链
//span[@class="app-name"]找到class为app-name的span标签下的a标签的href属性,@表示属性
getDetails是回调函数

"""
class DowngSpider(scrapy.Spider):
    name = "downg"
    allowed_domains = ["downg.com"]
    start_urls = (
        'http://www.downg.com/new/0_%s.html' % x for x in range(1,7)
    )

    def parse(self, response):
        urls = []
        sel = scrapy.Selector(response)
        url_list = sel.xpath('//span[@class="app-name"]/a/@href').extract()
        self.logger.info(url_list)
        print url_list
        for item in url_list:
            req = Request(item,callback=self.getDetails)
            urls.append(req)
        return urls
    
    def getDetails(self,response):
        print response.url
        #print ""