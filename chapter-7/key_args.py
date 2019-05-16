#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你希望函数的某些参数强制使用关键字参数传递
"""


def recv(maxsize, *, block):
    'Receives a message'
    pass


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


if __name__ == '__main__':
    recv(1024, True)
    recv(1024, block=True)

    mininum(1, 5, 2, -5, 10)
    mininum(1, 5, 2, -5, 10, clip=0)