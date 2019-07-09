#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你在不同的机器上面运行着多个 Python 解释器实例，并希望能够在这些解释器之
间通过消息来交换数据。
"""

import traceback
from multiprocessing.connection import Listener


def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')


def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 25000), authkey=b'peekaboo')

# >>> from multiprocessing.connection import Client
# >>> c = Client(('localhost', 25000), authkey=b'peekaboo')
# >>> c.send('hello')
# >>> c.recv()
# 'hello'
# >>> c.send(42)
# >>> c.recv()
# 42
# >>> c.send([1, 2, 3, 4, 5])
# >>> c.recv()
# [1, 2, 3, 4, 5]
# >>>
