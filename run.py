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
    base_url = Readconfig.get_url()
    username = Readconfig.get_user_password()[0]
    password = Readconfig.get_user_password()[1]
    login_data = [(username,password)]
    def setup_module(module):
        print("--------执行用例开始-----------")

    def teardown_module(module):
        print("--------执行用例结束-----------")

    # @pytest.mark.login
    @pytest.mark.parametrize("username,password",login_data)
    def test_login(self,username,password):

        url = self.base_url +"/api/v1/auth-center/oauth/token?username={}&password={}&grant_type=password&scope=app&client_id=view&client_secret=view".format(username,password)
        # url = self.base_url +"/api/v1/auth-center/oauth/token"
        headers = {
            "Content-Type": "application/json",
            "charset":"UTF-8"
                   }
        # data ={
        #         "username":username,
        #         "password":password,
        #         "grant_type":"password",
        #         "scope":"app",
        #         "client_id":"view",
        #         "client_secret":"view"
        # }
        data={}
        a = get_requests("post",str(headers),url=url,data=data)
        return a.json()['access_token']
    #通过pytest.mark.parametrize遍历数组request_parameters输入参数
    @pytest.mark.skip
    @pytest.mark.parametrize("parameters", request_parameters)
    def test_1(self, parameters, modlog=modlog):
        url = self.base_url + parameters["url"]
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
        print(rq.json()['message'])


    @pytest.mark.skip
    def test_2(self,modlog=modlog):
        print(1)



if __name__ == "__main__":
    pytest.main(["-v"])
