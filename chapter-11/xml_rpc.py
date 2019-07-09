#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想找到一个简单的方式去执行运行在远程机器上面的 Python 程序中的函数或方
法。
"""

from xmlrpc.server import SimpleXMLRPCServer

# 实现一个远程方法调用的最简单方式是使用 XML-RPC。下面我们演示一下一个实
# 现了键 -值存储功能的简单服务器：

class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


# Example
if __name__ == '__main__':
    kvserv = KeyValueServer(('', 15000))
    kvserv.serve_forever()


# 下面我们从一个客户端机器上面来访问服务器：

# >>> from xmlrpc.client import ServerProxy
# >>> s = ServerProxy('http://localhost:15000', allow_none=True)
# >>> s.set('foo', 'bar')
# >>> s.set('spam', [1, 2, 3])
# >>> s.keys()
# ['spam', 'foo']
# >>> s.get('foo')
# 'bar'
# >>> s.get('spam')
# [1, 2, 3]
# >>> s.delete('spam')
# >>> s.exists('spam')
# False
# >>>