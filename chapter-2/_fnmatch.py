#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
from fnmatch import fnmatch, fnmatchcase

if __name__ == '__main__':
    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print(names)
    csv_ = [name for name in names if fnmatch(name, 'Dat*.csv')]
    print(csv_)

    # 完全使用你的模式大小写匹配
    _fnmatchcase = fnmatchcase('foo.txt', '*.TXT')
    print(_fnmatchcase)
