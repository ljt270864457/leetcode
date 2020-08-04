#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 4:39 下午
# @Author  : liujiatian
# @File    : 4.归并排序.py

def merge(left, right):
    tmp = []
    # 两个数组的指针
    i = 0
    j = 0
    # 对left和right进行排序并合并到tmp中
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            tmp.append(right[j])
            j += 1
        else:
            tmp.append(left[i])
            i += 1
    tmp.extend(left[i:])
    tmp.extend(right[j:])
    return tmp


def merge_sort(seq):
    '''
    归并排序
    利用分治的思想，将数组分为左右两部分，每次分别对左右两部分进行排序合并
    时间复杂度 O(nlogn)
    :param seq:
    :return:

    递推公式：merge_sort(p…r) = merge(merge_sort(p…q), merge_sort(q+1…r))
    终止条件：p >= r 不用再继续分解
    '''
    if len(seq) <= 1:
        return seq

    # 将整个数组分成左右两部分，每部分都去做合并排序
    m_index = int(len(seq) / 2)
    # 递归执行
    left = merge_sort(seq[:m_index])
    right = merge_sort(seq[m_index:])
    return merge(left, right)


if __name__ == '__main__':
    a = [8, 92, 32, 55, 1, 2, 3, 6, 0]
    print(merge_sort(a))
