#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。
"""
import re

if __name__ == '__main__':
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    split = re.split(r'[;,\s]\s*', line)
    print(split)

    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)

    # [开始：结束：一步]
    values = fields[::2]
    print(values)
    delimiters = fields[1::2] + ['']
    print(delimiters)

    join = ''.join(v + d for v, d in zip(values, delimiters))
    print(join)
