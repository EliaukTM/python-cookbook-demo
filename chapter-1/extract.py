#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai


def extract_from_array():
    p = (4, 5)
    x, y = p
    print("x = %s" % x)
    print("y = %s" % y)


def extract_from_iterator():
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(phone_numbers)


if __name__ == '__main__':
    extract_from_array()
    extract_from_iterator()
