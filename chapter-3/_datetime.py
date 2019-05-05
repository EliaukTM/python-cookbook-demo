#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便
在上面执行非字符串操作。
"""
from datetime import datetime, timedelta

from pytz import timezone

if __name__ == '__main__':
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print(diff)

    """
    你有一个安排在 2012 年 12 月 21 日早上 9:30 的电话会议，地点在芝加哥。而你的
    朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？
    """
    d = datetime(2012, 12, 21, 9, 30, 0)
    print(d)
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)

    # Convert to Bangalore time
    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print(bang_d)

    d = datetime(2013, 3, 10, 1, 45)
    loc_d = central.localize(d)

    later = loc_d + timedelta(minutes=30)
    # 2013-03-10 02:15:00-06:00 # WRONG! WRONG!
    print(later)

    # 结果错误是因为它并没有考虑在本地时间中有一小时的跳跃。为了修正这个错误，
    # 可以使用时区对象 normalize() 方法。
    later = central.normalize(loc_d + timedelta(minutes=30))
    print(later)
