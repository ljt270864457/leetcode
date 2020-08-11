#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 7:23 下午
# @Author  : liujiatian
# @File    : 3.组合总和.py

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#  candidates 中的数字可以无限制重复被选取。
#
#  说明：
#
#
#  所有数字（包括 target）都是正整数。
#  解集不能包含重复的组合。
#
#
#  示例 1：
#
#  输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
#
#
#  示例 2：
#
#  输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#
#
#  提示：
#
#
#  1 <= candidates.length <= 30
#  1 <= candidates[i] <= 200
#  candidate 中的每个元素都是独一无二的。
#  1 <= target <= 500
#
#  Related Topics 数组 回溯算法
#  👍 802 👎 0


class Solution:
    def combinationSum(self, candidates, target):
        def backtrace(number_list, target):
            if sum(number_list) == target and sorted(number_list) not in result:
                result.append(sorted(number_list))
                return

            for number in candidates:
                cur_sum = sum(number_list)
                if cur_sum + number <= target:
                    backtrace(number_list + [number], target)

        if not candidates:
            return []

        result = []
        backtrace([], target)
        return result


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
