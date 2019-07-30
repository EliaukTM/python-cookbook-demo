#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你创建一个工作者线程池，用来相应客户端请求或执行其他的工作。
"""

# concurrent.futures 函数库有一个 ThreadPoolExecutor 类可以被用来完成这个
# 任务。下面是一个简单的 TCP 服务器，使用了一个线程池来响应客户端：

from concurrent.futures import ThreadPoolExecutor


def echo_client(sock, client_addr):
    '''
    Handle a client connection
    '''
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
    pool.submit(echo_client, client_sock, client_addr)


echo_server(('', 15000))

# 如果你想手动创建你自己的线程池，通常可以使用一个 Queue 来轻松实现。下面
# 是一个稍微不同但是手动实现的例子：

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


def echo_client(q):
    '''
    Handle a client connection
    '''
    sock, client_addr = q.get()
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
    sock.sendall(msg)
    print('Client closed connection')
    sock.close()


def echo_server(addr, nworkers):
    # Launch the client workers
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()
    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))


echo_server(('', 15000), 128)

# 使用 ThreadPoolExecutor 相对于手动实现的一个好处在于它使得任务提交者更方
# 便的从被调用函数中获取返回值。例如，你可能会像下面这样写：

from concurrent.futures import ThreadPoolExecutor
import urllib.request
def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data
pool = ThreadPoolExecutor(10)
# Submit work to the pool
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')
# Get the results back
x = a.result()
y = b.result()