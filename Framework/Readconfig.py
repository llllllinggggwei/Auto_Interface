"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: Readconfig.py
@time: 2020-4-24 上午 10:01

首先，如果商品的描述和图片与实物严重不符，具有欺诈性质甚至涉嫌诈骗，这时买家可以选择报警，或者依据《消费者权益保护法》要求卖家双倍赔偿货款。
其次，如果商品的描述和图片与实物不符但未到欺诈的程度，买家可以依据《合同法》要求解除合同并返还货款也就是退货。
最后，如果商品的描述和图片与实物只是略微不符，例如衣服显示色差等瑕疵，尚不构成根本违约，买家就不能要求卖家退货，只能下次网购的时候多加注意。

"""

import configparser, os

def get_excel_path():
    Config_Path = os.path.abspath(os.path.join(os.getcwd(), "..\\Config\\config.ini"))

    cf = configparser.ConfigParser()
    cf.read(Config_Path)

    secs = cf.sections()
    print(secs)


    excel_path = cf.get("Test-Case", "excel_path")
    return excel_path

get_excel_path()


