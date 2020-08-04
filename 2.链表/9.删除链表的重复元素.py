#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 10:10 下午
# @Author  : liujiatian
# @File    : 9.删除链表的重复元素.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

    示例 1:

    输入: 1->1->2
    输出: 1->2
    示例 2:

    输入: 1->1->2->3->3
    输出: 1->2->3
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
