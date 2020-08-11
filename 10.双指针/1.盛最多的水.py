#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 8:20 上午
# @Author  : liujiatian
# @File    : 盛最多的水.py

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#
#
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
#  示例：
#
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#  Related Topics 数组 双指针
#  👍 1719 👎 0


# class Solution:
#     def maxArea(self, height) -> int:
#         '''
#         使用滑窗法解决该问题
#         1.初始化滑窗window=len(height)-1,len(height)-2...1
#         2.左指针left=0 右指针right=window 宽度window 盛水量min(height[left],height[right])*window
#         :param height:
#         so slow
#         :return:
#         '''
#         max_area = 0
#         len_height = len(height)
#         if len_height < 2:
#             return max_area
#
#         window = len_height - 1
#         while window > 0:
#             left = 0
#             right = window
#             while right < len_height:
#                 max_area = max(min(height[left], height[right]) * window, max_area)
#                 left += 1
#                 right += 1
#             window -= 1
#         return max_area

class Solution:
    def maxArea(self, height) -> int:
        '''
        使用双指针法
        1.init left=0 right=len(height-1)
        2. 如果左边界小于右边界；左指针右移；反之，右指针左移
        :param height:
        so slow
        :return:
        '''
        max_area = 0
        len_height = len(height)
        if len_height < 2:
            return max_area

        left = 0
        right = len_height - 1
        while right > left:
            width = right - left
            max_area = max(width * min(height[left], height[right]), max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
