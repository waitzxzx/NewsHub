# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from GetNews.items import SCUItem
import time
from GetNews.settings import MYSQL_DATE_FORMAT
from scrapy.selector import Selector
class BangbingSpider(CrawlSpider):
    name = 'bangbing'
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
        i['title'] = response.xpath("/html/body/div[@class='news-content']/div[@class='main']/form/div[@class='contentContainer']/p[@class='title']/text()").extract()[0]
        i['time'] = response.xpath("/html/body/div[@class='news-content']/div[@class='main']/form/div[@class='contentContainer']/p[@class='info']/span[@class='s1'][1]/text()").extract()[0]
        data = response.xpath("/html/body/div[@class='news-content']/div[@class='main']/form/div[@class='contentContainer']/div[@id='vsb_content']/div[@class='v_news_content']/p")
        info = data.xpath("string(.)").extract()
        i["content"] = info
        i["newsSource"] = "四川大学官网"
        i["newsCrawlTime"] = time_str
        return i
