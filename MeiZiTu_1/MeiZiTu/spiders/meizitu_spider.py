# -*- coding: utf-8 -*-
import scrapy
from MeiZiTu.items import MeizituItem
import re


class MeizituSpiderSpider(scrapy.Spider):
    name = 'meizitu_spider'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://meizitu.com/']
    count = 1
    pattern = re.compile(r'\d+')

    def parse(self, response):
        print '开始爬取： 第 %s 页' % self.count
        item = MeizituItem()
        # ImagePipeline要求['image_urls']字段必须是一个列表，就算只有一个url，也必须是一个列表，因此这里使用extract()而不是extract()[0]
        item['image_urls'] = response.xpath(
            '//div[@class="postContent"]//img/@src | //div[@class="pic"]//img/@src').extract()
        yield item
        print '结束爬取： 第 %s 页' % self.count

        max_page = response.xpath('//div[@id="wp_page_numbers"]/ul/li[last()]/a/@href').extract()[0]
        max_page = int(self.pattern.search(max_page).group(0))

        # 如果count小于最大页数，则继续往下爬取
        # 若不需要爬取完全部页数，可更改max_page
        if self.count < max_page:
            self.count += 1
            print 'go to next page seccess.'
            next_url = 'http://meizitu.com/a/more_' + str(self.count) + '.html'
            if self.count < max_page - 1:
                yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            print 'end.'
