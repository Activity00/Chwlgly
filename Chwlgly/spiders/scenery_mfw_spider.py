#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/5/27 下午12:44
# @Author  : 武明辉
# @File    : scenery_mfw_spider.py
import json
import os
import re

import scrapy
import time

from scrapy import Selector
from scrapy.exceptions import IgnoreRequest
from selenium import webdriver

from Chwlgly.items import SceneryItem


class Scenery_mfw_soider(scrapy.Spider):
    name = 'scenery_mfw'
    custom_settings = {
        'ITEM_PIPELINES': {'Chwlgly.pipelines.DropPipeline': 50,
                           'scrapy.pipelines.images.ImagesPipeline': 200,
                           'Chwlgly.pipelines.MongoPipeline': 400, },
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
        'IMAGES_STORE': 'images/scenery_pic/',
        'DOWNLOADER_MIDDLEWARES': {'Chwlgly.middlewares.RandomUserAgent': None,
                                   'Chwlgly.middlewares.ProxytxtMiddleware': 900,
                                   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
                                  },
    }

    def start_requests(self):
        if os.path.exists('scenery_list_urls.txt'):
            urls = []
            with open('scenery_list_urls.txt', 'r') as f:
                for url in f.readlines():
                    urls.append(scrapy.Request(url=url.strip(), callback=self.parse, dont_filter=True))
            return urls
        browser = webdriver.Firefox()
        browser.get('http://www.mafengwo.cn/jd/10132/gonglve.html')
        time.sleep(5)
        selector = Selector(text=browser.page_source)
        links = selector.xpath('//ul[@class="scenic-list clearfix"]//a/@href').extract()
        urls = []
        url_by = []
        for link in links:
            req = scrapy.Request(url='http://www.mafengwo.cn%s'%link, callback=self.parse)
            urls.append(req)
            url_by.append('http://www.mafengwo.cn%s'%link)

        next = browser.find_element_by_xpath('//a[@class="pi pg-next"]')
        while next:
            browser.find_element_by_xpath('//a[@class="pi pg-next"]').click()
            time.sleep(2)
            selector = Selector(text=browser.page_source)
            links = selector.xpath('//ul[@class="scenic-list clearfix"]//a/@href').extract()
            for link in links:
                req = scrapy.Request(url='http://www.mafengwo.cn%s' % link,callback=self.parse)
                urls.append(req)
                url_by.append('http://www.mafengwo.cn%s' % link)
            try:
                next = browser.find_element_by_xpath('//a[@class="pi pg-next"]')
            except:
                next = None

        browser.quit()
        self.saveurlby(url_by)
        return urls

    def saveurlby(self, url_by):
        fl = open('scenery_list_urls.txt', 'w')
        for i in url_by:
            fl.write(i)
            fl.write("\n")
        fl.close()

    def parse(self, response):
        num = response.url.split('/')[-1].split('.')[0]
        item = SceneryItem()
        item['num'] = num
        item['description'] = response.xpath('//div[@class="summary"]/text()').extract_first()
        item['name'] = response.xpath('//div[@class="title"]/h1/text()').extract_first()
        item['tel'] = response.xpath('//li[@class="tel"]/div[@class="content"]/text()').extract_first()
        content = []
        for em in response.xpath('//div[@class="mod mod-detail"]/dl'):
            content_dic = {}
            k = em.xpath('.//dt/text()').extract_first()
            v = em.xpath('.//dd/text()').extract_first()
            if k is not None:
                content_dic[k] = v
                content.append(content_dic)
        item['content'] = content

        url_loc = 'http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiLocationApi?callback=&params={"poi_id":%s}'%num
        yield scrapy.Request(url_loc, self.getloc, meta=item)


    def getloc(self, response):
        poi = json.loads(response.body)['data']['controller_data']['poi']
        item = response.meta
        #item['lat'] = re.findall('"lat":(.*?),', response.body)[0]
        #item['lng'] = re.findall('"lng":(.*?),', response.body)[0]
        item['lat'] = poi['lat']
        item['lng'] = poi['lng']
        url_com = 'http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=&params={"poi_id":%s}' % item['num']
        yield scrapy.Request(url_com, self.getComment, meta=item)

    def getComment(self, response):
        item = response.meta
        try:
            commentj = json.loads(response.body)
        except:
            raise IgnoreRequest()
        comment_html = commentj['data']['html']
        selector = Selector(text=comment_html)
        temp_dic = {}
        tags = []
        for li in selector.xpath('//ul[@class="clearfix"]/li'):
            tag_dic = {}
            k = li.xpath('.//a/span[1]/text()').extract_first()
            v = li.xpath('.//a/span[@class="num"]/text()').extract_first()
            if k:
                tag_dic[k] = v
                tags.append(tag_dic)
        temp_dic['tags'] = tags

        comment_main = []
        for li in selector.xpath('//div[@class="rev-list"]//li'):
            head_icon_url = li.xpath('.//div[@class="user"]/a/img/@src').extract_first()
            nick_name = li.xpath('.//a[@class="name"]/text()').extract_first()
            star_num = 0
            try:
                star_num = re.search('[0-9]+([.]{1}[0-9]+){0,1}', li.xpath('.//span[contains(@class,"s-star")]/@class').extract_first()).group()
            except:
                pass
            content = li.xpath('.//p/text()').extract_first()
            comment_pics_url = li.xpath('.//div[@class="rev-img"]/a/@href').extract_first()
            if comment_pics_url:
                comment_pics_url = response.urljoin(comment_pics_url)

            last_time = li.xpath('.//span[@class="time"]/text()').extract_first()
            main_dic = {'head_icon_url': head_icon_url, 'star_num': star_num, 'nick_name': nick_name,
                        'content': content, 'comment_pics_url': comment_pics_url, 'last_time': last_time}
            comment_main.append(main_dic)
        temp_dic['main'] = comment_main
        item['comment'] = temp_dic
        url_onsale = 'http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiTicketsApi?callback=&params={"poi_id":%s}' % item['num']
        yield scrapy.Request(url_onsale, self.getOnSale, meta=item)

    def getOnSale(self, response):
        item = response.meta
        onsalej = json.loads(response.body)
        onsale_html = onsalej['data']['html']
        selector = Selector(text=onsale_html)
        onsale_list = []
        for tr in selector.xpath('//div[@class="mbd"]//tbody/tr'):
            onsale_dic = {}
            stype = tr.xpath('.//td[@class="type"]/text()').extract_first()
            description = tr.xpath('.//td[@class="pro"]/a/text()').extract_first()
            price = tr.xpath('.//td[@class="price"]/text()').extract_first()
            onsale_dic = {'type': stype, 'description': description, 'price': price}
            onsale_list.append(onsale_dic)
        item['onsale'] = onsale_list
        url_pic = 'http://www.mafengwo.cn/mdd/ajax_photolist.php?act=getPoiPhotoList&poiid=%s&page=1' % item['num']
        yield scrapy.Request(url_pic, self.getPics, meta=item)


    def getPics(self, response):
        item = response.meta
        image_urls = response.xpath('//li/a[1]/img/@src').extract()
        if image_urls:
            item['image_urls'] = image_urls
        yield item




