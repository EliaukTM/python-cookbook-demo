#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要处理一个很大的数据集并需要计算数据总和或其他统计量。
"""
import pandas

if __name__ == '__main__':
    rats = pandas.read_csv('rats.csv', skip_footer=1)
    print(rats)

    rats['Current Activity'].unique()
    crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
    print(len(crew_dispatched))

    print(crew_dispatched['ZIP Code'].value_counts()[:10])

    dates = crew_dispatched.groupby('Completion Date')
    print(len(dates))

    date_counts = dates.size()
    print(date_counts[0:10])

    date_counts.sort()
    print(date_counts[-10:])
