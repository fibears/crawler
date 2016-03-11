#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-10 11:29:20
# @Last Modified by:   zengphil
# @Last Modified time: 2016-03-10 11:34:23
import json

def readMovieJson():
    inFile = open("result.json",'r',0)
    text = inFile.read() # text是str
    movie_dict = json.loads(text) # movie_dict是list
    for movie in movie_dict: # movie是dict
        rank = movie["rank"][0] # rank等都是Unicode
        title = movie["title"][0]
        link = movie["link"][0]
        rate = movie["rate"][0]
        if movie["quote"]:
            quote = movie["quote"][0]
        else: quote = "暂无".decode("utf-8")

        # str和Unicode不能混用，要么将Unicode类型encode为其他编码。要么将str类型decode为其他编码
        # python的内部使用Unicode，str如“电影： ”是字节串，由Unicode经过编码(encode)后的字节组成的
        # 下句等价于 print "电影: " + title.encode("utf-8") + " 链接: " + link.encode("utf=8")
        print "top".decode("utf-8") + rank + ".".decode("utf-8") + title + " 评分".decode("utf-8") +  '('.decode("utf-8") + rate + ')'.decode("utf-8") + "\n链接：".decode("utf-8") + link +  "\n豆瓣评论：".decode("utf-8") + quote + "\n"

readMovieJson()
