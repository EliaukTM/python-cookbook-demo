#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要读写各种不同编码的文本数据，比如 ASCII，UTF-8 或 UTF-16 编码等。
"""


# 使用带有 rt 模式的 open() 函数读取文本文件。
def read():
    with open('somefile.txt', 'rt') as f:
        data = f.read()
        print(data)


# 为了写入一个文本文件，使用带有 wt 模式的 open() 函数，如果之前文
# 件内容存在则清除并覆盖掉。
def write():
    with open('somefile.txt', 'wt') as f:
        f.write("*****************")
        f.write("-----------------")

    with open('somefile.txt', 'wt') as f:
        print("line1", file=f)
        print("line2", file=f)


# 如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数。
def append():
    with open('somefile.txt', 'at') as f:
        print("line1", file=f)
        print("line2", file=f)


def encode():
    with open('somefile.txt', 'rt', encoding='latin-1') as f:
        data = f.read()
        print(data)


if __name__ == '__main__':
    encode()
