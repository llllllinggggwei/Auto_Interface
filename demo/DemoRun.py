"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: DemoRun.py
@time: 2020-4-23 下午 4:04

首先，如果商品的描述和图片与实物严重不符，具有欺诈性质甚至涉嫌诈骗，这时买家可以选择报警，或者依据《消费者权益保护法》要求卖家双倍赔偿货款。
其次，如果商品的描述和图片与实物不符但未到欺诈的程度，买家可以依据《合同法》要求解除合同并返还货款也就是退货。
最后，如果商品的描述和图片与实物只是略微不符，例如衣服显示色差等瑕疵，尚不构成根本违约，买家就不能要求卖家退货，只能下次网购的时候多加注意。

"""


class Solution:
    def isHappy(self, n: int) -> bool:
        ln = len(str(n))
        x = 0
        for i in range(ln):
            i = i+1
            if i != (ln):
                a = n % (10 ** i)
            else:
                a = n // (10 ** (i-1))
            x = x + (a ** 2)
        if x == n and x != 1:
            print("False")
            return False
        elif x == 1:
            print("666")
            return True
        else:
            Solution.isHappy(self, x)

Solution.isHappy(self=Solution,n=68)