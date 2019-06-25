#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
需要在数据序列上执行聚集函数 (比如 sum() , min() , max() )，但是首先你需
要先转换或者过滤数据
"""

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    sum = sum(x * x for x in nums)
    print(sum)

    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min(s['shares'] for s in portfolio)
    print(min_shares)

    _min_shares = min(portfolio, key=lambda s: s['shares'])
    print(_min_shares)
