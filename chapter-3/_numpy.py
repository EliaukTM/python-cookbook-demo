#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import numpy as np


def f(x):
    return 3 * x ** 2 - 2 * x + 7


# 你需要在大数据集 (比如数组或网格) 上面执行计算。
if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]

    print(x * 2)
    print(x + y)

    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])

    print(ax * 2)
    print(ax + 10)

    print(ax + ay)
    print(ax * ay)

    print(f(ax))

    print(np.sqrt(ax))
    print(np.cos(ax))

    grid = np.zeros(shape=(10000, 10000), dtype=float)
    print(grid)
    grid += 10
    print(grid)

    print(np.sin(grid))

    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
