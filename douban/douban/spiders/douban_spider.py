# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-10 10:04:31
# @Last Modified by:   zengphil
# @Last Modified time: 2016-03-11 13:52:39

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.linkextractors import LinkExtractor


class DoubanSpider(CrawlSpider):
    """docstring for DoubanSpider"""
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "http://movie.douban.com/top250"
    ]
    rules=[
        Rule(LinkExtractor(allow=(r'\?start=\d+&filter='))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+/')),callback="parse_page"),
    ]


    # rules = (
    #     Rule(LinkExtractor(allow = (r'http://movie.douban.com/top250\?start=\d+&filter=&type=',))),
    #     Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback="parse_page", follow = True),
    #     )


    def parse_page(self, response):
        sel = Selector(response)
        item = DoubanItem()
        item['name'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
        item['desc'] = sel.xpath('//div/span[@property="v:summary"]/text()').extract()
        item['score'] = sel.xpath('//div/strong[@class="ll rating_num"]/text()').extract()
        item['number'] = sel.xpath('//div/span[@property="v:votes"]/text()')
        item['url'] = response.url
        return item





