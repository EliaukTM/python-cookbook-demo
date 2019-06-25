#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想获取文件系统中某个目录下的所有文件列表
"""
import os

if __name__ == '__main__':
    names = os.listdir('somedir')

    # 获取所有的文件
    names = [name for name in os.listdir('somedir')
             if os.path.isfile(os.path.join('somedir', name))]

    # 获取所有的文件夹
    dirnames = [name for name in os.listdir('somedir')
                if os.path.isdir(os.path.join('somedir', name))]