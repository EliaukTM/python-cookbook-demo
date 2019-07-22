#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要对多线程程序中的临界区加锁以避免竞争条件。
"""

import threading


class SharedCounter:
    """
    A counter object that can be shared by multiple threads.
    """

    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        """
        Increment the counter with locking
        """
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        """
        Decrement the counter with locking
        """
        with self._value_lock:
            self._value -= delta


# Lock 对象和 with 语句块一起使用可以保证互斥执行，就是每次只有一个线程可以
# 执行 with 语句包含的代码块。with 语句会在这个代码块执行前自动获取锁，在执行结
# 束后自动释放锁。