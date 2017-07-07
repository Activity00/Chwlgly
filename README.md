# 吃喝玩乐鼓浪屿数据爬取

## 酒店信息
**信息来源:**
大众点评<br>
[列表页](https://www.dianping.com/xiamen/hotel)
[内容页](http://www.dianping.com/newhotel/2325856)


field | type | description
---|---|---
name | string | hotel name
num | string | id for recognize this hotel
listpics | list | 列表页的图片列表信息<br>－path list(string) 本地路径；<br>－url list(string)真实链接
carouselfigures | list | 内容页图片信息
price | string |  hotel的起步价
list_tags | list | 列表页tags
loc_listpage | string | 列表页的地理位置
star_num | string  | 星星的数量
remark_num | string | 评论数量
lat | string | 坐标纬度
lng | string | 纬度
score | string |分数
tel | string | 电话
type | string | 酒店类型 eg:婚宴
fullAdress | string | 详细地址
hotelinfo | object |酒店信息<br>opentime string:开业时间<br> checkintime string:退房时间 <br>facilities list:基础设施eg：［'残疾人中心','商务中心'...］<br>roomFacilities list:房间设施 eg：［'电话'，'写字台'...］<br>services list(string):eg:['叫醒'，'洗衣服']<br>checkInTime string:住房提醒
comment | object |评论<br>reviewCountAll <string>:总评论数量；reviewDataList<list>:eg:见下json1（复制到格式化工具查看）
goods_info | object | 货物信息 见表

**comemnt下reviewDataList－json1**
```
{"reviewDataList": [
            {
                "reviewData": {
                    "userId": 43133438,
                    "shopId": 2325856,
                    "reviewId": 348630048,
                    "picTotal": 6,
                    "lastTime": "2017-05-19 18:36",
                    "addTime": "2017-05-19 18:36",
                    "followNoteNo": 0,
                    "reviewBody": "很幸运在这住了两天，来厦门第一天住的别的酒店，进门就霉味特别重，实在住不惯，幸好厦门宾馆还有房间，下了出租车就有人帮着拿行李，办入住时说只能住两天，五六日早已全部预定出去（在厦门大多数酒店周末房价都比平时贵），进了房间干净舒适，一点霉味潮湿的感觉也没有，我是北方人感觉很舒服，服务特别棒，我老公生日还给送手写的贺卡、蛋糕、菊花茶，还有自助早餐种类特别多，孩子也特别喜欢。两天过后我们换了另一家酒店，我无奈的说跟第一家差不多，在厦门只推荐厦门宾馆",
                    "reviewBodyLength": 222,
                    "star": {
                        "desc": "非常好",
                        "title": "总体评价",
                        "value": 50
                    },
                    "flowerTotal": 0,
                    "scoreList": null,
                    "expenseInfoList": [
                        {
                            "desc": "元",
                            "title": "费用",
                            "value": 0
                        }
                    ],
                    "extInfoList": null
                },
                "reviewFollowNoteDTO": null,
                "userPic": [
                    {
                        "orderNo": 0,
                        "status": 1,
                        "height": 700,
                        "width": 525,
                        "userId": 43133438,
                        "cityId": 15,
                        "title": "",
                        "url": "http://qcloud.dpfile.com/pc/vnYgnb6HHgLSWTc20vtr5nejTIyIR8r_WBYbD1rQereGwq2aDeX9hkBkULrF2prDQs6E6HQccbzhvkqkRN4krQ.jpg",
                        "clientType": 2,
                        "shopId": 2325856,
                        "shopType": 60,
                        "bigPicture": "http://qcloud.dpfile.com/pc/vnYgnb6HHgLSWTc20vtr5nejTIyIR8r_WBYbD1rQerdh1BiHYpf6wl7vuyL1SHKnCUldaiupJgKYTSfIaRn8IQ.jpg",
                        "lastTime": 1495190160000,
                        "addTime": 1495190160000,
                        "followNoteNo": 0,
                        "price": 0,
                        "shopGroupId": 2325856,
                        "hits": 0,
                        "lastIp": "183.250.0.214",
                        "statusCode": 0,
                        "picId": 770381713,
                        "picType": 0,
                        "picPower": 0,
                        "isTop": false,
                        "rank": 0,
                        "middlePicture": "http://qcloud.dpfile.com/pc/vnYgnb6HHgLSWTc20vtr5nejTIyIR8r_WBYbD1rQerdD-Ejailh_Vk04bSSbCDM_05mDabRMXcC-NnPom6wedQ.jpg",
                        "smallPicture": "http://qcloud.dpfile.com/pc/vnYgnb6HHgLSWTc20vtr5nejTIyIR8r_WBYbD1rQereNT9V2B1mbU5XXuzTXPq9k3dWYFEM5hoslgWXTJDjSPA.jpg",
                        "clientTypeName": "iPhone",
                        "rateGoodTotal": 0,
                        "picPrice": 0,
                        "picPowerTitle": "",
                        "tags": null
                    },
                    {
                        "orderNo": 0,
                        "status": 1,
                        "height": 700,
                        "width": 525,
                        "userId": 43133438,
                        "cityId": 15,
                        "title": "",
                        "url": "http://qcloud.dpfile.com/pc/Bc_dVDkLZcHIjyjVdI6HuVbcfmtrQIssRVonoGxS9LFJ3bR4RueesKH27sNRwe5oQs6E6HQccbzhvkqkRN4krQ.jpg",
                        "clientType": 2,
                        "shopId": 2325856,
                        "shopType": 60,
                        "bigPicture": "http://qcloud.dpfile.com/pc/Bc_dVDkLZcHIjyjVdI6HuVbcfmtrQIssRVonoGxS9LEg4TtDXRFkkZxqkhMQfYR5CUldaiupJgKYTSfIaRn8IQ.jpg",
                        "lastTime": 1495190160000,
                        "addTime": 1495190160000,
                        "followNoteNo": 0,
                        "price": 0,
                        "shopGroupId": 2325856,
                        "hits": 0,
                        "lastIp": "183.250.0.214",
                        "statusCode": 0,
                        "picId": 770381712,
                        "picType": 0,
                        "picPower": 0,
                        "isTop": false,
                        "rank": 0,
                        "middlePicture": "http://qcloud.dpfile.com/pc/Bc_dVDkLZcHIjyjVdI6HuVbcfmtrQIssRVonoGxS9LEnQRHBxSiRxl1W9pnkrto_05mDabRMXcC-NnPom6wedQ.jpg",
                        "smallPicture": "http://qcloud.dpfile.com/pc/Bc_dVDkLZcHIjyjVdI6HuVbcfmtrQIssRVonoGxS9LGExPwWvOOL0cVtGD7MmpsM3dWYFEM5hoslgWXTJDjSPA.jpg",
                        "clientTypeName": "iPhone",
                        "rateGoodTotal": 0,
                        "picPrice": 0,
                        "picPowerTitle": "",
                        "tags": null
                    },
                    {
                        "orderNo": 0,
                        "status": 1,
                        "height": 700,
                        "width": 525,
                        "userId": 43133438,
                        "cityId": 15,
                        "title": "",
                        "url": "http://qcloud.dpfile.com/pc/qtn8T7GEqyRFwJYxNpRXxg9v_kwP5CFXA62BeTOhO71J3bR4RueesKH27sNRwe5oQs6E6HQccbzhvkqkRN4krQ.jpg",
                        "clientType": 2,
                        "shopId": 2325856,
                        "shopType": 60,
                        "bigPicture": "http://qcloud.dpfile.com/pc/qtn8T7GEqyRFwJYxNpRXxg9v_kwP5CFXA62BeTOhO70g4TtDXRFkkZxqkhMQfYR5CUldaiupJgKYTSfIaRn8IQ.jpg",
                        "lastTime": 1495190160000,
                        "addTime": 1495190160000,
                        "followNoteNo": 0,
                        "price": 0,
                        "shopGroupId": 2325856,
                        "hits": 0,
                        "lastIp": "183.250.0.214",
                        "statusCode": 0,
                        "picId": 770381711,
                        "picType": 0,
                        "picPower": 0,
                        "isTop": false,
                        "rank": 0,
                        "middlePicture": "http://qcloud.dpfile.com/pc/qtn8T7GEqyRFwJYxNpRXxg9v_kwP5CFXA62BeTOhO70nQRHBxSiRxl1W9pnkrto_05mDabRMXcC-NnPom6wedQ.jpg",
                        "smallPicture": "http://qcloud.dpfile.com/pc/qtn8T7GEqyRFwJYxNpRXxg9v_kwP5CFXA62BeTOhO72ExPwWvOOL0cVtGD7MmpsM3dWYFEM5hoslgWXTJDjSPA.jpg",
                        "clientTypeName": "iPhone",
                        "rateGoodTotal": 0,
                        "picPrice": 0,
                        "picPowerTitle": "",
                        "tags": null
                    },
                    {
                        "orderNo": 0,
                        "status": 1,
                        "height": 700,
                        "width": 525,
                        "userId": 43133438,
                        "cityId": 15,
                        "title": "",
                        "url": "http://qcloud.dpfile.com/pc/WCZZ41YmGo_0Fi1DYLvwj5XQuEhPDf-gUBs21SyFed1PJn2_hVfIqxZER5y0YCq3Qs6E6HQccbzhvkqkRN4krQ.jpg",
                        "clientType": 2,
                        "shopId": 2325856,
                        "shopType": 60,
                        "bigPicture": "http://qcloud.dpfile.com/pc/WCZZ41YmGo_0Fi1DYLvwj5XQuEhPDf-gUBs21SyFed2l3GY7xKdKcM9hmxs7unpgCUldaiupJgKYTSfIaRn8IQ.jpg",
                        "lastTime": 1495190160000,
                        "addTime": 1495190160000,
                        "followNoteNo": 0,
                        "price": 0,
                        "shopGroupId": 2325856,
                        "hits": 0,
                        "lastIp": "183.250.0.214",
                        "statusCode": 0,
                        "picId": 770381710,
                        "picType": 0,
                        "picPower": 0,
                        "isTop": false,
                        "rank": 0,
                        "middlePicture": "http://qcloud.dpfile.com/pc/WCZZ41YmGo_0Fi1DYLvwj5XQuEhPDf-gUBs21SyFed2lSkkfXSO7vBQmufFwcoDC05mDabRMXcC-NnPom6wedQ.jpg",
                        "smallPicture": "http://qcloud.dpfile.com/pc/WCZZ41YmGo_0Fi1DYLvwj5XQuEhPDf-gUBs21SyFed3_far5cIxnKiIPM87fLh3M3dWYFEM5hoslgWXTJDjSPA.jpg",
                        "clientTypeName": "iPhone",
                        "rateGoodTotal": 0,
                        "picPrice": 0,
                        "picPowerTitle": "",
                        "tags": null
                    },
                    {
                        "orderNo": 0,
                        "status": 1,
                        "height": 700,
                        "width": 525,
                        "userId": 43133438,
                        "cityId": 15,
                        "title": "",
                        "url": "http://qcloud.dpfile.com/pc/pINJM_0hLLm8KMgWp5F7nkDfplC3_JHu8tk1uw1weNDnRpke_cQ1_sKtriigjrfxQs6E6HQccbzhvkqkRN4krQ.jpg",
                        "clientType": 2,
                        "shopId": 2325856,
                        "shopType": 60,
                        "bigPicture": "http://qcloud.dpfile.com/pc/pINJM_0hLLm8KMgWp5F7nkDfplC3_JHu8tk1uw1weNADtRtiGsuN5TG7euqw-Rk_CUldaiupJgKYTSfIaRn8IQ.jpg",
                        "lastTime": 1495190160000,
                        "addTime": 1495190160000,
                        "followNoteNo": 0,
                        "price": 0,
                        "shopGroupId": 2325856,
                        "hits": 0,
                        "lastIp": "183.250.0.214",
                        "statusCode": 0,
                        "picId": 770381709,
                        "picType": 0,
                        "picPower": 0,
                        "isTop": false,
                        "rank": 0,
                        "middlePicture": "http://qcloud.dpfile.com/pc/pINJM_0hLLm8KMgWp5F7nkDfplC3_JHu8tk1uw1weNBaTcpu13Kp8ZFV-oA0oU_o05mDabRMXcC-NnPom6wedQ.jpg",
                        "smallPicture": "http://qcloud.dpfile.com/pc/pINJM_0hLLm8KMgWp5F7nkDfplC3_JHu8tk1uw1weNDyAxtlEDu89TaL0T4C-DzE3dWYFEM5hoslgWXTJDjSPA.jpg",
                        "clientTypeName": "iPhone",
                        "rateGoodTotal": 0,
                        "picPrice": 0,
                        "picPowerTitle": "",
                        "tags": null
                    }
                ],
                "good": false,
                "reviewUser": {
                    "userId": 43133438,
                    "userNickName": "miaomiao992",
                    "userCity": 10,
                    "userPower": 5,
                    "userFace": "https://p0.meituan.net/userheadpic/onigiri.png%4048w_48h_1e_1c_1l%7Cwatermark%3D0"
                }
            }
]
}
```
**goods_info 商品信息**
```
{
    "roomList": [
        {
            "roomId": 3411048,
            "title": "8号楼高级双床房",
            "price": 544,
            "goodsList": [
                {
                    "goodsIdL": "6298943",
                    "imageList": [
                        "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                        "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                        "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                        "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                        "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                        "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                        "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                        "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                        "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png"
                    ],
                    "title": "8号楼高级双床房",
                    "price": 544,
                    "inventoryMin": 0,
                    "roomAttrList": [
                        {
                            "name": "床型",
                            "value": "单人床1.2×2.0米 2张"
                        },
                        {
                            "name": "早餐",
                            "value": "双早"
                        },
                        {
                            "name": "上网",
                            "value": "wifi和宽带"
                        },
                        {
                            "name": "窗户",
                            "value": "有"
                        },
                        {
                            "name": "可住",
                            "value": "2人"
                        },
                        {
                            "name": "卫浴",
                            "value": "独立"
                        },
                        {
                            "name": "面积",
                            "value": "30㎡"
                        }
                    ],
                    "buyUrl": "https://m.dianping.com/hotel/htorder/prepay/orderPage?shop=2325856&hotelId=4787998&otaId=19&checkin=2017-05-24&checkout=2017-05-25&roomId=3220464&platform=4&strategyId=6298943&goodsSource=1&goodsType=1&mtCityId=62&mtPartnerId=3787876&traceId=0&token=!",
                    "appBuyUrl": "dianping://hotelmtcreateorder?shopid=2325856&checkoutdate=2017-05-25&checkindate=2017-05-24&goodsid=6298943&extrainfo=&traceid=0",
                    "mwapBuyUrl": "https://dpurl.cn/s/928sot",
                    "goodsId": 6298943,
                    "breakfast": "双早",
                    "goodsType": "预付",
                    "cancelRule": "不可取消",
                    "type": 1,
                    "bedType": "双床",
                    "netType": "wifi和宽带",
                    "score": 60,
                    "mtGoodsType": 1,
                    "stockStatus": 0
                },
                {
                    "goodsIdL": "5709677",
                    "imageList": [
                        "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                        "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                        "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                        "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                        "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                        "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                        "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                        "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                        "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png"
                    ],
                    "title": "8号楼高级双床房",
                    "price": 560,
                    "inventoryMin": 0,
                    "roomAttrList": [
                        {
                            "name": "床型",
                            "value": "单人床1.2×2.0米 2张"
                        },
                        {
                            "name": "早餐",
                            "value": "双早"
                        },
                        {
                            "name": "上网",
                            "value": "wifi和宽带"
                        },
                        {
                            "name": "窗户",
                            "value": "有"
                        },
                        {
                            "name": "可住",
                            "value": "2人"
                        },
                        {
                            "name": "卫浴",
                            "value": "独立"
                        },
                        {
                            "name": "面积",
                            "value": "30㎡"
                        }
                    ],
                    "buyUrl": "https://m.dianping.com/hotel/htorder/prepay/orderPage?shop=2325856&hotelId=4787998&otaId=19&checkin=2017-05-24&checkout=2017-05-25&roomId=3220464&platform=4&strategyId=5709677&goodsSource=1&goodsType=1&mtCityId=62&mtPartnerId=500214&traceId=0&token=!",
                    "appBuyUrl": "dianping://hotelmtcreateorder?shopid=2325856&checkoutdate=2017-05-25&checkindate=2017-05-24&goodsid=5709677&extrainfo=&traceid=0",
                    "mwapBuyUrl": "https://dpurl.cn/s/928sp2",
                    "goodsId": 5709677,
                    "breakfast": "双早",
                    "goodsType": "预付",
                    "cancelRule": "不可取消",
                    "type": 1,
                    "bedType": "双床",
                    "netType": "wifi和宽带",
                    "score": 56,
                    "mtGoodsType": 1,
                    "stockStatus": 0
                },
                {
                    "goodsIdL": "5191361",
                    "imageList": [
                        "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                        "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                        "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                        "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                        "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                        "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                        "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                        "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                        "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png"
                    ],
                    "title": "8号楼高级双床房",
                    "price": 559,
                    "inventoryMin": 0,
                    "roomAttrList": [
                        {
                            "name": "床型",
                            "value": "单人床1.2×2.0米 2张"
                        },
                        {
                            "name": "早餐",
                            "value": "双早"
                        },
                        {
                            "name": "上网",
                            "value": "wifi和宽带"
                        },
                        {
                            "name": "窗户",
                            "value": "有"
                        },
                        {
                            "name": "可住",
                            "value": "2人"
                        },
                        {
                            "name": "卫浴",
                            "value": "独立"
                        },
                        {
                            "name": "面积",
                            "value": "30㎡"
                        }
                    ],
                    "buyUrl": "https://m.dianping.com/hotel/htorder/prepay/orderPage?shop=2325856&hotelId=4787998&otaId=19&checkin=2017-05-24&checkout=2017-05-25&roomId=4517906&platform=4&strategyId=5191361&goodsSource=2&goodsType=1&mtCityId=62&mtPartnerId=3922646&traceId=0&token=!",
                    "appBuyUrl": "dianping://hotelmtcreateorder?shopid=2325856&checkoutdate=2017-05-25&checkindate=2017-05-24&goodsid=5191361&extrainfo=&traceid=0",
                    "mwapBuyUrl": "https://dpurl.cn/s/928soa",
                    "goodsId": 5191361,
                    "breakfast": "双早",
                    "goodsType": "预付",
                    "cancelRule": "不可取消",
                    "type": 3,
                    "bedType": "双床",
                    "netType": "wifi和宽带",
                    "score": 55,
                    "mtGoodsType": 1,
                    "stockStatus": 0
                },
                {
                    "goodsIdL": "4556383",
                    "imageList": [
                        "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                        "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                        "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                        "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                        "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                        "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                        "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                        "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                        "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png"
                    ],
                    "title": "8号楼高级双床房",
                    "price": 565,
                    "inventoryMin": 0,
                    "roomAttrList": [
                        {
                            "name": "床型",
                            "value": "单人床1.2×2.0米 2张"
                        },
                        {
                            "name": "早餐",
                            "value": "双早"
                        },
                        {
                            "name": "上网",
                            "value": "wifi和宽带"
                        },
                        {
                            "name": "窗户",
                            "value": "有"
                        },
                        {
                            "name": "可住",
                            "value": "2人"
                        },
                        {
                            "name": "卫浴",
                            "value": "独立"
                        },
                        {
                            "name": "面积",
                            "value": "30㎡"
                        }
                    ],
                    "buyUrl": "https://m.dianping.com/hotel/htorder/prepay/orderPage?shop=2325856&hotelId=4787998&otaId=19&checkin=2017-05-24&checkout=2017-05-25&roomId=3220464&platform=4&strategyId=4556383&goodsSource=1&goodsType=1&mtCityId=62&mtPartnerId=2725564&traceId=0&token=!",
                    "appBuyUrl": "dianping://hotelmtcreateorder?shopid=2325856&checkoutdate=2017-05-25&checkindate=2017-05-24&goodsid=4556383&extrainfo=&traceid=0",
                    "mwapBuyUrl": "https://dpurl.cn/s/928sqm",
                    "goodsId": 4556383,
                    "breakfast": "双早",
                    "goodsType": "预付",
                    "cancelRule": "不可取消",
                    "type": 1,
                    "bedType": "双床",
                    "netType": "wifi和宽带",
                    "score": 52,
                    "mtGoodsType": 1,
                    "stockStatus": 0
                },
                {
                    "goodsIdL": "3760245",
                    "imageList": [
                        "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                        "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                        "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                        "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                        "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                        "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                        "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                        "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                        "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png"
                    ],
                    "title": "8号楼高级双床房",
                    "price": 620,
                    "inventoryMin": 0,
                    "roomAttrList": [
                        {
                            "name": "床型",
                            "value": "单人床1.2×2.0米 2张"
                        },
                        {
                            "name": "早餐",
                            "value": "双早"
                        },
                        {
                            "name": "上网",
                            "value": "wifi和宽带"
                        },
                        {
                            "name": "窗户",
                            "value": "有"
                        },
                        {
                            "name": "可住",
                            "value": "2人"
                        },
                        {
                            "name": "卫浴",
                            "value": "独立"
                        },
                        {
                            "name": "面积",
                            "value": "30㎡"
                        }
                    ],
                    "buyUrl": "https://m.dianping.com/hotel/htorder/prepay/orderPage?shop=2325856&hotelId=4787998&otaId=19&checkin=2017-05-24&checkout=2017-05-25&roomId=2600230&platform=4&strategyId=3760245&goodsSource=1&goodsType=1&mtCityId=62&mtPartnerId=3531895&traceId=0&token=!",
                    "appBuyUrl": "dianping://hotelmtcreateorder?shopid=2325856&checkoutdate=2017-05-25&checkindate=2017-05-24&goodsid=3760245&extrainfo=&traceid=0",
                    "mwapBuyUrl": "https://dpurl.cn/s/928spu",
                    "goodsId": 3760245,
                    "breakfast": "双早",
                    "goodsType": "预付",
                    "cancelRule": "不可取消",
                    "type": 1,
                    "bedType": "双床",
                    "netType": "wifi和宽带",
                    "score": 50,
                    "mtGoodsType": 1,
                    "stockStatus": 0
                }
            ],
            "roomAttrList": [
                {
                    "name": "床型",
                    "value": "单人床1.2×2.0米 2张"
                },
                {
                    "name": "上网",
                    "value": "wifi和宽带"
                },
                {
                    "name": "窗户",
                    "value": "有"
                },
                {
                    "name": "可住",
                    "value": "2人"
                },
                {
                    "name": "卫浴",
                    "value": "独立"
                },
                {
                    "name": "面积",
                    "value": "30㎡"
                }
            ],
            "imageList": [
                "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png",
                "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png",
                "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png",
                "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png",
                "https://p1.meituan.net/tdchotel/9fd632796a50eff99f3c8ccd770ba539305731.png",
                "https://p1.meituan.net/tdchotel/5713fd7552ebe0e9ce11ab53cf46bb7e231709.png",
                "https://p1.meituan.net/tdchotel/974bffab367c88f65b552bbe782f8f9f257768.png",
                "https://p1.meituan.net/tdchotel/17a3d9a2f726d8c46a9074946d23c477224243.png",
                "https://p1.meituan.net/tdchotel/0fa8479b0ddfb961903eee59eddcc110241476.png",
                "https://p0.meituan.net/tdchotel/c81ef9a4596e05a2a853df1fffc1115f233230.png",
                "https://p1.meituan.net/tdchotel/4d7dde5a48a8e84ae9554e24eff4534a234896.png",
                "https://p0.meituan.net/tdchotel/2e32e286cd5bd76ae4df76b0e99fe366155309.png",
                "https://p1.meituan.net/tdchotel/3a08ac0f2647cc25f5f89b0b85ef4e59255147.png"
            ],
            "isFullRoom": true,
            "firstGoodsType": 1
        }
    ]
}
```

## 店铺信息
**信息来源:**

[大众点评店铺信息列表页面](http://www.dianping.com/search/category/15/10/g0r0)

[大众点评内容也](http://www.dianping.com/shop/23540221)

[大众点评图片页](http://www.dianping.com/photos/169872900)


field | type | description
---|---|---
num | string |惟一值
name | string |标题
comment_count | int |评论总数
avg_price |int| 平均消费
starnum | int | 五十分制
special | string|特色
loc_list| string | 列表页位置
tags |list| 列表页标签 [{'name':'xx','num':'xx'},{...}]
listpics |list| 收集返回信息[{'path':'...','url':'...},{...}]
fullAddress|string |详细地址
description|string| 描述
tels |string| 电话
lng |string|
lat |string|
dishes|dict|菜品 见下表
comment |下表| 评论

**dishes 菜品信息**
[例子链接](http://www.dianping.com/ajax/json/shopDynamic/shopTabs?shopId=23540221&cityId=15&shopName=%E5%A0%82%E5%AE%B4%E8%80%81%E5%8E%A6%E9%97%A8%E7%A7%81%E6%88%BF%E8%8F%9C&power=5&mainCategoryId=251&shopType=10&shopCityId=15)

```
{
  "briefStory": "很多人对厦门菜的理解就是：海鲜，其实不然，早在七八十年代，厦门菜曾风靡一时，当时的代表酒楼有：新南轩、绿岛、鸿山、双全等，虽然它们已走入历史，但这些酒楼的代表菜品却如瑰宝般封存在厦门人的记忆中，为了勾起这些回忆，堂宴遍翻古籍，探访厦门老饕客，深度复原了一大批菜品，我们将他称之为：老厦门的失传菜~经过...",
  "dishesWithPicVO": [
    {
      "menuId": 278876,
      "shopId": 23540221,
      "dishTagName": "香酥芋泥鸭",
      "tagCount": 150,
      "priceMap": null,
      "priceCount": null,
      "finalPrice": 66,
      "officialPrice": null,
      "desc": null,
      "addTime": 1439620692000,
      "lastTime": 1495716031000,
      "defaultPicId": null,
      "defaultPicURL": "http://p0.meituan.net/poirichness/menu_8945894_169872939.jpg%40249w_249h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20",
      "officialPicId": null,
      "officialPicURL": null,
      "shopPrice": "66"
    }
  ]
}
```
**评论信息**
```
[
    {
        "reviewId": 348385269,
        "userId": 795404801,
        "shopId": 23540221,
        "shopGroupId": 10329803,
        "shopType": 10,
        "cityId": 15,
        "status": 1,
        "statusCode": 0,
        "star": {
            "title": "总体评价",
            "value": 40,
            "desc": "很好"
        },
        "reviewBody": "上了大众点评必吃榜的一家店铺，环境很是不错，在大众点评上可以直接预约位置和时间可不知道为啥我收到短信提醒了，去的时候在前台却没有找到!幸好还有空位!<br />服务态度总体很是不错，端茶倒水的很勤快，而且还送饭前小菜、油炸冰淇淋、还有饭后甜点，点了一个网友推荐的酥皮鸭和黄鱼面线～个人觉得酥皮鸭偏甜和油腻、黄鱼面线很鲜，但是不一定每个人都吃的习惯!<br />杏仁豆腐摆盘很不错，杏仁味挺重的!<br />点了一小桌菜下来，大家最喜欢的居然是蟹黄豆腐，确实很不错!<br />总体而言，服务态度真的没话说，菜品比较精致!",
        "reviewBodyLength": 240,
        "addTime": 1495066658000,
        "lastTime": 1495066658000,
        "lastIp": "106.61.4.232",
        "hits": 0,
        "flowerTotal": 3,
        "picTotal": 9,
        "followNoteNo": 0,
        "scoreList": [
            {
                "title": "口味",
                "value": 3,
                "desc": "很好"
            },
            {
                "title": "环境",
                "value": 3,
                "desc": "很好"
            },
            {
                "title": "服务",
                "value": 3,
                "desc": "很好"
            }
        ],
        "expenseInfoList": [
            {
                "title": "人均",
                "value": 70,
                "desc": "元"
            }
        ],
        "extInfoList": [
            {
                "title": "喜欢的菜",
                "hide": false,
                "values": [
                    "蟹粉豆腐"
                ],
                "desc": "喜欢的菜"
            }
        ],
        "tuangouTag": null,
        "referType": 22,
        "referId": 0,
        "extDealOrderId": 0,
        "extShanHuiOrderId": 170506458714328,
        "extOrderId": 0,
        "extDealId": 0,
        "referToken": null,
        "clientType": 1,
        "merchantFollowCount": 0,
        "type": 0,
        "reviewPics": [
            {
                "reviewId": 348385269,
                "picId": 758177083,
                "url": "5ec3eae8d8f12a7e02c3769914934f80"
            },
            {
                "reviewId": 348385269,
                "picId": 758177084,
                "url": "a3b9b599b6df8d958964c3073040bf96"
            },
            {
                "reviewId": 348385269,
                "picId": 758177085,
                "url": "c22e865bcc5e4d348577c67b61d4bd1a"
            },
            {
                "reviewId": 348385269,
                "picId": 758177086,
                "url": "f34ab73aa1b32be7b854233065b763af"
            },
            {
                "reviewId": 348385269,
                "picId": 758177087,
                "url": "b60006ff010108c010d0b8015581d67d"
            },
            {
                "reviewId": 348385269,
                "picId": 758177088,
                "url": "527adc8ce8961f64d3f4df3d0232e3e7"
            },
            {
                "reviewId": 348385269,
                "picId": 758177089,
                "url": "e8323327f39098c3df20028df6eb4883"
            },
            {
                "reviewId": 348385269,
                "picId": 758177090,
                "url": "a8540ecf9c202ec04c82363d1bdbe987"
            },
            {
                "reviewId": 348385269,
                "picId": 758177091,
                "url": "dfa93b00336105fc60c7413bc7c26f38"
            }
        ]
    }

]


```

