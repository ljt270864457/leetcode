#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 9:02 下午
# @Author  : liujiatian
# @File    : tmp.py

def quick_sort_v1(seq):
    if len(seq) == 1:
        return seq

    left = []
    right = []
    pivot = seq[0]
    for i in range(1, len(seq)):
        if seq[i] < pivot:
            left.append(seq[i])
        else:
            right.append(seq[i])
    return quick_sort_v1(left) + [pivot] + quick_sort_v1(right)


def quick_sort_v2(seq, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = seq[left]
    while i < j:
        while i < j and seq[j] > pivot:
            j -= 1
        while i < j and seq[i] <= pivot:
            i += 1
        seq[i], seq[j] = seq[j], seq[i]
    seq[left], seq[i] = seq[i], seq[left]
    quick_sort_v2(seq, left, i - 1)
    quick_sort_v2(seq, i + 1, right)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head: Node):
    '''
    非递归
    :param head:
    :return:
    '''
    new_head = Node(None)
    while head:
        tmp = head.next
        head.next = new_head
        new_head = head
        head = tmp
    return new_head


def reverse_list_v2(head: Node):
    if not head.next:
        return head

    new_head = reverse_list_v2(head.next)
    head.next.next = head
    head.next = None
    return new_head


def dfs(graph, node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n)


if __name__ == '__main__':
    # a = [3, 1, 5]
    # print(quick_sort_v1(a))
    # quick_sort_v2(a, 0, 2)
    # print(a)

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    # print(reverse_list(node1).val)
    print(reverse_list_v2(node1).val)

    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': [],
        'F': ['G'],
        'G': []
    }
    visited = []
    dfs(graph, 'A')
    print(visited)
