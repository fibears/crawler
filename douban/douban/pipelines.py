# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pony.orm import db_session

from scrapy.utils.project import get_project_settings

from douban.models import db
from douban.models import DoubanEntity

settings = get_project_settings()

class DoubanPipeline(object):

    def __init__(self):
        db.bind('mysql', **settings.get('SQLDB'))
        db.generate_mapping()

    def process_item(self, item, spider):

        with db_session:

            doubanEntity = DoubanEntity(
                rank = item['rank'],
                name = item['name'],
                director = item['director'],
                doubanscore = item['doubanscore'],
                # imdbscore = item['imdbscore'],
                people = item['people'],
                description = item['description']

                )

            print('save post')

    def spider_close(self, spider):
        db.disconnect()










