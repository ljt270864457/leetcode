#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 8:57 下午
# @Author  : liujiatian
# @File    : 8.下一个最小的元素.py

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        '''
        496. 下一个更大元素 I
        给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

        nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

        示例 1:

        输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
        输出: [-1,3,-1]
        解释:
            对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
            对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
            对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
        示例 2:

        输入: nums1 = [2,4], nums2 = [1,2,3,4].
        输出: [3,-1]
        解释:
            对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
            对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
         

        解题思路：
        1. 构建一张hash表，这个表存了nums2中每个元素对应的下一个最大的数
        2. 构建一个递减栈，如果该元素小于栈顶元素，入栈；否则弹出所有比当前元素小的元素并计入hash表中，并把当前元素存入到栈中
        '''

        hash_map = {}
        stack = []
        for i in nums2:
            if not stack or i < stack[-1]:
                stack.append(i)
            else:
                while stack and stack[-1] < i:
                    hash_map[stack.pop()] = i
                stack.append(i)
        return [hash_map.get(_, -1) for _ in nums1]


if __name__ == '__main__':
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(Solution().nextGreaterElement(nums1, nums2))
