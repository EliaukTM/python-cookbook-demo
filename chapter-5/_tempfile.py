#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁
掉。
"""
from tempfile import NamedTemporaryFile, TemporaryDirectory
from tempfile import TemporaryFile

if __name__ == '__main__':
    with TemporaryFile('w+t') as f:
        # Read/write to the file
        f.write('Hello World\n')
        f.write('Testing\n')
        # Seek back to beginning and read the data
        f.seek(0)
        data = f.read()

    f = TemporaryFile('w+t')
    f.close()

    """
    在大多数 Unix 系统上，通过 TemporaryFile() 创建的文件都是匿名的，甚至连目
    录都没有。如果你想打破这个限制，可以使用 NamedTemporaryFile() 来代替。
    """

    with NamedTemporaryFile('w+t') as f:
        print('filename is:', f.name)

    """
    临时目录
    """
    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)
