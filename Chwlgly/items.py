# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class HotelItem(scrapy.Item):
    ''' hotel_dzdp '''
    num = scrapy.Field()  # 唯一 num
    name = scrapy.Field()  # 名字
    listpics_urls = scrapy.Field()  # 这里是4个小图
    listpics = scrapy.Field()  # 收集返回信息
    carouselfigures_urls = scrapy.Field()  # 内容页面6个图
    carouselfigures = scrapy.Field()  # 返回图片的信息
    price = scrapy.Field()  # 价格
    image_urls = scrapy.Field()  # 内容页图片链接信息
    images = scrapy.Field()  # 图片存储信息
    list_tags = scrapy.Field()  # 标签tags
    loc_listpage = scrapy.Field()  # the location info in listpage
    star_num = scrapy.Field()  # 星星的数量
    remark_num = scrapy.Field()  # 评论数量
    lat = scrapy.Field()  # 坐标
    lng = scrapy.Field()  # 坐标
    score = scrapy.Field()  # 分数
    tel = scrapy.Field()  # 电话
    type = scrapy.Field()  # 酒店类型 eg:婚宴
    fullAdress = scrapy.Field()  # 地址
    hotelinfo = scrapy.Field()  # 酒店信息 opentime:开业时间 checkintime:退房时间 facilities
    comment = scrapy.Field()  # 评论
    goods_info = scrapy.Field()  # 货物信息


class FoodStoreItem(scrapy.Item):
    ''' FoodStore_dzdp '''
    num = scrapy.Field()  # 惟一值
    name = scrapy.Field()  # 标题
    comment_count = scrapy.Field()  # 评论总数
    avg_price = scrapy.Field()  # 平均消费
    starnum = scrapy.Field()
    business_time = scrapy.Field()  # 营业时间
    special = scrapy.Field()  # 特色
    loc_list = scrapy.Field()  # 列表页位置
    tags = scrapy.Field()  # 列表页标签
    listpics_urls = scrapy.Field()  # 这里是1个小图
    listpics = scrapy.Field()  # 收集返回信息

    fullAddress = scrapy.Field()  # 详细地址
    description = scrapy.Field()  # 描述
    tels = scrapy.Field()  # 电话
    lng = scrapy.Field()
    lat = scrapy.Field()
    dishes = scrapy.Field()  # 菜品
    carouselfigures_urls = scrapy.Field()  # 内容页面6个图
    carouselfigures = scrapy.Field()  # 返回图片的信息
    carouselfigures_urls2 = scrapy.Field()  # 餐厅图片
    carouselfigures2 = scrapy.Field()   #
    carouselfigures_urls3 = scrapy.Field()  # 评论图片
    carouselfigures3 = scrapy.Field()  #
    comment = scrapy.Field()  # 评论
    meta = scrapy.Field()  # 临时属性


class SceneryItem(scrapy.Item):
    '''mfw'''
    num = scrapy.Field()  # id
    name = scrapy.Field()  # 标题
    description = scrapy.Field()  # 描述
    tel = scrapy.Field()  # 电话
    content = scrapy.Field()  # 内容包括开业时间交通门票等
    lat = scrapy.Field()
    lng = scrapy.Field()
    comment = scrapy.Field()
    onsale = scrapy.Field()
    image_urls = scrapy.Field()  # 图片链接信息
    images = scrapy.Field()  # 图片存储信息


class SpecialFood(scrapy.Item):
    '''手礼网'''
    num = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    starnum = scrapy.Field()
    comment_count = scrapy.Field()
    description = scrapy.Field()
    marketprice = scrapy.Field()
    outmonth = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    listpics_urls = scrapy.Field()  # 这里是1个小图
    listpics = scrapy.Field()  # 收集返回信息
