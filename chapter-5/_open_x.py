#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想向一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。也就
是不允许覆盖已存在的文件内容。
"""

if __name__ == '__main__':
    """
    可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题。
    """
    with open('somefile', 'wt') as f:
        f.write('Hello\n')

    with open('somefile', 'xt') as f:
        f.write('Hello\n')
