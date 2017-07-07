# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver


class ChwlglySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    '''auto change user-agent'''

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ProxytxtMiddleware(object):
    '''auto change ip'''

    def __init__(self):
        self.lins = open('ipn.txt', 'r').readlines()
        self.totalpage = len(self.lins)
        self.index = 0

    def dropvalidips(self):
        data = open('ipn.txt', 'r').readlines()
        with open('ipn.txt', 'w') as handle:
            handle.writelines(data[:self.index])
            handle.writelines(data[self.index + 1:])
            self.lins = handle.readlines()
            self.totalpage = len(self.lins)
        self.index = self.index - 1

    def process_request(self, request, spider):
        if not self.lins:
            return None
        proxy = self.lins[self.index]
        if self.index < self.totalpage - 1:
            self.index += 1
        else:
            self.index = 0
        if proxy is not None:
            request.meta['proxy'] = "http://%s" % proxy
            spider.logger.info('use:%s' % proxy)

    # def process_response(self, request, response, spider):
    #     if response.status != 200:
    #         if not self.lins:
    #             pass
    #         proxy = self.lins[self.index]
    #         if self.index < self.totalpage - 1:
    #             self.index += 1
    #         else:
    #             self.index = 0
    #         if proxy is not None:
    #             request.meta['proxy'] = "http://%s" % proxy
    #         return request

    def process_exception(self, request, exception, spider):
        proxy = None
        try:
            proxy = request.meta['proxy']
        except:
            pass
        if proxy in self.lins:
            self.lins.remove(proxy)
            self.totalpage -= 1
        self.process_request(request, spider)
        return request


class JavaScriptMiddleware(object):

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def process_request(self, request, spider):
        url = request.url
        if url.startswith('https://www.dianping.com') or url.startswith('http://www.dianping.com'):
            self.driver.get(url)
            time.sleep(3)
            js = "var q=document.documentElement.scrollTop=100"
            self.driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
            body = self.driver.page_source
            return HtmlResponse(url, encoding='utf-8', status=200, body=body)
            # return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        return None
