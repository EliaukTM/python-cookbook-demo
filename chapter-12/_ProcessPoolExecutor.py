#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有个程序要执行 CPU 密集型工作，你想让他利用多核 CPU 的优势来运行的快一点。
"""

"""
oncurrent.futures 库提供了一个 ProcessPoolExecutor 类，可被用来在一个单
独的 Python 解释器中执行计算密集型函数。不过，要使用它，你首先要有一些计算密
集型的任务。我们通过一个简单而实际的例子来演示它。假定你有个 Apache web 服务
器日志目录的 gzip 压缩包：

logs/
20120701.log.gz
20120702.log.gz
20120703.log.gz
20120704.log.gz
20120705.log.gz
20120706.log.gz
...

进一步假设每个日志文件内容类似下面这样：

124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369
61.135.216.105 - - [10/Jul/2012:00:20:04 -0500] "GET /blog/atom.xml ..." 304 -
...

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
