"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: GetLogger.py
@time: 2020-4-29 上午 10:51

首先，如果商品的描述和图片与实物严重不符，具有欺诈性质甚至涉嫌诈骗，这时买家可以选择报警，或者依据《消费者权益保护法》要求卖家双倍赔偿货款。
其次，如果商品的描述和图片与实物不符但未到欺诈的程度，买家可以依据《合同法》要求解除合同并返还货款也就是退货。
最后，如果商品的描述和图片与实物只是略微不符，例如衣服显示色差等瑕疵，尚不构成根本违约，买家就不能要求卖家退货，只能下次网购的时候多加注意。

"""

import logbook
import time, sys
import pytest



time = time.strftime("%y-%m-%d %H:%M:%S")
@pytest.fixture(scope="module")
def modlog(request):
    name = request.module.__name__
    if name.startswith('test_'):
        name = name[5:]
    #创建一个logger
    logger = logbook.Logger(name)
    #文件输出路径
    logpath = '../Log'
    log_name = logpath + 'Test_'+ name + time +'.log'

    # 创建handler，用于写入日志
    logger.handlers.append(logbook.FileHandler(log_name, level="DEBUG"))
    # 创建handler，用于控制台输出
    logger.handlers.append(logbook.StreamHandler(sys.stdout, level="INFO"))

    return modlog
