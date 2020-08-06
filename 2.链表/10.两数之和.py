#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 8:25 下午
# @Author  : liujiatian
# @File    : 10.两数之和.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        问题描述
        给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

        如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

        您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

        示例：

        输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 0 -> 8
        原因：342 + 465 = 807

        思路：
        1. 将两个链表补成一样的长度，短链表用0补位
        2. 初始化gt_10为False 如果两个数相加大于等于10为True(注意考虑上次是否有进位，如果进位需要判断x1+x2+1是否大于等于10)
        3. 计算当前位数的值，如果不需要进位，直接相加，负责加1
        4. 如果最后遍历完链表后gt_10为True，需要新加一个1的尾结点
        '''
        new_head = ListNode(None)
        dummy = new_head
        if not l1 and not l2:
            return dummy

        gt_10 = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            value = (l1.val + l2.val + 1) % 10 if gt_10 else (l1.val + l2.val) % 10
            gt_10 = l1.val + l2.val + gt_10 >= 10
            new_head.next = ListNode(value)

            l1 = l1.next
            l2 = l2.next
            new_head = new_head.next

        if gt_10:
            new_head.next = ListNode(1)
        return dummy.next

