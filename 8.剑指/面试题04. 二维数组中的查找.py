#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 10:10 PM
# @Author  : liujiatian

'''

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

解题思路
1.从右上角开始检索，例如 5

5<15
[
  [1,   4,  7, 11],
  [2,   5,  8, 12],
  [3,   6,  9, 16],
  [10, 13, 14, 17],
  [18, 21, 23, 26]
]

5<11
[
  [1,   4,  7],
  [2,   5,  8],
  [3,   6,  9],
  [10, 13, 14],
  [18, 21, 23]
]

5 < 7
[
  [1,   4],
  [2,   5],
  [3,   6],
  [10, 13],
  [18, 21]
]
5>4
[
  [2,   5],
  [3,   6],
  [10, 13],
  [18, 21]
]

5==5 找到了
'''


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) <= 0:
            return False

        max_row_num = len(matrix) - 1
        max_column_num = len(matrix[0]) - 1

        start_row = 0
        start_column = max_column_num

        while True:
            right_left = matrix[start_row][start_column]
            if target == right_left:
                return True
            if target < right_left:
                start_column -= 1
            else:
                start_row += 1
            if start_row > max_row_num or start_column < 0:
                return False


if __name__ == '__main__':
    a = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17],
        [18, 21, 23, 26]
    ]
    s = Solution()
    print(s.findNumberIn2DArray(a, 5))
    print(s.findNumberIn2DArray(a, 22))
