#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 4:45 下午
# @Author  : liujiatian
# @File    : 5.快速排序.py


def quick_sort_v1(seq):
    '''
    v1方法可读性好，但是空间复杂度高，因为又声明了两个left和right两个数组
    快速排序，找到seq的最后一个元素作为分区元素，如果小于该元素，则放到分区元素的左边，否则放到右边
    :param seq:
    :return:
    '''
    if len(seq) <= 1:
        return seq

    left = []
    right = []
    pivot = seq[-1]
    # 小的放到left 大的放到right
    for i in range(len(seq) - 1):
        if seq[i] < pivot:
            left.append(seq[i])
        else:
            right.append(seq[i])
    return quick_sort_v1(left) + [pivot] + quick_sort_v1(right)


def quick_sort_v2(seq: list, left, right):
    '''
    1. 取第一个元素作为base
    2. 最左边，最右边两个元素游标为i，j
    3. while i!=j:
        while i<j and seq[j]>base
            j--
        while i<j and seq[i]<=base
            i++
        # 交换i和j元素
        seq[i],seq[j]=seq[j],seq[i]
    4. base元素和seq[i]元素交换

    5.递归1~4步骤
    '''
    # print(left, right)
    if left >= right:
        return

    i = left
    j = right
    # 第0个元素作为分界点
    base = seq[left]
    while i < j:
        while i < j and seq[j] > base:
            j -= 1
        while i < j and seq[i] <= base:
            i += 1
        seq[i], seq[j] = seq[j], seq[i]

    seq[left], seq[i] = seq[i], seq[left]
    quick_sort_v2(seq, left, i - 1)
    quick_sort_v2(seq, i + 1, right)

def quick_sort_v3(seq: list, left: int, right: int):
    if left >= right:
        return

    base = seq[left]
    i = left
    j = right
    while i < j:
        if i < j and seq[j] > base:
            j -= 1
        if i < j and seq[j] <= base:
            i += 1
        seq[i], seq[j] = seq[j], seq[i]
    seq[left], seq[i] = seq[i], seq[left]
    quick_sort_v2(seq, left, i - 1)
    quick_sort_v2(seq, i + 1, right)


if __name__ == '__main__':
    a = [8, 92, 32, 55, 1, 2, 3, 6, 0]
    # print(quick_sort_v1(a))
    quick_sort_v3(a, 0, 8)
    # quick_sort_v2(a, 0, 8)
    print(a)
