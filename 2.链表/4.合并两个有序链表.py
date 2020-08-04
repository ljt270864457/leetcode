#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 11:55 上午
# @Author  : liujiatian
# @File    : 4.合并两个有序链表.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    LeetCode 21
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
    示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    '''

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哨兵节点 好用
        dummyRoot = ListNode(0)
        new_head = dummyRoot
        while (l1 or l2):
            if not l1:
                new_head.next = l2
                break

            if not l2:
                new_head.next = l1
                break

            if l1.val < l2.val:
                new_head.next = l1
                l1 = l1.next
            else:
                new_head.next = l2
                l2 = l2.next
            new_head = new_head.next
        return dummyRoot.next
