#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/6/13 下午5:01
# @Author  : 武明辉
# @File    : utils.py

import os
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config


class UploadToQiniu(object):
    '''根据文件名上传七牛并且返回key'''

    def __init__(self, access_key, secret_key, bucket_name='wmh-test', filename=None, seconds=3000):
        '''
        
        :param access_key: ...
        :param secret_key: ...
        :param bucket_name: ...
        :param filename: ... key 用于固定文件名
        :param seconds:  过期时间
        '''
        q = Auth(access_key, secret_key)
        # 要上传的空间
        self.bucket_name = bucket_name
        # 上传到七牛后保存的文件名
        self.key = filename
        # 生成上传 Token，可以指定过期时间等
        self.token = q.upload_token(bucket_name, self.key, 3000)
        # 要上传文件的本地路径

    def upload(self,filepath):
        ret, info = put_file(self.token, self.key, filepath)
        return ret['key']


import pymongo
from pymongo import MongoClient

class Mmm(object):

    def __init__(self):
        client = MongoClient('mongodb://root:root@127.0.0.1:27017/myinfo')
        db = client.myinfo
        self.store = db.store2

    def main(self):
        result = self.store.find({})
        for ret in result:
            self.logc(ret)

    def logc(self, ret):
        num = ret['num']
        listpics_urls = ret['listpics_urls']
        carouselfigures_urls = ret['carouselfigures_urls']
        #print listpics_urls
        print carouselfigures_urls


# m = Mmm()
# m.main()
access_key = 'EEe5gPomysw_ViIs462N43M-9Pdmm86REUgpsoqr'
secret_key = 'jCQvlfADza7apWs4V8Fi8eMmEhkb7oIHZ3DQBSce'
bucket_name = 'wmh-test'
up = UploadToQiniu(access_key, secret_key, bucket_name)
print up.upload('../../images/store2/full/0a3fc7edecbbd50bb9aaf44e6d7eda66f13379f5.jpg')

# for path in os.listdir('../../images/full'):
#     localfile = '../../images/full/'+path
#     hash = up.upload(localfile)
#     print hash
