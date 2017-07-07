#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/6/14 下午4:04
# @Author  : 武明辉
# @File    : mtom.py
import json

import MySQLdb
import pymongo

client = pymongo.MongoClient('mongodb://root:root@127.0.0.1:27017/myinfo')
collection = client['myinfo']['store3']
db = MySQLdb.connect('localhost', 'root', 'root', 'myinfo', charset="utf8")
cursor = db.cursor()

result = collection.find({})
for item in result:
    starnum = 0
    if item['starnum']:
        starnum = int(item['starnum'])

    avg_price = 0
    if item['avg_price']:
        avg_price = float(item['avg_price'])

    lng = 0
    lat = 0
    try:
        if item['lng']:
            lng = float(item['lng'])

        if item['lat']:
            lat = float(item['lat'])
    except:
        pass
    flavour = 0
    environment = 0
    service = 0
    try:
        if item['tags']:
            flavour = item['tags'][0].encode('utf-8').split('：')[1]
            environment = item['tags'][1].encode('utf-8').split('：')[1]
            service = item['tags'][2].encode('utf-8').split('：')[1]
    except:
        pass
    shop_imgs = None
    if item['listpics']:
        shop_img_temp = []
        for pic in item['listpics']:
            shop_img_temp.append(pic['path'].split('/')[1])
        shop_imgs = json.dumps(shop_img_temp)


    shop_environment_imgs = None
    if item['carouselfigures']:
        shop_environment_imgs_temp = []
        for pic in item['carouselfigures']:
            shop_environment_imgs_temp.append(pic['path'].split('/')[1])
        shop_environment_imgs = shop_environment_imgs_temp

    comment_tag = None
    if item['comment']['tag']:
        comment_tag_temp = []
        for i in item['comment']['tag']:
            dic_temp ={}
            key = i.split('(')[0]
            value = i.split('(')[1].split(')')[0]
            if key:
                dic_temp[key] = value
                comment_tag_temp.append(dic_temp)
        comment_tag = comment_tag_temp

    foods = item['dishes']
    path = []
    if item['carouselfigures2']:
        for i in item['carouselfigures2']:
            path.append(i['path'])
    if path:
        for i, food in enumerate(foods):
            try:
                food['food_imgs'] = path[i]
            except:
                food['food_imgs'] = path[0]

    comments = str(item['comment']['main'])

    cursor.execute('insert into store(dp_shop_id,country,province,county,shop_name,address,phone'
                           ',business_time,grade,avg_price,flavour,environment,service,lng,lat,'
                           'shop_imgs,shop_environment_imgs,comment_tag,foods,comments) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                  (item['num'], '中国', '上海市', '上海', item['name'], item['fullAddress'], item['tels'], item['business_time'],
                  starnum, avg_price, flavour, environment,service,lng,lat, shop_imgs,
                 json.dumps(shop_environment_imgs), json.dumps(comment_tag), json.dumps(foods), json.dumps(comments)))
    db.commit()

db.close()