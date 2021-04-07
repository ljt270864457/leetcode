#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 10:00 上午
# @Author  : liujiatian
# @File    : 下一个排列.py

# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
#  必须原地修改，只允许使用额外常数空间。
#
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 1,2,3,8,5,7,6,4 -> 1,2,3,8,6,4,5,7
#  Related Topics 数组
#  👍 605 👎 0


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        解题思路：参考自
        1.从第0个元素向后查，找到第一个大于该元素所在的索引j，如果没找到，说明是降序，直接reverse即可
        2.从j向后遍历，找到第一个比nums[j]大的第一个元素索引k，交换nums[j],nums[k]
        3.排序第j+1个元素到最后一个元素升序排列
        """
        nums_len = len(nums)
        if nums_len < 2:
            return
        