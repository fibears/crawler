# -*- coding: utf-8 -*-
# @Author: fibears
# @Date:   2016-03-14 19:04:07
# @Last Modified by:   fibears
# @Last Modified time: 2016-03-14 22:23:28

from pony.orm import *

db = Database()


class DoubanEntity(db.Entity):
    """docstring for DoubanEntity"""

    _table_ = 'douban'

    id = PrimaryKey(int, size = 64, unsigned = True, auto = True)

    rank = Optional(int)
    name = Optional(unicode)
    director = Optional(unicode)
    doubanscore = Optional(float)
    # imdbscore = Optional(float)
    people = Optional(float)

    description = Optional(LongUnicode)



