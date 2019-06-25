#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你的程序创建了很多循环引用数据结构 (比如树、图、观察者模式等)，你碰到了内
存管理难题。
"""

import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


if __name__ == '__main__':
    root = Node('parent')
    c1 = Node('child')
    root.add_child(c1)
    print(c1.parent)

    del root
    print(c1.parent)
