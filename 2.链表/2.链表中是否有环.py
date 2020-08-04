#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 10:27 上午
# @Author  : liujiatian
# @File    : 2.链表中是否有环.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        141.给定一个链表，判断链表中是否有环。

        为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

        解决思路：
        使用快慢指针，类似于小学奥数的追及问题。
        快指针每次走两步，慢指针每次走一步。
            如果快指针追上慢指针，则说明链表有环；
            如果慢指针.next 或快指针.next.next为None，那么就没有环

        :param head:
        :return:
        '''
        if not head or not head.next:
            return False

        fast_node = head.next
        slow_node = head
        while (fast_node != slow_node):
            if not fast_node.next or not fast_node.next.next or not slow_node.next:
                return False
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return True

