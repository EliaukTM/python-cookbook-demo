#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想直接读取二进制数据到一个可变缓冲区中，而不需要做任何的中间复制操作。
或者你想原地修改数据并将它写回到一个文件中去。
"""
import os


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


if __name__ == '__main__':
    with open('sample.bin', 'wb') as f:
        f.write(b'Hello World')

    buf = read_into_buffer('sample.bin')
    print(buf)

    print(buf[0:5])

    with open('newsample.bin', 'wb') as f:
        f.write(buf)
    buf = read_into_buffer('sample.bin')
    print(buf)