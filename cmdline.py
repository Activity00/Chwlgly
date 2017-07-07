# -*- coding: utf-8 -*-
# @Time    : 17/4/24 下午5:52
# @Author  : 武明辉
# @File    : cmdline.py

import scrapy.cmdline

if __name__ == '__main__':
    # scrapy.cmdline.execute(['scrapy', 'crawl', 'store_dzdp2'])
    scrapy.cmdline.execute('scrapy crawl store_dzdp2 -o store2.json'.split())
    # scrapy.cmdline.execute('scrapy crawl hotel_dzdp -o hotel.json'.split())
    # scrapy.cmdline.execute('scrapy crawl food_slw -o foods.json'.split())
    # scrapy.cmdline.execute('scrapy crawl scenery_mfw -o scenery.json'.split())
    # scrapy.cmdline.execute('scrapy crawl scenery_mfw2 -o scenery2.json'.split())