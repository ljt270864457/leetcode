#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 10:46 上午
# @Author  : liujiatian
# @File    : 7.旋转链表.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''

        LeetCode61：给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

        示例 1:

        输入: 1->2->3->4->5->NULL, k = 2
        输出: 4->5->1->2->3->NULL
        解释:
        向右旋转 1 步: 5->1->2->3->4->NULL
        向右旋转 2 步: 4->5->1->2->3->NULL
        示例 2:

        输入: 0->1->2->NULL, k = 4
        输出: 2->0->1->NULL
        解释:
        向右旋转 1 步: 2->0->1->NULL
        向右旋转 2 步: 1->2->0->NULL
        向右旋转 3 步: 0->1->2->NULL
        向右旋转 4 步: 2->0->1->NULL


        解题思路
        1.遍历链表，计算元素的个数,并构建环形链表
        2. 遍历 (count-k%count)次，此时指针指向链表尾，下一个node是链表头
        '''

        if not head:
            return head

        # 声明一个哨兵
        dummy = ListNode(0)
        dummy.next = head
        new_head = dummy

        # 记录链表长度并将链表构建成环形链表
        count = 0
        while head:
            count += 1
            if head.next:
                head = head.next
            else:
                head.next = dummy.next
                break

        for _ in range(count - k % count):
            new_head = new_head.next

        # 下一个node
        tmp = new_head.next
        # 断开链表
        new_head.next = None
        # 新的链表头
        new_head = tmp
        return new_head

