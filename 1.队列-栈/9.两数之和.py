#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 11:28 上午
# @Author  : liujiatian
# @File    : 9.两数之和.py

class Solution:
    def twoSum(self, nums, target: int):
        '''
        给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

        示例:

        给定 nums = [2, 7, 11, 15], target = 9

        因为 nums[0] + nums[1] = 2 + 7 = 9
        所以返回 [0, 1]

        解法说明：
        1. 对列表进行升序排序 并记录下原索引 [-1, -2, -3, -4, -5] -> [(-5,4),(-4,3),(-3,2),(-2,1),(-1,0)]
        2. 设置左右两指针，如果左指针数据+右指针数据，左指针左移，否则右移，如果元素相加等于target，取出原索引返回
        '''
        nums = [(k, v) for k, v in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[1])
        left = 0
        right = len(nums) - 1
        while right != left:
            if nums[left][1] + nums[right][1] == target:
                return [nums[left][0], nums[right][0]]

            if nums[left][1] + nums[right][1] < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    a = [-1, -2, -3, -4, -5]
    print(Solution().twoSum(a, -8))
