#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import math
from decimal import Decimal, localcontext

if __name__ == '__main__':
    a = 2.1
    b = 4.2
    c = a + b
    print(c)

    # 这些错误是由底层CPU和IEEE754标准通过自己的浮点单位去执行算术时的特征。
    # 由于Python的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的误差。

    # 如果你想更加精确(并能容忍一定的性能损耗)，你可以使用decimal模块
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b)
    print((a + b) == Decimal('6.3'))

    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)

    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    """
    Python新手会倾向于使用decimal模块来处理浮点数的精确运算。然而，先理解
    你的应用程序目的是非常重要的。如果你是在做科学计算或工程领域的计算、电脑绘
    图，或者是科学领域的大多数运算，那么使用普通的浮点类型是比较普遍的做法。其
    中一个原因是，在真实世界中很少会要求精确到普通浮点数能提供的17位精度。因
    此，计算过程中的那么一点点的误差是被允许的。第二点就是，原生的浮点数计算要
    快的多 - 有时候你在执行大量运算的时候速度也是非常重要的。
    """

    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))
    print(math.fsum(nums))
