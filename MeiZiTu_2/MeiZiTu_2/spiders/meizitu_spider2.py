# -*- coding: utf-8 -*-
import scrapy
import re
from MeiZiTu_2.items import Meizitu2Item
from scrapy import Request


class MeizituSpider2Spider(scrapy.Spider):
    name = 'meizitu_spider2'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://meizitu.com/a/more_1.html']
    count = 1
    # 使用正则提取url数字页码
    pattern = re.compile(r'\d+')

    def parse(self, response):
        item = Meizitu2Item()
        print '开始爬取： 第 %s 页' % self.count


        # # 高清大图的URL
        # for i in range(len(response.xpath('//h3[@class="tit"]//a/@href').extract())):
        #     images_hd_url = response.xpath('//h3[@class="tit"]//a/@href').extract()[i]
        #     print "images_hd_url is %s\n" % images_hd_url
        #     item['images_folder_name'] = \
        #         response.xpath('//h3[@class="tit"]//b/text() | //h3[@class="tit"]/a/text()').extract()[0]
        #     request = scrapy.Request(url=images_hd_url, callback=self.parse_img, )
        #     request.meta['item'] = item
        #     yield request

        # 测试时只爬取前五个
        for i in response.xpath('//h3[@class="tit"]')[0:5]:
            # print i.xpath('./a/@href').extract()[0]
            images_hd_url = i.xpath('./a/@href').extract()[0]
            print "images_hd_url is %s\n" % images_hd_url
            item['images_folder_name'] = i.xpath('./a/b/text() | ./a/text()').extract()[0]
            print "images_folder_name is %s\n" % item['images_folder_name']
            request = scrapy.Request(url=images_hd_url, callback=self.parse_img)
            request.meta['item'] = item
            yield request

        try:
            max_page = response.xpath('//div[@id="wp_page_numbers"]/ul/li[last()]/a/@href').extract()[0]
            max_page = int(self.pattern.search(max_page).group(0))

            # 如果count小于最大页数，则继续往下爬取
            # 若不需要爬取完全部页数，可更改此处max_page
            # 测试时只爬取前5页
            if self.count < 5:
                self.count += 1
                print 'go to next page success.'
                next_url = 'http://meizitu.com/a/more_' + str(self.count) + '.html'
                yield scrapy.Request(url=next_url, callback=self.parse)
            else:
                print 'normal end.'
        except Exception as e:
            print 'spider end.'


    def parse_img(self, response):
        item = response.meta['item']
        item['image_urls'] = response.xpath('//div[@id="picture"]//img/@src').extract()
        print '结束爬取： 第 %s 页' % self.count
        yield item
