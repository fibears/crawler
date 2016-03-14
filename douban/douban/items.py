# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    name = scrapy.Field()
    director = scrapy.Field()
    doubanscore = scrapy.Field()
    # imdbscore = scrapy.Field()
    people = scrapy.Field()
    description = scrapy.Field()

