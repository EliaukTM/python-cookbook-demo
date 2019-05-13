#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在文本模式打开的文件中写入原始的字节数据。
"""
import sys

if __name__ == '__main__':
    # sys.stdout.write(b'Hello\n')
    sys.stdout.buffer.write(b'Hello\n')
