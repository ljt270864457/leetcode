#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 6:43 下午
# @Author  : liujiatian
# @File    : 5.删除链表的倒数第N个节点.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        LeetCode19
        给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
        示例：

        给定一个链表: 1->2->3->4->5, 和 n = 2.

        当删除了倒数第二个节点后，链表变为 1->2->3->5.

        解法 图解地址
        https://pic.leetcode-cn.com/6ca1b293adce7a473b5bee6b5f0838e20aa773af811373b2974f96e744e46e9d-19.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E5%80%92%E6%95%B0n%E4%B8%AA%E8%8A%82%E7%82%B9.gif

        双指针法：
        1.前指针先走n步
        2.前后指针同步后移，前指针的next为None时，后指针的next=next.next
        '''

        # 新建哨兵 ==> dum ->1->2->3->4->5
        dummy_root = ListNode(0)
        dummy_root.next = head
        # 前指针
        head_front = dummy_root
        # 后指针
        head_back = dummy_root

        # 前指针先走n步
        for _ in range(n):
            head_front = head_front.next

        while head_front.next:
            head_front = head_front.next
            head_back = head_back.next

        head_back.next = head_back.next.next
        return dummy_root.next
