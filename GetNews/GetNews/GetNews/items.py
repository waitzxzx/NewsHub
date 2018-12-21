# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SCUItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    newsSource = scrapy.Field()
    newsCrawlTime = scrapy.Field()
    newsLabel = scrapy.Field()

class SCU_JWCItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    newsSource = scrapy.Field()
    newsCrawlTime = scrapy.Field()
    newsLabel = scrapy.Field()

class SCU_CSItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    newsSource = scrapy.Field()
    newsCrawlTime = scrapy.Field()
    newsLabel = scrapy.Field()



