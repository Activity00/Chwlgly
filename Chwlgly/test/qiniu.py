#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/6/14 上午11:24
# @Author  : 武明辉
# @File    : qiniu.py
def qiniufetch(url,bucket,filename):
    """调用七牛的fetch API 将url的图片存储到七牛"""
    from base64 import urlsafe_b64encode as b64e
    from qiniu.auth import digest
    access_key = "EEe5gPomysw_ViIs462N43M-9Pdmm86REUgpsoqr"
    secret_key = "jCQvlfADza7apWs4V8Fi8eMmEhkb7oIHZ3DQBSce"

    encoded_url = b64e(url)
    dest_entry = "%s:%s" % (bucket, filename)
    encoded_entry = b64e(dest_entry.encode('utf-8'))
    api_host = "iovip.qbox.me"
    api_path = "/fetch/%s/to/%s" % (encoded_url, encoded_entry)

    mac = digest.Mac(access=access_key, secret=secret_key)
    client = digest.Client(host=api_host, mac=mac)

    ret, err = client.call(path=api_path)
    if err is not None:
        print "Fetch image file\"%s\" failed" % url
        print err
        return None
    else:
        print "Fetch \"%s\" to qiniu \"%s\" success!" % (url,dest_entry)
        return "http://%s.qiniudn.com/%s" % (bucket, urllib.quote(filename.encode('utf-8')))

url = 'http://qcloud.dpfile.com/pc/eqgCg0yc6cjlaq2PiNL_GhfRELSBYXcyIkqqvI2aioLRYGyP8AybpPZbV1VuhnXgF5u7J_jS4MuCaeLAHD0KTg.jpg'
print qiniufetch(url,'wmh-test',None)