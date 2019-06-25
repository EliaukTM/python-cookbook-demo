#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你在代码中使用 while 循环来迭代处理数据，因为它需要调用某个函数或者和一
般迭代模式不同的测试条件。能不能用迭代器来重写这个循环呢？
"""


def process_data(data):
    print(data)


CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(chunk)
