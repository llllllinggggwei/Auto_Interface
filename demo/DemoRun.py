"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: DemoRun.py
@time: 2020-4-23 下午 4:04

首先，如果商品的描述和图片与实物严重不符，具有欺诈性质甚至涉嫌诈骗，这时买家可以选择报警，或者依据《消费者权益保护法》要求卖家双倍赔偿货款。
其次，如果商品的描述和图片与实物不符但未到欺诈的程度，买家可以依据《合同法》要求解除合同并返还货款也就是退货。
最后，如果商品的描述和图片与实物只是略微不符，例如衣服显示色差等瑕疵，尚不构成根本违约，买家就不能要求卖家退货，只能下次网购的时候多加注意。

"""

import os, time

os.path.abspath(os.path.join(os.getcwd(), "..\\Config\\config.ini"))
# from Framework import DealData
#
#
# excel_file = "/test.xlsx"
# def aaaa(excel_file):
#     result = DealData.get_excel_text(excel_file)
#     print(result)
#     a = iter(result)
#     print(x for x in range(5))
#     # print(result[0])
#     # print(result[0]['url'])
#     # print(len(result))
#
# aaaa(excel_file)
#
# import requests, json
#
# url = 'http://181.181.0.50:22020/api/camera/v1/camera/insert'
# url_get = 'https://181.181.0.50:24220/bow/search/detail/person'
# url1 = 'www.baidu.com'
# data = {
# 	"id":"",
# 	"cameraSn":"10011",
# 	"direction":"",
# 	"manufacturer":"",
# 	"model":"ssr1l2",
# 	"cameraName":"python_post",
# 	"ip":"181.181.111.2",
# 	"regionCode":"330105",
# 	"communityCode":"330106B10F4C",
# 	"longitude":70.27,
# 	"latitude":96.40,
# 	"state":5,
# 	"installationAddress":"",
# 	"type":9,
# 	"username":"admin",
# 	"password":"abcd1234",
# 	"remark":"cevcya"
# }
# params = {"idcard":"331021199901010101",
#            "personType":"3"}
# data_json = json.dumps(data)
# headers = {"Content-Type":"application/json"}
# r = requests.post(url=url,data=data_json,headers=headers).json()
# r1 = requests.post(url=url,data=data_json,headers=headers)
# rget = requests.get(url=url_get,params=params,verify=False)
# # print(r.text["status"])
# print(r)
# print(r1.status_code)
