#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai


if __name__ == '__main__':
    def apply_async(func, args, *, callback):
        # Compute the result
        result = func(*args)

        # Invoke the callback with the result
        callback(result)


    def print_result(result):
        print('Got:', result)


    def add(x, y):
        return x + y


    apply_async(add, (2, 3), callback=print_result)

    apply_async(add, ('hello', 'world'), callback=print_result)

    """
    为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函
    数。比如，下面这个类会保存一个内部序列号，每次接收到一个 result 的时候序列号加 1：
    """


    class ResultHandler:
        def __init__(self):
            self.sequence = 0

        def handler(self, result):
            self.sequence += 1
            print('[{}] Got: {}'.format(self.sequence, result))


    r = ResultHandler()
    apply_async(add, (2, 3), callback=r.handler)

    apply_async(add, ('hello', 'world'), callback=r.handler)

    """
    第二种方式，作为类的替代，可以使用一个闭包捕获状态值
    """


    def make_handler():
        sequence = 0

        def handler(result):
            nonlocal sequence
            sequence += 1
            print('[{}] Got: {}'.format(sequence, result))
        return handler


    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ('hello', 'world'), callback=handler)

    """
    还有另外一个更高级的方法，可以使用协程来完成同样的事情
    """


    def make_handler():
        sequence = 0
        while True:
            result = yield
            sequence += 1
            print('[{}] Got: {}'.format(sequence, result))


    handler = make_handler()
    next(handler)
    apply_async(add, (2, 3), callback=handler.send)
    apply_async(add, ('hello', 'world'), callback=handler.send)
