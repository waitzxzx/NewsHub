# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from GetNews.items import SCUItem
import time
import datetime
from GetNews.settings import MYSQL_DATE_FORMAT
from scrapy.selector import Selector
import re
import jieba
class BangbingSpider(CrawlSpider):
    name = 'SCU'
    allowed_domains = ['scu.edu.cn']
    start_urls = ['http://www.scu.edu.cn/']
    #http://www.scu.edu.cn/info/1207/7849.htm
    rules = (
        Rule(LinkExtractor(allow=r'.*?/info/.*?htm'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i =  SCUItem()
        a = time.time()
        time_str = time.ctime(a)
        i['title'] = response.xpath("/html/body/div[1]/div[3]/form/div[1]/p[3]/text()").extract_first()
        i['time'] = response.xpath("/html/body/div[1]/div[3]/form/div[1]/p[5]/span[1]/text()").extract_first()
        data = response.xpath('//*[@id="vsb_content"]/div/p')
        info = data.xpath("string(.)").extract()
        i["content"] = info
        i["newsSource"] = "四川大学官网"
        i["newsCrawlTime"] = time_str
        return i
