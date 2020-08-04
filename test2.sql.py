#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 1:38 下午
# @Author  : liujiatian
# @File    : test2.sql

'''
select
    username,
    pageurl,
    date,
    sum(page_count) as visit_count
from
    t1
group by
    date,username,pageurl
sort by
    visit_count
'''