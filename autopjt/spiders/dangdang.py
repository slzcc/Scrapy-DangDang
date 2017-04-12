# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request

class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://category.dangdang.com/pg1-cid4002203.html']

    def parse(self, response):
        item=AutopjtItem()
        # 通过各 XPath 表达式分别听取商品的名称、价格、连接、评论数等信息
        item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        item["comments"]=response.xpath("//a[@name='P_pl']/text()").extract()
        # 提取完后返回 item
        yield item
        # 接下来通过自动爬取 75 页的数据
        for i in range(1, 76):
            url="http://category.dangdang.com/pg"+str(i)+"-cid4002203.html"
            yield Request(url, callback=self.parse)
