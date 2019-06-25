#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些
操作，比如查找值或者检查某些键是否存在。
"""
from collections import ChainMap

if __name__ == '__main__':
    """
    先从 a 中找，如果找不到再在 b中找
    """
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)
    print(c['x'])  # Outputs 1 (from a)
    print(c['y'])  # Outputs 2 (from b)
    print(c['z'])  # Outputs 3 (from a)
