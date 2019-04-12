#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']

    ivals = list(filter(is_int, values))
    print(ivals)
    # Outputs ['1', '2', '-3', '4', '5']
