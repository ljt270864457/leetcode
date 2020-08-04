#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 6:37 PM
# @Author  : liujiatian
# @File    : 面试题03. 数组中重复的数字.py


'''
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3


法一：
通过hash表去判断是否有重复 时间复杂度O(n) 空间复杂度O(n)

法二：
利用下标法进行判断
遍历每个元素索引为k，值为v
如果k==v continue
while v!=data[v]:
    if v==data[v]:
        出现重复了
    交换两数据直到v==data[v]
'''


class Solution(object):

    # def findRepeatNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     tmp_hash = {}
    #     for _ in nums:
    #         if _ in tmp_hash:
    #             return _
    #         else:
    #             tmp_hash[_] = 0
    #     return

    def findRepeatNumber(self, nums):
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]

                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return


if __name__ == '__main__':
    data = [2, 3, 1, 0, 2, 5, 3]
    s = Solution()
    print(s.findRepeatNumber(data))
