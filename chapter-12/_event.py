#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你已经启动了一个线程，但是你想知道它是不是真的已经开始运行了。
"""

# Event 对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。在
# 初始情况下，event 对象中的信号标志被设置为假。如果有线程等待一个 event 对象，
# 而这个 event 对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。一个
# 线程如果将一个 event 对象的信号标志设置为真，它将唤醒所有等待这个 event 对象的
# 线程。如果一个线程等待一个已经被设置为真的 event 对象，那么它将忽略这个事件，
# 继续执行。

import time
from threading import Thread, Event


# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
print('countdown is running')

# 当你执行这段代码，“countdown is running”总是显示在“countdown starting”之
# 后显示。这是由于使用 event 来协调线程，使得主线程要等到 countdown() 函数输出
# 启动信息后，才能继续执行。