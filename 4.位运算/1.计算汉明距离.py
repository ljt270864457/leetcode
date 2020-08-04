#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 11:36 PM
# @Author  : liujiatian
# @File    : 1.计算汉明距离.py


class Solution:
    '''
    0010
    1110

    1100 1的数量为2 汉明距离为2
    '''

    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
