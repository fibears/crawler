# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-09 20:18:32
# @Last Modified by:   zengphil
# @Last Modified time: 2016-03-09 20:18:52
import scrapy


class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]

    def parse(self, response):
        # We want to inspect one specific response.
        if ".org" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)

        # Rest of parsing code.
