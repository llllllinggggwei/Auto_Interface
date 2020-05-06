"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: RequestsProcess.py
@time: 2020-4-29 下午 3:34

首先，如果商品的描述和图片与实物严重不符，具有欺诈性质甚至涉嫌诈骗，这时买家可以选择报警，或者依据《消费者权益保护法》要求卖家双倍赔偿货款。
其次，如果商品的描述和图片与实物不符但未到欺诈的程度，买家可以依据《合同法》要求解除合同并返还货款也就是退货。
最后，如果商品的描述和图片与实物只是略微不符，例如衣服显示色差等瑕疵，尚不构成根本违约，买家就不能要求卖家退货，只能下次网购的时候多加注意。

"""
import requests
import json

def get_requests(method, headers, url, data):
    if data:
        data = eval(data)
    else:
        data = data
    if headers:
        headers = eval(headers)
    else:
        headers = headers

    # get请求
    if method == 'get' or method == 'GET':
        request = requests.get(url=url, params=data, verify=False)
        return request
    # post请求
    elif method == 'post' or method == 'POST':
        data_json = json.dumps(data)
        request = requests.post(url=url, headers=headers, data=data_json, verify=False)
        return request
    # put请求
    elif method == 'put' or method == 'PUT':
        data_json = json.dumps(data)
        request = requests.put(url=url, headers=headers, data=data_json, verify=False)
        return request
    # delete请求
    elif method == 'delete' or method == 'DELETE':
        request = requests.delete(url=url, verify=False)
        return request
    else:
        return "方法不在get,post,put,delete范围内"


