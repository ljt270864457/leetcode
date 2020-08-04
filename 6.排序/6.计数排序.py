#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 7:34 下午
# @Author  : liujiatian
# @File    : 6.计数排序.py


def count_sort(seq):
    min_val = min(seq)
    max_val = max(seq)
    counter_list = [0] * (max_val - min_val + 1)
    
