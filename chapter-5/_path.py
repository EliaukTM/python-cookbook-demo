#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要使用路径名来获取文件名，目录名，绝对路径等等。
"""
import os

if __name__ == '__main__':
    path = '/Users/beazley/Data/data.csv'

    print(os.path.basename(path))
    print(os.path.dirname(path))

    print(os.path.join('tmp', 'data', os.path.basename(path)))

    path = '~/Data/data.csv'
    # Expand the user's home directory
    print(os.path.expanduser(path))

    # Split the file extension
    print(os.path.splitext(path))
