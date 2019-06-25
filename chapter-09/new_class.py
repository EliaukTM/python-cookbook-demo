#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你在写一段代码，最终需要创建一个新的类对象。你考虑将类的定义源代码以字符
串的形式发布出去。并且使用函数比如 exec() 来执行它，但是你想寻找一个更加优雅
的解决方案。
"""


# 你可以使用函数 types.new class() 来初始化新的类对象。

# stock.py
# Example of making a class manually from parts
# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}
# Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
# 一 个 比 较 难 理 解 的 地 方 是 在 调 用 完 types.new class() 对
# Stock. module 的赋值。每次当一个类被定义后，它的 module 属性包含定义
# 它的模块名。这个名字用于生成 repr () 方法的输出。
Stock.__module__ = __name__

if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s.cost())
