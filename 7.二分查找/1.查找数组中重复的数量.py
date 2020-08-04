#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 2:51 下午
# @Author  : liujiatian
# @File    : 1.查找数组中重复的数量.py

def get_first_index(nums, target: int) -> int:
    '''
    找到第一个元素
    '''
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        elif mid == 0 or nums[mid - 1] != target:
            return mid
        else:
            high = mid - 1
    return -1


def get_last_index(nums, target: int) -> int:
    '''
    找到最后一个元素
    '''
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        elif mid == len(nums) - 1 or nums[mid + 1] != target:
            return mid
        else:
            low = mid + 1
    return -1


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return 0

        first_index = get_first_index(nums, target)
        if first_index == -1:
            return 0
        last_index = get_last_index(nums, target)
        return last_index - first_index + 1


if __name__ == '__main__':
    a = [1]
    print(Solution().search(a, 1))
