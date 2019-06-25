#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想创建一个实例，但是希望绕过执行 init () 方法。
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    d = Date.__new__(Date)
    print(d)

    # print(d.year)

    # Traceback(most recent call last):
    #     File "<stdin>", line 1, in < module >
    # AttributeError: 'Date' object has no attribute 'year'

    # 结果可以看到，这个Date实例的属性year还不存在，所以你需要手动初始化
    data = {'year': 2012, 'month': 8, 'day': 29}
    for key, value in data.items():
        setattr(d, key, value)

    print(d.year)
