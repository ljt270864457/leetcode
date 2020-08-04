#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 5:46 下午
# @Author  : liujiatian
# @File    : 8.判断环的入口.py


'''

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        解题思路：
        设从头结点的距离是a，从入环口到快慢指针相遇的点的距离是b，从相遇点到还口的距离是c。
        快指针走的距离a+b+c+b；慢指针走的距离是a+b 由于快指针走的距离是慢指针走的距离的两倍，所以2(a+b)=a+b+c+b 可得a=c

        相遇后将快指针重新定位到头指针，并将步长也设置为1，然后重新让快慢指针相遇，相遇的点即为环口
        :param head:
        :return:
        '''
        slow_node = head
        fast_node = head
        while fast_node and fast_node.next and fast_node.next.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            if fast_node == slow_node:
                fast_node = head
                while fast_node != slow_node:
                    fast_node = fast_node.next
                    slow_node = slow_node.next
                return slow_node
