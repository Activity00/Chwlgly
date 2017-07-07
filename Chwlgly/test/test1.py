#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/5/24 下午3:52
# @Author  : 武明辉
# @File    : test1.py
import os

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config




# 需要填写你的 Access Key 和 Secret Key
access_key = 'EEe5gPomysw_ViIs462N43M-9Pdmm86REUgpsoqr'
secret_key = 'jCQvlfADza7apWs4V8Fi8eMmEhkb7oIHZ3DQBSce'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'wmh-test'
# 上传到七牛后保存的文件名
key = None
# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, None, 3000)
# 要上传文件的本地路径
for path in os.listdir('../../images/full'):
    localfile = '../../images/full/'+path
    ret, info = put_file(token, key, localfile)
    ret['key']

# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)