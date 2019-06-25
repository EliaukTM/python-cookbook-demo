#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

from collections import deque


# 保留长度的队列
def get_last_num_element(n):
    q = deque(maxlen=n)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)

    q.append(4)
    q.append(5)
    print(q)


# 队列操作
def deque_pop():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.appendleft(4)
    print(q)
    q.pop()
    print(q)
    q.popleft()


if __name__ == '__main__':
    get_last_num_element(3)
    deque_pop()
