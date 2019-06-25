#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想测试一个文件或目录是否存在。
"""
import os
import time

if __name__ == '__main__':
    os.path.exists('/etc/passwd')
    os.path.exists('/tmp/spam')

    os.path.isfile('/etc/passwd')
    os.path.isdir('/etc/passwd')

    # 软连接
    os.path.islink('/usr/local/bin/python3')
    os.path.realpath('/usr/local/bin/python3')

    os.path.getsize('/etc/passwd')
    os.path.getmtime('/etc/passwd')

    time.ctime(os.path.getmtime('/etc/passwd'))
