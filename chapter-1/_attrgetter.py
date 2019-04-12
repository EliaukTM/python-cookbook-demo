#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想排序类型相同的对象，但是他们不支持原生的比较操作。
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


if __name__ == '__main__':
    sort_notcompare()
    # 另一种方法，使用attrgetter
    users = [User(23), User(3), User(99)]
    users = sorted(users, key=attrgetter('user_id'))
    print(users)
