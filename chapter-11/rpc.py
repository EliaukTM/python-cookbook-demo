#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在一个消息传输层如 sockets 、multiprocessing connections 或 ZeroMQ 的
基础之上实现一个简单的远程过程调用（RPC）。
"""

# rpcserver.py
import pickle


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # Receive a message
                func_name, args, kwargs = pickle.loads(connection.recv())
                # Run the RPC and send a response
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass
