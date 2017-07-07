#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/5/20 下午12:03
# @Author  : 武明辉
# @File    : hotel_dzdp_spider.py
import json
import re
import scrapy
from scrapy.exceptions import IgnoreRequest
from Chwlgly.items import HotelItem


class Hotel_dzdp_spider(scrapy.Spider):
    ''' hotel info in dzdp '''
    name = 'hotel_dzdp'
    start_urls = ['https://www.dianping.com/xiamen/hotel', ]
    custom_settings = {'ITEM_PIPELINES': {'Chwlgly.pipelines.DropPipeline': 50,
                                          'Chwlgly.pipelines.ListPageImagesPipeline': 200,
                                          'Chwlgly.pipelines.CarouselFigurePiplines': 300,
                                          'Chwlgly.pipelines.MongoPipeline': 400, },
                       'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
                       }

    def parse(self, response):
        '''function:
            1.get basic info in list page and retrieval all the pages
            2.pass on the basicinfo and request the main content page
        '''
        info_lists = response.xpath('//ul[@class="hotelshop-list"]/li')
        for info in info_lists:
            item = HotelItem()
            item['name'] = info.xpath('.//div[@class="hotel-info-main"]/h2/a/text()').extract_first()
            item['price'] = info.xpath('.//div[@class="hotel-remark"]/div[@class="price"]/strong/text()').re_first('\d+')
            item['list_tags'] = info.xpath('.//p[@class="hotel-tags"]/span/text()').extract()
            # this time listpics_urls more than one in list page
            item['listpics_urls'] = info.xpath('.//ul[@class="J_hotel-pics"]/li/a/img/@data-lazyload').extract()
            item['loc_listpage'] = info.xpath('.//p[@class="place"]/a/text()').extract_first()
            item['star_num'] = info.xpath('.//div[@class="remark"]//span/@class').re_first('\d+')
            item['remark_num'] = info.xpath('.//div[@class="remark"]//a/text()').re_first('\d+')
            url = info.xpath('.//div[@class="hotel-info-main"]/h2/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(url), callback=self.parsedetail, meta=item)

        next_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

    def parsedetail(self, response):

        item = response.meta  # get the basic info from list page
        item['num'] = response.url.split('/')[-1]
        infos = None
        try:
            infos = json.loads(re.findall('window.__INITIAL_STATE__ = (.*?);', response.body)[0])
        except:
            raise IgnoreRequest()

        basicInfo = infos['basicInfo']
        hotelinfo = infos['hotelIntro']
        userComment = infos['userComment']
        item['score'] = basicInfo['score']
        item['lat'] = basicInfo['lat']
        item['lng'] = basicInfo['lng']
        item['tel'] = basicInfo['phoneNo']
        item['type'] = basicInfo['refShopTypeStr']
        item['fullAdress'] = basicInfo['fullAdress']
        # images
        item['carouselfigures_urls'] = [url['picUrl'] for url in infos['picInfo']['headPic']]
        item['hotelinfo'] = hotelinfo

        # comemtn
        comment_dic = {}
        comment_dic['reviewCountAll'] = userComment['reviewCountAll']
        comment_dic['reviewDataList'] = userComment['reviewDataList']
        item['comment'] = comment_dic

        goods_url = ''

        yield scrapy.Request('http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=%s' % item['num'],
                             callback=self.getGoodsInfo, meta=item)
        
    def getGoodsInfo(self, response):
        ''' get goods info '''
        item = response.meta
        dataj = json.loads(response.body)
        item['goods_info'] = dataj['data']['hotelGoodsList']['roomList']
        yield item