"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: run.py
@time: 2020-4-23 下午 2:49

首先，如果商品的描述和图片与实物严重不符，具有欺诈性质甚至涉嫌诈骗，这时买家可以选择报警，或者依据《消费者权益保护法》要求卖家双倍赔偿货款。
其次，如果商品的描述和图片与实物不符但未到欺诈的程度，买家可以依据《合同法》要求解除合同并返还货款也就是退货。
最后，如果商品的描述和图片与实物只是略微不符，例如衣服显示色差等瑕疵，尚不构成根本违约，买家就不能要求卖家退货，只能下次网购的时候多加注意。

"""

import pytest
import json

from Framework import DealData, Readconfig
from Framework.GetLogger import modlog
from Framework.RequestsProcess import get_requests


class Test_Interface(object):
    excel_path = Readconfig.get_excel_path()
    request_parameters = DealData.get_excel_text(excel_path)
    def setup_module(module):
        print("setup_module")

    def teardown_module(module):
        print("tearDown_module")

    #通过pytest.mark.parametrize遍历数组request_parameters输入参数
    @pytest.mark.parametrize("parameters", request_parameters)
    def test_1(self, parameters, modlog=modlog):
        url = parameters["url"]
        data = parameters["data"]
        headers = parameters["headers"]
        method = parameters["method"]
        assert_data = str(parameters["assert-text"])
        state = parameters["state"]
        rq = get_requests(method=method, url=url, data=data, headers=headers)
        print(rq.text)
        assert rq.status_code == 200
        assert rq.json()['status'] == state
        assert assert_data in rq.json()['message']



    def test_2(self,modlog=modlog):
        print(1)



if __name__ == "__main__":
    pytest.main(["-v"])
