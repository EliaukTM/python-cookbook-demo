#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import re

if __name__ == '__main__':
    text1 = '11/27/2012'
    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')

    text2 = 'Nov 27, 2012'
    if re.match(r'\d+/\d+/\d+', text2):
        print('yes')
    else:
        print('no')

    # 多次匹配。预编译
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        print('yes')
    else:
        print('no')
