#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai


from datetime import timedelta, datetime

if __name__ == '__main__':
    """
    你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。
    """
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)

    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    # 如果你想表示指定的日期和时间，先创建一个datetime实例然后使用标准的数学运算来操作它们
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))

    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)

    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    print(a - b)

    print((a - b).days)

    c = datetime(2013, 3, 1)
    d = datetime(2013, 2, 28)
    print((c - d).days)

    """
    你需要查找星期中某一天最后出现的日期，比如星期五。
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']


    def get_previous_byday(dayname, start_date=None):
        if start_date is None:
            start_date = datetime.today()
        day_num = start_date.weekday()
        day_num_target = weekdays.index(dayname)
        days_ago = (7 + day_num - day_num_target) % 7
        if days_ago == 0:
            days_ago = 7
        target_date = start_date - timedelta(days=days_ago)
        return target_date


    print(datetime.today())
    print(get_previous_byday('Friday'))
