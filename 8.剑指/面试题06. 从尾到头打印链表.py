#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 6:34 PM
# @Author  : liujiatian
# @File    : 面试题06. 从尾到头打印链表.py

import sys

sys.setrecursionlimit(100000)
from typing import List

'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]


解法1：
    辅助栈法
    1.从头到尾遍历链表，将每个元素按顺序入栈
    2.弹出栈，将每个元素进行打印

解法2：
    递归法
    reversePrint(1)
    reversePrint(1) -> reversePrint(3)
    reversePrint(1) ->reversePrint(3) -> reversePrint(2)
    reversePrint(1) ->reversePrint(3) -> reversePrint(2) -> []

    reversePrint(1) <- reversePrint(3) <- reversePrint(2) <- []
    reversePrint(1) <- reversePrint(3) <- [2]
    reversePrint(1) <- [2,3]
    [2,3,1]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # 辅助栈法
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

    # 递归法
    def reversePrint_2(self, head: ListNode) -> List[int]:
        '''
        reversePrint(1)
        reversePrint(1) -> reversePrint(3)
        reversePrint(1) ->reversePrint(3) -> reversePrint(2)
        reversePrint(1) ->reversePrint(3) -> reversePrint(2) -> []

        reversePrint(1) <- reversePrint(3) <- reversePrint(2) <- []
        reversePrint(1) <- reversePrint(3) <- [2]
        reversePrint(1) <- [2,3]
        [2,3,1]
        '''
        return self.reversePrint(head.next) + [head.val] if head else []
