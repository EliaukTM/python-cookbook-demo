#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想内存映射一个二进制文件到一个可变字节数组中，目的可能是为了随机访问它
的内容或者是原地做些修改。
"""
import mmap
import os


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


if __name__ == '__main__':
    # 为了使用这个函数，你需要有一个已创建并且内容不为空的文件。下面是一个例
    # 子，教你怎样初始创建一个文件并将其内容扩充到指定大小
    size = 1000000
    with open('data', 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')

    m = memory_map('data')
    print(len(m))

    print(m[0:10])
    print(m[0])

    m[0:11] = b'Hello World'
    m.close()

    with open('data', 'rb') as f:
        print(f.read(11))
