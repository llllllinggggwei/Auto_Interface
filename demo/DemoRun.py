"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: DemoRun.py
@time: 2020-4-23 下午 4:04

首先，如果商品的描述和图片与实物严重不符，具有欺诈性质甚至涉嫌诈骗，这时买家可以选择报警，或者依据《消费者权益保护法》要求卖家双倍赔偿货款。
其次，如果商品的描述和图片与实物不符但未到欺诈的程度，买家可以依据《合同法》要求解除合同并返还货款也就是退货。
最后，如果商品的描述和图片与实物只是略微不符，例如衣服显示色差等瑕疵，尚不构成根本违约，买家就不能要求卖家退货，只能下次网购的时候多加注意。

"""
import requests,json
from Framework.RequestsProcess import get_requests

url = 'http://181.181.0.33:22020/api/acs/v1/door_ban/insert'
data = {
 "doorBanSn":"1111",
 "ip":"1.1.1.1",
 "doorBanName":"门禁1",
 "manufacturer":"厂商1",
 "model":"型号1",
 "longitude":120.333,
 "latitude":20.333,
 "regionCode":"330104",
 "communityCode":"330104",
 "direction":"0",
 "installationAddress":"杭州下去",
 "remark":"没有备注",
 "state":0
}

headers = str({'Content-Type':'application/json'})

# a = requests.post(url=url, headers=headers,data=json.dumps(data),verify=False)
# print(a.json())
print(headers)
print(url)
print(type(data))
a = get_requests(method='post',url=url, headers=headers,data=data)
print(a.json())
