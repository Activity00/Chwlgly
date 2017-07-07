#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/5/27 下午1:35
# @Author  : 武明辉
# @File    : food_slw_spider.py
import scrapy

from Chwlgly.items import SpecialFood


class Food_slw_spider(scrapy.Spider):
    name = 'food_slw'
    start_urls = ['http://www.shouliwang.com/search.html?keyword=厦门', ]
    custom_settings = {'ITEM_PIPELINES': {'Chwlgly.pipelines.DropPipeline': 10,
                                          'scrapy.pipelines.images.ImagesPipeline': 1,
                                          'Chwlgly.pipelines.MongoPipeline': 2,
                       },
                       'IMAGES_STORE': 'images/special_pic/'
                       }
    def parse(self, response):
        for li in response.xpath('//div[@class="productDetail"]//li'):
            item = SpecialFood()
            href = li.xpath('.//p[@class="fore1"]/a/@href').extract_first()
            item['name'] = li.xpath('.//p[@class="fore1"]/a/img/@alt').extract_first()
            item['price'] = li.xpath('.//p[@class="fore3"]/strong/text()').extract_first()
            star_url = li.xpath('.//p[@class="fore4"]/img/@src').extract_first()
            item['starnum'] = ''.join(star_url.split('/')[-1].split('.')[:2])
            item['comment_count'] = li.xpath('.//p[@class="fore4"]/a/span/text()').extract_first()
            item['listpics_urls'] = [li.xpath('.//li/p[@class="fore1"]/a/img/@src').extract_first()]
            meta = item
            yield scrapy.Request(response.urljoin(href), self.parsedetail, meta=meta)
        next_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), self.parse)


    def  parsedetail(self, response):
        item = response.meta
        item['num'] = response.url.split('/')[-1].split('.')[0]
        item['description'] = response.xpath('//div[@class="detailsRmaterial fr"]/div[@class="detailstitle clearfix"]/div//span/text()').extract_first()
        item['marketprice'] = response.xpath('//ul[@id="summary"]//div[@class="dd"]/span/b/text()').extract_first()
        item['outmonth'] = response.xpath('//li[@id="summary-market"]/div[@class="dd"]/text()').extract_first()
        headpic = response.xpath('//div[@id="productShow"]//li/a/@href').extract()
        content_pics = response.xpath('//div[contains(@class,"detail2015")]/p/img/@src').extract()
        headpic.append(content_pics)
        item['image_urls'] = self.reurllist(content_pics, response)
        yield item

    def reurllist(self, urls, response):
        temp = []
        for url in urls:
            if url.startswith('http'):
                temp.append(url)
            else:
                temp.append(response.urljoin(url))
        return temp