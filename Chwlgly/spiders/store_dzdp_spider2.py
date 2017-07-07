#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/6/12 下午6:31
# @Author  : 武明辉
# @File    : store_dzdp_spider2.py
import json
import random
import re

import scrapy

from Chwlgly.items import FoodStoreItem


class StoreDzdpSpider2(scrapy.Spider):
    name = 'store_dzdp2'
    start_urls = ['https://www.dianping.com/search/category/1/10', ]
    custom_settings = {
        'ITEM_PIPELINES': {'Chwlgly.pipelines.DropPipeline': 50,
                           'Chwlgly.pipelines.ListPageImagesPipeline': 200,
                           'Chwlgly.pipelines.CarouselFigurePiplines': 300,
                           'Chwlgly.pipelines.CarouselFigureTPiplines': 350,
                           'Chwlgly.pipelines.CarouselFigureSPiplines': 370,
                           'Chwlgly.pipelines.MongoPipeline': 400,
                           #'Chwlgly.pipelines.MysqlPipeline': 500,
                           },
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
        'IMAGES_STORE': 'images/store2/', 'DOWNLOADER_MIDDLEWARES': {'Chwlgly.middlewares.JavaScriptMiddleware': 900,
                                                                     'Chwlgly.middlewares.ProxytxtMiddleware': None,
                                                                     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, }, }

    def parse(self, response):

        urls = response.xpath('//div[@class="tit"]/a[1]/@href').extract()
        for url in urls:
            yield scrapy.Request(response.urljoin(url), self.parsedetail)

        next_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url).split('?')[0], self.parse)

    def parsedetail(self, response):
        """解析详情页"""
        item = FoodStoreItem()
        item['num'] = response.url.split('/')[-1]
        item['name'] = response.xpath('//h1[@class="shop-name"]/text()').extract_first()  # 标题
        item['comment_count'] = response.xpath('//span[@id="reviewCount"]/text()').re_first('\d+')  # 评论总数
        item['avg_price'] = response.xpath('//span[@id="avgPriceTitle"]/text()').re_first('\d+')  # 平均消费
        item['starnum'] = response.xpath('//span[contains(@class,"mid-rank-stars mid-str")]/@class').re_first('\d+')
        # item['loc_list'] = response.xpath  # 列表页位置
        item['tags'] = response.xpath('//span[@id="comment_score"]//span/text()').extract()
        if item['tags']:
            tags_l = []
            for tags in item['tags']:
                temp_dic = {}
                tag_k, tag_v = tags.encode('utf-8').split('：')
                if tag_k:
                    temp_dic[tag_k] = tag_v
                if temp_dic:
                    tags_l.append(temp_dic)
            item['tags'] = tags_l  # 列表页标签

        item['fullAddress'] = response.xpath('//div[@class="expand-info address"]/span[@class="item"]/text()').extract_first()  # 详细地址
        # item['description'] = response.xpath  # 描述
        item['tels'] = response.xpath('//span[@itemprop="tel"]/text()').extract_first()  # 电话

        # pd to get the lat and lng
        contentli = re.findall('window.shop_config=(.*?)</script>', response.body, re.S)
        item['lat'] = 0
        item['lng'] = 0
        try:
            content = contentli[0]
            temp = re.sub('(\w+):\s{0, 1}', '"\g<1>":', content)
            temp = re.sub('("http")', 'http', temp)
            temp = re.sub('("https")', 'http', temp)
            baseinfo = json.loads(temp)
            item['lat'] = baseinfo['shopGlat']
            item['lng'] = baseinfo['shopGlng']
            item['special'] = baseinfo['mainCategoryName']
        except:
            pass
        item['business_time'] = response.xpath(u'//p[@class="info info-indent"]/span[contains(text(),"营业时间")]/following-sibling::span/text()').extract_first()

        list_pics_temp = response.xpath('//div[@class="photo-carousel J_photo-carousel"]/ul/li/a/img/@src').extract()
        item['listpics_urls'] = [i.split('%')[0] for i in list_pics_temp]  # 这里是上面的小图
        # item['listpics'] = response.xpath  # 收集返回信息
        item['carouselfigures_urls'] = response.xpath('//div[@id="shop-tabs"]/div[2]/div/a/img/@src').extract()  # 餐厅环境

        food_tag = []
        for i in response.xpath('//p[@class="recommend-name"]/a'):
            k = i.xpath('./text()').extract_first()
            v = i.xpath('./em/text()').re_first('\d+')
            food_imgs = None
            food_price = 0
            if k:
                xp = '//div[@id="shop-tabs"]/div[1]/ul/li/p[contains(text(),"%s")]' % (k.strip())
                if response.xpath(xp).extract():
                    food_imgs = response.xpath(xp+'/preceding-sibling::img/@src').extract_first()
                    if food_imgs:
                        food_imgs = food_imgs.split('%')[0]
                    food_price = response.xpath(xp+'/following-sibling::span/text()').re_first('\d+')
                    if food_price:
                        food_price = float(food_price.strip())
            food_tag.append({'food_name': k, 'food_times': int(v),
                            'food_imgs': food_imgs, 'food_price': food_price})

        item['dishes'] = food_tag  # 菜品
        item['carouselfigures_urls2'] = []
        for dish in item['dishes']:
            if dish['food_imgs']:
                item['carouselfigures_urls2'].append(dish['food_imgs'])  # 返回食物的信息

        comment = {}
        comment_tag = response.xpath('//div[@id="comment"]/div[@id="summaryfilter-wrapper"]//div[@class="content"]/span/a/text()').extract()
        comment_tag_temp = []
        if comment_tag:
            for t in comment_tag:
                tag_name = t.split('(')[0]
                tag_weight = int(t.split('(')[1].split(')')[0])
                comment_tag_temp.append({'tag_name': tag_name, 'tag_weight': tag_weight})
        comment['tag'] = comment_tag_temp
        comment_temp = []
        carouselfigures_urls3 = []
        for it in response.xpath('//ul[@id="reviewlist-wrapper"]/li'):
            comment_main = {}
            comment_main['name'] = it.xpath('./p/a/text()').extract_first()
            comment_main['comment'] = it.xpath('./div[@class="content"]/div[contains(@class,"J-info-all")]/p/text()').extract_first()
            comment_main['star_num'] = it.xpath('./div[@class="content"]/p/span[1]/@class').re_first('\d+')
            if comment_main['star_num']:
                comment_main['star_num'] = int(comment_main['star_num'])
            tag = it.xpath('./div[@class="content"]/p/span[@class="item"]/text()').extract()
            tag_temp = []
            if tag:
                for t in tag:
                    k, v = t.encode('utf-8').split('：')
                    if k:
                        tag_temp.append({k: int(v)})

            comment_main['tags'] = tag_temp

            comment_main['urls'] = it.xpath('div[@class="content"]/div[@class="photos"]//a/img/@src').extract()
            carouselfigures_urls3.extend(comment_main['urls'])
            comment_temp.append(comment_main)
        item['carouselfigures_urls3'] = carouselfigures_urls3
        comment['main'] = comment_temp
        item['comment'] = comment  # 评论

        yield item
