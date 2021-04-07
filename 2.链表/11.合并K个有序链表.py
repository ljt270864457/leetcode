#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 8:21 上午
# @Author  : liujiatian
# @File    : 11.合并K个有序链表.py

# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
#  示例:
#
#  输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#  Related Topics 堆 链表 分治算法
#  👍 840 👎 0


from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        1. 每次将所有链表的头结点（Node，index）push到head_list构成的heapq中
        2. 如果head_list不为空，弹出最小的元素，将该元素加入到新的链表；并将index对应的新头结点放入到head_list，如果没有元素，则删除lists中的这个链表
        :param lists:
        :return:
        '''
        dummy = ListNode(None)
        cur = dummy
        head_list = []
        for head in lists:
            while head:
                heapq.heappush(head_list, head.val)
                head = head.next

        while head_list:
            cur.next = ListNode(heapq.heappop(head_list))
            cur = cur.next

        return dummy.next
