# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from GetNews.items import SCU_JWCItem
import time
import re
import jieba
from GetNews.settings import MYSQL_DATE_FORMAT
from scrapy.selector import Selector
class BangbingSpider(CrawlSpider):
    name = 'JWC'
    allowed_domains = ['scu.edu.cn']
    start_urls = ['http://jwc.scu.edu.cn']
    #http://www.scu.edu.cn/info/1207/7849.htm
    rules = (
        Rule(LinkExtractor(allow=r'.*?/detail/.*?htm'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i =  SCU_JWCItem()
        a = time.time()
        time_str = time.ctime(a)
        i['title'] = response.xpath("/html/body/div[@id='serach_div']/div[@class='list-a-content']/h3[@class='page-title']/text()").extract()[0]
        news_time = response.xpath("/html/body/div[@id='serach_div']/div[@class='list-a-content']/p[@class='page-date']/span[1]/text()").extract()[0]
        news_time = news_time.strip()
        i["time"] = news_time
        data = response.xpath("/html/body/div[@id='serach_div']/div[@class='list-a-content']/div[@class='page-content']/p")
        info = data.xpath("string(.)").extract()
        info_new = [str(j) for j in info]
        info_res = ''.join(info_new)
        i["content"] = info_res
        seg = jieba.cut(info_res, cut_all=False)
        seg_list = '/'.join(seg)
        test1 = ".*?/(?:停课|放假|考试安排|选课)/*?"  # 教学
        test2 = ".*?/(?:晚会|社团|青春广场)/*?"  # 活动
        test3 = ".*?/(?:大赛|竞赛|选拔)/*?"  # 竞赛
        test4 = ".*?/(?:科研成果|论文|SCI|影响因子)/*?"  # 科研
        test5 = ".*?/(?:讲座|科学家|院士)/*?"  # 学术
        test6 = ".*?/(?:留学|出国|交换生|护照|签证|联合培养|港澳台)/*?"  # 国际
        test7 = ".*?/(?:就业|实习生|公司)/*?"  # 就业
        if (re.match(test1, seg_list, flags=0)):
            i["newsLabel"] = 1
        elif (re.match(test2, seg_list, flags=0)):
            i["newsLabel"] = 2
        elif (re.match(test3, seg_list, flags=0)):
            i["newsLabel"] = 3
        elif (re.match(test4, seg_list, flags=0)):
            i["newsLabel"] = 4
        elif (re.match(test5, seg_list, flags=0)):
            i["newsLabel"] = 5
        elif (re.match(test6, seg_list, flags=0)):
            i["newsLabel"] = 6
        else:
            i["newsLabel"] = 7
        i["newsSource"] = "四川大学教务处"
        i["newsCrawlTime"] = time_str
        return i
