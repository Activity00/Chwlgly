# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import pymongo
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from Chwlgly.items import FoodStoreItem, HotelItem


class ListPageImagesPipeline(ImagesPipeline):
    '''like android ListView usually have one picture in left 
        the other side is some info about description...
        but sometimes there are more than one pic ,so called 
        ListPageImagesPipline
    '''
    pass
    # def get_media_requests(self, item, info):
    #     super(ListPageImagesPipeline, self).get_media_requests(item, info)
    # def item_completed(self, results, item, info):
    #     super(ListPageImagesPipeline, self).item_completed(results, item, info)

class CarouselFigurePiplines(ImagesPipeline):
    ''' sometimes it like ListPageImagesPipeline,just is for 
        Carousel figure in contentn page.
    '''
    pass
    # def get_media_requests(self, item, info):
    #     super(CarouselFigurePiplines, self).get_media_requests(item, info)
    # def item_completed(self, results, item, info):
    #     super(CarouselFigurePiplines, self).item_completed(results, item, info)
class CarouselFigureTPiplines(ImagesPipeline):
    ''' sometimes it like ListPageImagesPipeline,just is for 
        Carousel figure in contentn page.
    '''
    pass
    # def get_media_requests(self, item, info):
    #     super(CarouselFigurePiplines, self).get_media_requests(item, info)
    # def item_completed(self, results, item, info):
    #     super(CarouselFigurePiplines, self).item_completed(results, item, info)

class CarouselFigureSPiplines(ImagesPipeline):
    ''' sometimes it like ListPageImagesPipeline,just is for 
        Carousel figure in contentn page.
    '''
    pass
    # def get_media_requests(self, item, info):
    #     super(CarouselFigurePiplines, self).get_media_requests(item, info)
    # def item_completed(self, results, item, info):
    #     super(CarouselFigurePiplines, self).item_completed(results, item, info)

class DropPipeline():
    ''' hotel drop item '''
    def process_item(self, item, spider):
        if not item['num'] or not item['name']:
            raise DropItem('drop a valid item: have no num or name')
        return item


class MongoPipeline():
    ''' hotel_pipeline 
    '''

    collection_hotel = 'hotel_last'
    collection_store = 'store'
    collection_foods = 'foods_last'
    collection_scenery = 'scenery_last'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
                   mongo_db=crawler.settings.get('MONGO_DATABASE', 'myinfo'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
        spider.logger.info('insert all data compelte')

    def process_item(self, item, spider):
        if spider.name == 'store_dzdp':
            cur = self.db[self.collection_store].find_one({'num': item['num']})
            if not cur:
                spider.logger.info('insert one new item')
                self.db[self.collection_store].insert(item)
            else:
                pass  # ???这里应该更新需要更新的信息
            return item
        elif spider.name == 'store_dzdp2':
            cur = self.db[self.collection_store].find_one({'num': item['num']})
            if not cur:
                num = int(item['num'])
                business_time = item['business_time']
                grade = 0
                if item['starnum']:
                    grade = int(item['starnum'])
                avg_price = 0
                if item['avg_price']:
                    avg_price = float(item['avg_price'])
                flavour = 0
                environment = 0
                service = 0
                if item['tags']:
                    flavour = item['tags'][0].values()[0]
                    environment = item['tags'][1].values()[0]
                    service = item['tags'][2].values()[0]

                lng = float(item['lng'])
                lat = float(item['lat'])

                shop_imgs = None
                listpics = item['listpics']
                if listpics:
                    shop_imgs = ['https://qiniu.yhimg.net/'+x['path'].split('/')[1] for x in listpics]

                shop_environment_imgs = None
                carouselfigures = item['carouselfigures']
                if carouselfigures:
                    shop_environment_imgs = ['https://qiniu.yhimg.net/'+x['path'].split('/')[1] for x in carouselfigures]

                comment_tag = item['comment']['tag']  # tag_name tag_weight

                foods = None    # food_name food_times food_imgs food_price
                dishes = item['dishes']
                carouselfigures2 = item['carouselfigures2']
                if dishes:
                    foods = []
                    for i, dish in enumerate(dishes):
                        dish['food_imgs'] = 'https://qiniu.yhimg.net/' + carouselfigures2[i]['path'].split('/')[1]
                        foods.append(dish)

                comments = None  # comment_name comment_content comment_grade
                # comment_flavour comment_environment comment_service comment_imgs
                try:
                    main = item['comment']['main']
                    comments = []

                    carouselfigures3 = {}
                    if item['carouselfigures3']:
                        for c in item['carouselfigures3']:
                            k, v = c['url'], c['path']
                            if k:
                                carouselfigures3[k] = v

                    for m in main:
                        comment_name = m['name']
                        comment_content = m['comment']
                        comment_grade = m['star_num']
                        comment_flavour = m['tags'][0].values()[0]
                        comment_environment = m['tags'][1].values()[0]
                        comment_service = m['tags'][2].values()[0]
                        url_temp = []
                        for url in m['urls']:
                            if url in carouselfigures3:
                                url_temp.append('https://qiniu.yhimg.net/'+carouselfigures3['url'].split('/')[1])
                        comment_imgs = url_temp
                        comments.append({'comment_name': comment_name, 'comment_content': comment_content,
                                         'comment_grade': comment_grade, 'comment_flavour': comment_flavour,
                                         'comment_environment': comment_environment, 'comment_service': comment_service,
                                         'comment_imgs': comment_imgs})

                except Exception as e:
                    print '没有到这里吧'
                    spider.logger.error(e)

                inserted = {'dp_shop_id': num, 'country': '中国', 'province': None,
                            'city': '上海市', 'county': None, 'shop_name': item['name'],
                            'address': item['fullAddress'], 'phone': item['tels'],
                            'business_time': business_time, 'grade': grade, 'avg_price': avg_price,
                            'flavour': flavour, 'environment': environment, 'service': service,
                            'lng': lng, 'lat': lat, 'shop_imgs': shop_imgs, 'shop_environment_imgs':shop_environment_imgs,
                            'comment_tag': comment_tag, 'foods': foods, 'comments': comments}

                spider.logger.info('insert one new item')
                self.db[self.collection_store].insert(inserted)
            else:
                pass  # ???这里应该更新需要更新的信息
            return item
        elif spider.name == 'hotel_dzdp':
            cur = self.db[self.collection_hotel].find_one({'num': item['num']})
            if not cur:
                spider.logger.info('insert one new item')
                self.db[self.collection_hotel].insert(item)
            else:
                pass  # ???这里应该更新需要更新的信息
            return item
        elif spider.name == 'food_slw':
            cur = self.db[self.collection_foods].find_one({'num': item['num']})
            if not cur:
                spider.logger.info('insert one new item')
                self.db[self.collection_foods].insert(item)
            else:
                pass  # ???这里应该更新需要更新的信息
            return item
        elif spider.name == 'scenery_mfw':
            cur = self.db[self.collection_scenery].find_one({'num': item['num']})
            if not cur:
                spider.logger.info('insert one new item')
                self.db[self.collection_scenery].insert(item)
            else:
                pass  # ???这里应该更新需要更新的信息
            return item


# class  MysqlPipeline():
#     """ 写如mysql下载管道"""
#
#     def __init__(self, db_uri, db_name, username, password):
#         self.db_uri = db_uri
#         self.db_name = db_name
#         self.username = username
#         self.password = password
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(db_uri='localhost', db_name='myinfo',
#                    username='root', password='root')
#     def open_spider(self, spider):
#         self.db = MySQLdb.connect(self.db_uri, self.username, self.password, self.db_name, charset="utf8")
#
#     def close_spider(self, spider):
#         self.db.close()
#
#     def process_item(self, item, spider):
#         cursor = self.db.cursor()
#         try:
#             flavour = 0
#             environment = 0
#             service = 0
#             try:
#                 flavour = float(item['tags'][0].encode('utf-8').split('：')[1])
#                 environment = float(item['tags'][1].encode('utf-8').split('：')[1])
#                 service = float(item['tags'][2].encode('utf-8').split('：')[1])
#             except:
#                 pass
#             shop_imgs =
#             shop_environment_imgs =
#             comment_tag =
#             foods =
#             comments =
#             cursor.execute('insert into store(db_shop_id,country,province,county,shop_name,address,phone'
#                            ',business_time,grade,avg_price,flavour,environment,service,lng,lat,'
#                            'shop_imgs,shop_environment_imgs,comment_tag,foods,comments) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
#                 (item['num'], '中国', '上海市', '上海', item['name'], item['fullAddress'], item['tels'], item['business_time'],
#                  int(item['starnum']), float(item['avg_price']),flavour, environment,service,float(item['lng']),float(item['lat']), shop_imgs,
#                  shop_environment_imgs,comment_tag,foods,comments))
#             self.db.commit()
#             return item
#         except Exception as e:
#             print '数据库存储错误', e
#             self.db.rollback()
#             return item


import json
import logging
import sys

from scrapy.http import Response, Request
from scrapy.pipelines.files import FilesPipeline
from twisted.internet import threads
from qiniu import Auth, BucketManager
from scrapy.exceptions import NotConfigured

__author__ = 'zephyre'


class QiniuFilesStore(object):
    def get_access_key(self):
        return self._access_key

    def get_secret_key(self):
        return self._secret_key

    def get_bucket_mgr(self):
        if not self._bucket_mgr:
            ak = self.access_key
            sk = self.secret_key
            q = Auth(ak, sk)
            self._bucket_mgr = BucketManager(q)

        return self._bucket_mgr

    bucket_mgr = property(get_bucket_mgr)

    access_key = property(get_access_key)

    secret_key = property(get_secret_key)

    def __init__(self, settings):
        self.settings = settings

        # 获得access key和secret key
        self._access_key = settings.get('PIPELINE_QINIU_AK')
        self._secret_key = settings.get('PIPELINE_QINIU_SK')
        if not self._access_key or not self._secret_key:
            logging.getLogger('scrapy').error('PIPELINE_QINIU_AK or PIPELINE_QINIU_SK not specified.')
            raise NotConfigured

        self._bucket_mgr = None

    def get_file_stat(self, bucket, key):
        stat, error = self.bucket_mgr.stat(bucket, key)
        return stat

    def stat_file(self, path, info):
        def _onsuccess(stat):
            if stat:
                checksum = stat['hash']
                timestamp = stat['putTime'] / 10000000
                return {'checksum': checksum, 'last_modified': timestamp}
            else:
                return {}

        info = json.loads(path)
        return threads.deferToThread(self.get_file_stat, info['bucket'], info['key']).addCallback(_onsuccess)

    def persist_file(self, path, buf, info, meta=None, headers=None):
        """
        因为我们采用七牛的fetch模型，所以，当request返回的时候，图像已经上传到了七牛服务器
        """
        pass

    def fetch_file(self, url, key, bucket):
        if not bucket:
            logging.error('No bucket specified')
            raise IOError
        if not key:
            logging.error('No key specified')
            raise IOError

        ret, error = self.bucket_mgr.fetch(url, bucket, key)
        if ret:
            return ret
        else:
            raise IOError


class QiniuPipeline(FilesPipeline):
    """
    https://github.com/haizi-zh/scrapy-qiniu
    设置项：
    * PIPELINE_QINIU_ENABLED: 是否启用本pipeline
    * PIPELINE_QINIU_BUCKET: 存放在哪个bucket中
    * PIPELINE_QINIU_KEY_PREFIX: 资源在七牛中的key的名称为：prefix + hash(request.url)
    * QINIU_KEY_GENERATOR_FEILD: generator: 给定一个url, 如何获得资源在七牛中的bucket和key.
      该参数指明item中的哪个字段用来表示generator
    """
    MEDIA_NAME = "file"
    DEFAULT_FILES_URLS_FIELD = 'file_urls'
    DEFAULT_FILES_RESULT_FIELD = 'files'
    DEFAULT_QINIU_KEY_GENERATOR_FIELD = 'qiniu_key_generator'

    def __init__(self, settings=None):
        """
        初始化
        :param settings:
        :return:
        """
        # 存放到哪个bucket中
        bucket = settings.get('PIPELINE_QINIU_BUCKET')
        if not bucket:
            logging.getLogger('scrapy').warning('PIPELINE_QINIU_BUCKET not specified')
            raise NotConfigured
        self.bucket = bucket
        self.store = QiniuFilesStore(settings)

        self.key_prefix = (settings.get('PIPELINE_QINIU_KEY_PREFIX') or '').strip()
        if not self.key_prefix:
            logging.getLogger('scrapy').error('PIPELINE_QINIU_KEY_PREFIX not specified')
            raise NotConfigured

        super(FilesPipeline, self).__init__(download_func=self.fetch)

    def _extract_key_info(self, request):
        """
        从欲下载资源的request中, 获得资源上传七牛时的bucket和key
        """
        from scrapy.utils.request import request_fingerprint

        key_generator = request.meta.get('qiniu_key_generator')
        if key_generator:
            tmp = key_generator(request.url)
            bucket = tmp['bucket'] or self.bucket
            key = tmp['key']
        else:
            bucket = self.bucket
            key = '%s%s' % (self.key_prefix, request_fingerprint(request))

        return {'bucket': bucket, 'key': key}

    def fetch(self, request, spider):
        """download_func"""
        info = self._extract_key_info(request)

        ret = self.store.fetch_file(request.url, info['key'], info['bucket'])
        return Response(request.url, body=json.dumps(ret))

    def get_media_requests(self, item, info):
        """
        根据item中的信息, 构造出需要下载的静态资源的Request对象
        :param item:
        :param info:
        :return:
        """
        key_generator = item.get(self.QINIU_KEY_GENERATOR_FIELD)
        return [Request(x, meta={'qiniu_key_generator': key_generator}) for x in item.get(self.FILES_URLS_FIELD, [])]

    @classmethod
    def from_settings(cls, settings):
        if not settings.getbool('PIPELINE_QINIU_ENABLED', False):
            raise NotConfigured
        cls.FILES_URLS_FIELD = settings.get('FILES_URLS_FIELD', cls.DEFAULT_FILES_URLS_FIELD)
        cls.FILES_RESULT_FIELD = settings.get('FILES_RESULT_FIELD', cls.DEFAULT_FILES_RESULT_FIELD)
        cls.QINIU_KEY_GENERATOR_FIELD = settings.get('QINIU_KEY_GENERATOR_FIELD', cls.DEFAULT_QINIU_KEY_GENERATOR_FIELD)
        cls.EXPIRES = settings.getint('FILES_EXPIRES', sys.maxint)

        return cls(settings=settings)

    def file_path(self, request, response=None, info=None):
        """
        抓取到的资源存放到七牛的时候, 应该采用什么样的key? 返回的path是一个JSON字符串, 其中有bucket和key的信息
        """
        return json.dumps(self._extract_key_info(request))

    def file_downloaded(self, response, request, info):
        return json.loads(response.body)['hash']

    def item_completed(self, results, item, info):
        def process_result(result):
            data = json.loads(result['path'])
            result['bucket'] = data['bucket']
            result['key'] = data['key']
            return result

        if isinstance(item, dict) or self.FILES_RESULT_FIELD in item.fields:
            item[self.FILES_RESULT_FIELD] = [process_result(x) for ok, x in results if ok]
        return item



