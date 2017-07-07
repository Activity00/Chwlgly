#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/5/24 下午3:33
# @Author  : 武明辉
# @File    : store_dzdp_spider.py
import json
import re

import scrapy
from scrapy.exceptions import IgnoreRequest

from Chwlgly.items import FoodStoreItem


class StoreDzdpSpider(scrapy.Spider):
    name = 'store_dzdp'
    start_urls = ['http://www.dianping.com/search/category/15/10/g0r0', ]
    custom_settings = {
        'ITEM_PIPELINES': {'Chwlgly.pipelines.DropPipeline': 50,
                           'Chwlgly.pipelines.ListPageImagesPipeline': 200,
                           'Chwlgly.pipelines.CarouselFigurePiplines': 300,
                           'Chwlgly.pipelines.MongoPipeline': 400, },
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
        'DOWNLOADER_MIDDLEWARES': {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, },
    }

    def start_requests(self):
        requests = []
        for i in range(2, 51):
            url = 'http://www.dianping.com/search/category/15/10/g0r0/p%s' % i
            requests.append(scrapy.Request(url, callback=self.parse))
        return requests

    def parse(self, response):
        for li in response.xpath('//div[@id="shop-all-list"]//li'):
            item = FoodStoreItem()
            item['name'] = li.xpath('.//div[@class="tit"]//a/@title').extract_first()
            item['avg_price'] = int(li.xpath('.//div[@class="comment"]/a[@class="mean-price"]/b/text()').re_first('\d+'))
            item['comment_count'] = int(li.xpath('.//div[@class="comment"]/a[@class="review-num"]/b/text()').extract_first())
            item['starnum'] = int(li.xpath('.//div[@class="comment"]/span/@class').re_first('\d+'))
            threetupe = li.xpath('.//div[@class="tag-addr"]//span/text()').extract()
            item['special'] = threetupe[0]
            item['loc_list'] = threetupe[1]
            item['fullAddress'] =threetupe[2]

            tag_texts = li.xpath('.//span[@class="comment-list"]/span/text()').extract()
            tag_nums = li.xpath('.//span[@class="comment-list"]/span/b/text()').extract()
            tags = []
            for em in zip(tag_texts, tag_nums):
                dic_temp = {}
                dic_temp['name'] = em[0]
                dic_temp['num'] = em[1]
                tags.append(dic_temp)
            item['tags'] = tags
            item['listpics_urls'] = li.xpath('./div[@class="pic"]/a/img/@data-src').extract()
            url = li.xpath('.//div[@class="tit"]/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(url), self.parsedetail, meta=item)

        # next_url = response.xpath('//a[@class="next"]/@href').extract_first()
        # if next_url:
        #     yield scrapy.Request(response.urljoin(next_url).split('?')[0], self.parse)

    '''
     window.shop_config={
        userId: 0,
        shopId: 23540221,
        shopCityId: 15,
        shopName: "堂宴老厦门私房菜",
        address: "湖光路夏商沿街店面95号",
        publicTransit: "",
        cityId: 15,
        cityCnName: "厦门",
        cityName: "厦门",
        cityEnName: "xiamen",
        isOverseasCity: 0,
        fullName: "堂宴老厦门私房菜(火车站店)",
        shopGlat: "24.477908",
        shopGlng:"118.109903",
        cityGlat:"24.479615",
        cityGlng:"118.08939",
        power:5,
        shopPower:45,
        voteTotal:0,
        district:0,
        shopType:10,
        mainRegionId:1836,
        mainCategoryName:"海鲜",
        categoryURLName:"food",
        shopGroupId: 10329803,
        categoryName: "美食",
        loadUserDomain:"http://www.dianping.com",
        map:{
            power:5,
        manaScore:0
        },    mainCategoryId:251,
     defaultPic:"https://img.meituan.net/msmerchant/69d63076ac8f6afc55b0fb5346b612271324894.jpg%40120w_90h_1e_1c_1l_80q%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
    }
    '''

    def parsedetail(self, response):
        contentli = re.findall('window.shop_config=(.*?)</script>', response.body, re.S)
        if not contentli:
            print 'ignore request iiiiiiii'
            raise IgnoreRequest()
        item = response.meta
        content = contentli[0]
        temp = re.sub('(\w+):\s{0,1}', '"\g<1>":', content)
        temp = re.sub('("http")', 'http', temp)
        temp = re.sub('("https")', 'http', temp)
        baseinfo = json.loads(temp)
        item['num'] = response.url.split('/')[-1]
        item['lat'] = baseinfo['shopGlat']
        item['lng'] = baseinfo['shopGlng']
        item['dp_shop_id'] = item['num']

        meta = {}
        meta['shopId'] = response.url.split('/')[-1]
        meta['shopName'] = re.findall(r'shopName: "(.*?)",', content)[0].strip()
        meta['cityId'] = re.findall(r'cityId:(.*?),', content)[0].strip()
        meta['power'] = re.findall(r'power:(.*?),', content)[0].strip()
        meta['shopType'] = re.findall(r'shopType:(.*?),', content)[0].strip()
        meta['shopCityId'] = re.findall(r'shopCityId:(.*?),', content)[0].strip()
        meta['mainCategoryId'] = re.findall(r'mainCategoryId:(.*?),', content)[0].strip()
        meta['mainCategoryName'] = re.findall(r'mainCategoryName:"(.*?)",', content)[0].strip()

        url = 'http://www.dianping.com/ajax/json/shopDynamic/shopTabs?shopId=%s&cityId=%s&shopName=%s&power=%s&mainCategoryId=%s&shopType=%s&shopCityId=%s' % (
            meta['shopId'], meta['cityId'], meta['shopName'], meta['power'], meta['mainCategoryId'], meta['shopType'],
            meta['shopCityId'])
        item['meta'] = meta
        print 'bbb', item
        yield scrapy.Request(url, self.getDishes, meta=item)

    def getDishes(self, response):
        item = response.meta
        meta = item['meta']
        content = json.loads(response.body)
        item['description'] = content['briefStory']
        item['dishes'] = content['dishesWithPicVO']
        item['carouselfigures_urls'] = [x['defaultPicURL'] for x in item['dishes']]
        url = 'http://www.dianping.com/ajax/json/shopDynamic/allReview?shopId=%s&cityId=%s&categoryURLName=food&power=%s&cityEnName=xiamen&shopType=%s' % (
            meta['shopId'], meta['cityId'], meta['power'], meta['shopType'])
        print 'ccc', item
        yield scrapy.Request(url, callback=self.getComment, meta=item)

    def getComment(self, response):
        item = response.meta
        content = json.loads(response.body)
        item['comment'] = content['reviewDataList']
        print 'ddd', item
        yield item
















