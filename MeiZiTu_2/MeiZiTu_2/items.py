# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Meizitu2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 存放文件夹的名字
    images_folder_name = scrapy.Field()
    # 存放图片URL
    image_urls = scrapy.Field()
    images = scrapy.Field()
