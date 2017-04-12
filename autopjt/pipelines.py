# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json


class AutopjtPipeline(object):
    def __init__(self):
        # 打开 mydata.json 文件
        self.file = codecs.open("mydata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        # i = json.dumps(dict(item), ensure_ascii=False)
        # # 每条数据后加上换行符
        # line = i + '\n'
        # # 数据写入到 mydata.json 文件中
        # self.file.write(line)
        for j in range(0, len((item["name"]))):
            name = item["name"][j]
            price = item["price"][j]
            link = item["link"][j]
            comments = item["comments"][j]
            goods = {"name": name, "price":price, "comnum": comments, "link": link}
            i = json.dumps(dict(goods), ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)
        return item
    def close_spider(self, spider):
        # 关闭 mydata.json 文件
        self.file.close()