#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要保存正在运行线程的状态，这个状态对于其他的线程是不可见的。
"""

# 有时在多线程编程中，你需要只保存当前运行线程的状态。要这么做，可使用
# thread.local() 创建一个本地线程存储对象。对这个对象的属性的保存和读取操作都
# 只会对执行线程可见，而其他线程并不可见。

import threading
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock


# 代 码 中， 自 己 观 察 对 于 self.local 属 性 的 使 用。 它 被 初 始 化 尾 一 个
# threading.local() 实例。其他方法操作被存储为 self.local.sock 的套接字对象。
# 有了这些就可以在多线程中安全的使用 LazyConnection 实例了。
from functools import partial


def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    print('Got {} bytes'.format(len(resp)))


if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))
    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
