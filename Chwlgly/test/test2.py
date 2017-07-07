#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/6/13 下午4:46
# @Author  : 武明辉
# @File    : test2.py
import urllib2

url = 'http://p0.meituan.net/dpmerchantalbum/5f24f1711ebb5df63b7e6bebf6f314dd7086633.jpg%40280w_212h_1e_1c_1l%7Cwatermark%3D0'
f = urllib2.urlopen(url)
fil = open('test.jpg', 'wb')
fil.write(f.read())
fil.flush()
fil.close()