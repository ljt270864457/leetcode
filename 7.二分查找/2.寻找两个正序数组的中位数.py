#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 7:21 下午
# @Author  : liujiatian
# @File    : 寻找两个正序数组的中位数.py

# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
#
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
#  你可以假设 nums1 和 nums2 不会同时为空。
#
#
#
#  示例 1:
#
#  nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
#  示例 2:
#
#  nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#  Related Topics 数组 二分查找 分治算法
#  👍 3043 👎 0


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []

        # 将两个数组合并成一个数组
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))

        if nums1:
            nums.extend(nums1)
        if nums2:
            nums.extend(nums2)

        mid = int((len(nums) - 1) / 2)
        is_odd = len(nums) % 2 == 1
        return nums[mid] if is_odd else (nums[mid] + nums[mid + 1]) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
