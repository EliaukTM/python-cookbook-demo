#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

# 尽管队列是最常见的线程间通信机制，但是仍然可以自己通过创建自己的数据结构并添加
# 所需的锁和同步机制来实现线程间通信。最常见的方法是使用 Condition 变量来包装
# 你的数据结构。下边这个例子演示了如何创建一个线程安全的优先级队列，如同 1.5 节
# 中介绍的那样。

import heapq
import threading


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
        return heapq.heappop(self._queue)[-1]
