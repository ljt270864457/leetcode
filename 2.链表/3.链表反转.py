#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 10:35 上午
# @Author  : liujiatian
# @File    : 3.链表反转.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 头插法
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        LeetCode 206

        图解 https://pic.leetcode-cn.com/0421a9dede52f2e7c48da1eb48c259469f67364185e24a95ec4445bc9c891d7f-image.png

        [1,2,3] -> [3,2,1]
        新建一个空的头结点，每次往头部插入
        1. new_head = None
        2. node1 -> new_head
        3. node2 -> node1 -> new_head
        4. node3 -> node2 -> node1 -> new_head

        :param head:
        :return:
        '''
        # 新的头结点
        new_head = None
        while head:
            # tmp存储当前节点的下一个节点
            tmp = head.next
            # 令当前节点的next指向新的头结点
            head.next = new_head
            # 新的头结点移动到当前节点
            new_head = head
            # 当前节点移动到下一个节点
            head = tmp
        return new_head