#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想读写一个 CSV 格式的文件。
"""
import csv
from collections import namedtuple

if __name__ == '__main__':
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            # Process row
            pass

    """
    在上面的代码中， row 会是一个元组。因此，为了访问某个字段，你需要使用下
    标，如 row[0] 访问 Symbol， row[4] 访问 Change。
    """

    with open('stock.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            # Process row
            pass

    """
    它允许你使用列名如 row.Symbol 和 row.Change 代替下标访问。需要注意的是这
    个只有在列名是合法的 Python 标识符的时候才生效。如果不是的话，你可能需要修改
    下原始的列名 (如将非标识符字符替换成下划线之类的)。
    """

    with open('stocks.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            # process row
            pass

    """
    在这个版本中，你可以使用列名去访问每一行的数据了。比如，row['Symbol'] 或
    者 row['Change'] 。
    """

    """
    为了写入 CSV 数据，你仍然可以使用 csv 模块，不过这时候先创建一个 writer 对象。
    """
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

    """
    如果你有一个字典序列的数据，可以像这样做：
    """
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.46, 'Volume': 935000}, ]
    with open('stocks.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)
