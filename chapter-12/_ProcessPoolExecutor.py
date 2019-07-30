#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有个程序要执行 CPU 密集型工作，你想让他利用多核 CPU 的优势来运行的快一点。
"""

import glob
import gzip
import io


def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)

# 前面的程序使用了通常的 map-reduce 风格来编写。函数 find robots() 在一个文
# 件名集合上做 map 操作，并将结果汇总为一个单独的结果，也就是 find all robots()
# 函数中的 all robots 集合。现在，假设你想要修改这个程序让它使用多核 CPU。很
# 简单——只需要将 map() 操作替换为一个 concurrent.futures 库中生成的类似操作
# 即可。下面是一个简单修改版本：

from concurrent import futures


def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
        return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)
