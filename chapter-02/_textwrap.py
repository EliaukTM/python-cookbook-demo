#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一些长字符串，想以指定的列宽将它们重新格式化。
"""
import textwrap

if __name__ == '__main__':
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."
    print(textwrap.fill(s, 70))
    print(textwrap.fill(s, 40))
    print(textwrap.fill(s, 40, initial_indent=' '))
    print(textwrap.fill(s, 40, subsequent_indent=' '))
