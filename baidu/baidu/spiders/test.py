# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response.css('title').extract_first())
        pass
