# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-10 10:04:31
# @Last Modified by:   fibears
# @Last Modified time: 2016-03-14 22:33:09

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.linkextractors import LinkExtractor

import re

class DoubanSpider(CrawlSpider):
    """docstring for DoubanSpider"""
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "http://movie.douban.com/top250"
    ]
    rules=[
        Rule(LinkExtractor(allow=('\?start=\d+&filter=')), follow = True),
        # Rule(LinkExtractor(allow=(r'http://www.imdb.com/title/\w+')),
        #     callback="parse_imdb"),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+/')),callback="parse_douban"),
    ]


    def parse_douban(self, response):
        sel = Selector(response)
        item = DoubanItem()

        item['rank'] = sel.xpath('//div/span[@class="top250-no"]/text()').re(r'No.(\d+)')[0]
        item['name'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()[0]
        item['director'] = sel.xpath('//span[@class="attrs"]/a[@rel="v:directedBy"]/text()').extract()[0]
        item['doubanscore'] = sel.xpath('//div/strong[@class="ll rating_num"]/text()').extract()[0]
        item['people'] = sel.xpath('//span[@property="v:votes"]/text()').extract()[0]
        item['description'] = sel.xpath('//span[@property="v:summary"]/text()').extract()[0]
        yield item

    # def parse_imdb(self, response):

    #     sel = Selector(response)
    #     item = DoubanItem()
    #     item['imdbscore'] = sel.xpath('//div/strong/span[@itemprop="ratingValue"]/text()').extract()
    #     return item




