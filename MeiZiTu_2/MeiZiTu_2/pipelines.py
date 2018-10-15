# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
from spiders import meizitu_spider2


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Meizitu2Pipeline(object):
    def process_item(self, item, spider):
        return item


class Meizitu2ImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # print "item['image_urls'] is %s" % item['image_urls']
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        image_path_name = request.meta['item']['images_folder_name']
        # 图片URL为： http://mm.chinasareview.com/wp-content/uploads/2018a/01/01/11.jpg
        # 故切片去[-18:-4]
        path = request.url[-18:-4].replace('/', '-').replace('a', '') + '.jpg'
        # path = image_path_name + '/' + request.url[-18:-4].replace('/', '-').replace('a', '') + '.jpg'
        print path + '--------------hello'
        return path

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['images_folder_name'] = image_path
        return item
