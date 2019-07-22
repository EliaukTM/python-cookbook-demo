#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据
"""

# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列
# 了。创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作
# 来向队列中添加或者删除元素

# Queue 对象已经包含了必要的锁，所以你可以通过它在多个线程间多安全地共享数
# 据。当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。一个通用的
# 解决方法是在队列中放置一个特殊的只，当消费者读到这个值的时候，终止执行。例
# 如：

from queue import Queue
from threading import Thread
# Object that signals shutdown
_sentinel = object()
# A thread that produces data
def producer(out_q):
    while running:
    # Produce some data
        ...
        out_q.put(data)
    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)
# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break

# 消费者在读到这个特殊值之后立即又把它放回到队列
# 中，将之传递下去。这样，所有监听这个队列的消费者线程就可以全部关闭了。

