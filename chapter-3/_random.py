#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
"""
import random

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6]

    for i in range(0, 6):
        print(random.choice(values))

    for i in range(0, 6):
        print(random.sample(values, i))

    # 打乱顺序
    random.shuffle(values)
    print(values)

    # 生成随机整数，请使用random.randint()

    print(random.randint(0, 10))

    # 为了生成0到1范围内均匀分布的浮点数，使用random.random()
    print(random.random())

    # N位随机位(二进制)的整数，使用random.getrandbits()
    print(random.getrandbits(200))
