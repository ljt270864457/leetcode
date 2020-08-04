#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 9:20 PM
# @Author  : liujiatian
# @File    : stack.py

class MinStack(object):
    '''

    LeetCode155 最小栈

    首先想到是利用python中的列表来做，进栈用append，出栈用pop，但是这里还有一个小要求是要能检索到栈中的最小元素并且是在常数时间内。

    算法一般都是空间换时间或者时间换空间，要想得到最小元素并且是在常数时间内，在建栈的时候就保存这个索引就行了，详情见代码。

    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        cur_min = self.getMin()
        if not cur_min or x < cur_min:
            cur_min = x
        self.stack.append([x, cur_min])

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            cur_min = None
        else:
            cur_min = self.stack[-1][1]
        return cur_min


if __name__ == '__main__':
    obj = MinStack()
    for i in reversed(range(0, 3)):
        obj.push(i)
    print(obj.stack)

    for i in range(2):
        obj.pop()
    print(obj.stack)
