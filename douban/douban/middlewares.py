# -*- coding: utf-8 -*-
# @Author: fibears
# @Date:   2016-03-14 19:04:21
# @Last Modified by:   fibears
# @Last Modified time: 2016-03-14 21:22:23

import random

from agents import AGENTS


class UserAgentMiddlewares(object):
    """docstring for UserAgentMiddlewares"""
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent
        request.headers['Host']='movie.douban.com'


