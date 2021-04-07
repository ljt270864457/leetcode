#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 8:26 下午
# @Author  : liujiatian
# @File    : 接雨水.py

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。
#
#  示例:
#
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#  Related Topics 栈 数组 双指针
#  👍 1590 👎 0

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if len(height) < 2:
            return res

        max_height = max(height)
        height_group = []
        for i in range(max_height):
            tmp = []
            for index, h in enumerate(height):
                if h >= i + 1:
                    tmp.append(index)
            height_group.append(tmp)
        for group in height_group:
            if len(group) < 2:
                break
            for i in range(len(group) - 1):
                left = group[i]
                right = group[i + 1]
                res += (right - left - 1)
        return res



if __name__ == '__main__':
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(a))
