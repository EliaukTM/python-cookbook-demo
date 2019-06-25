#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想读写二进制文件，比如图片，声音文件等等。
"""

if __name__ == '__main__':
    with open('somefile.bin', 'rb') as f:
        data = f.read()
    with open('somefile.bin', 'wb') as f:
        f.write(b'Hello World')
