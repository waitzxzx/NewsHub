# -*- coding: utf-8 -*-

import pymysql

class GetnewsPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="120.79.22.44", user="root", passwd="123456", db="newshub",charset='utf8')
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        title = item["title"]
        time = item["time"]
        content = item["content"]
        newsSource = item["newsSource"]
        newsCrawlTime = item["newsCrawlTime"]
        newsLabel = item["newsLabel"]
        sql = "insert into news(newsContent, newsTitle, newstime,newsSource, newsCrawlTime, newsLabel) values(%s, %s, %s, %s, %s, %s)"
        self.cur.execute(sql, (content, title, time, newsSource, newsCrawlTime, newsLabel))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
