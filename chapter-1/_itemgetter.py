#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
通过某个关键字排序一个字典列表
"""
from operator import itemgetter

if __name__ == '__main__':
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)
    # 多个key
    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_lfname)
    # itemgetter() 有时候也可以用 lambda 表达式代替（使用 itemgetter() 方式会运行的稍微快点），比如
    rows_by_fname = sorted(rows, key=lambda r: r['fname'])
    rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
