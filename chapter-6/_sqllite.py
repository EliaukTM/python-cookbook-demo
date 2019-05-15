#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在关系型数据库中查询、增加或删除记录。
"""
import sqlite3

if __name__ == '__main__':

    stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
    ]

    db = sqlite3.connect('database.db')
    c = db.cursor()
    c.execute('create table portfolio (symbol text, shares integer, price real)')
    db.commit()

    c.executemany('insert into portfolio values (?,?,?)', stocks)
    db.commit()

    for row in db.execute('select * from portfolio'):
        print(row)

    min_price = 100
    for row in db.execute('select * from portfolio where price >= ?',
                          (min_price,)):
        print(row)
