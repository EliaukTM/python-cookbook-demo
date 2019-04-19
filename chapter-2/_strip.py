#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import re

if __name__ == '__main__':
    s = ' hello world \n'
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    t = '-----hello====='
    print(t.lstrip('-'))
    print(t.strip('-='))

    s = ' hello world \n'
    s = s.strip()
    print(s)

    # 去掉中间的空格
    print(s.replace(' ', ''))
    print(re.sub('\s+', ' ', s))
