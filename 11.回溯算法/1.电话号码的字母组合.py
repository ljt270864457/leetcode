#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 10:03 上午
# @Author  : liujiatian
# @File    : 电话号码的字母组合.py

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#  示例:
#
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
#  说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#  Related Topics 字符串 回溯算法
#  👍 823 👎 0


class Solution:
    def letterCombinations(self, digits: str):
        '''
        使用回溯算法解决该问题
        定义函数 backtrack(combination, nextdigit)，
        当nextdigit 非空时，对于 nextdigit[0] 中的每一个字母 letter，执行回溯 backtrack(combination + letter,nextdigit[1:]，直至 nextdigit 为空。最后将 combination 加入到结果中。
        :param digits:
        :return:
        '''
        number_2_str = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrace(combine, next_digits):
            if len(next_digits) == 0:
                result.append(combine)
                return

            for char in number_2_str.get(next_digits[0]):
                backtrace(combine + char, next_digits[1:])

        result = []
        if not digits:
            return []
        backtrace('', digits)
        return result


if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations(digits))
