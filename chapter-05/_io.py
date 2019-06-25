#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想使用操作类文件对象的程序来操作文本或二进制字符串。
"""
import io

if __name__ == '__main__':
    """
    使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据。
    """
    s = io.StringIO()
    s.write('Hello World\n')

    print('This is a test', file=s)

    print(s.getvalue())

    s = io.StringIO('Hello\nWorld\n')
    print(s.read(4))
    print(s.read())

    """
    io.StringIO 只能用于文本。如果你要操作二进制数据，要使用 io.BytesIO 类来代替。
    """
    s = io.BytesIO()
    s.write(b'binary data')
    print(s.getvalue())
