#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想自己去实现一个新的上下文管理器，以便使用 with 语句。
"""

import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1

"""
在函数 timethis() 中，yield 之前的代码会在上下文管理器中作为 enter ()
方法执行，所有在 yield 之后的代码会作为 exit () 方法执行。如果出现了异常，
异常会在 yield 语句那里抛出。
"""


# 下面是一个更加高级一点的上下文管理器，实现了列表对象上的某种事务：
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


# 这段代码的作用是任何对列表的修改只有当所有代码运行完成并且不出现异常的情
# 况下才会生效。下面我们来演示一下：

if __name__ == '__main__':
    items = [1, 2, 3]
    with list_transaction(items) as working:
        working.append(4)
        working.append(5)

    print(items)

    with list_transaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError('oops')
