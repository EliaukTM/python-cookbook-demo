#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在不关闭一个已打开的文件前提下增加或改变它的 Unicode 编码。
"""
import io
import sys
import urllib

if __name__ == '__main__':
    """
    如果你想给一个以二进制模式打开的文件添加 Unicode 编码/解码方式，可以使用io.TextIOWrapper() 对象包装它。
    """
    u = urllib.request.urlopen('http://www.python.org')
    f = io.TextIOWrapper(u, encoding='utf-8')
    text = f.read()

    """
    如果你想修改一个已经打开的文本模式的文件的编码方式，可以先使用 detach()
    方法移除掉已存在的文本编码层，并使用新的编码方式代替
    """

    print(sys.stdout.encoding)
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
    print(sys.stdout.encoding)
