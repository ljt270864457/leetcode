#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 11:57 上午
# @Author  : liujiatian
# @File    : 2.括号生成.py

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法
#  👍 1223 👎 0


class Solution:
    def generateParenthesis(self, n: int):
        '''
        1.递归终止条件 l_count,r_count==0,0
        如果l_count>0 可以添加(;
        如果 ( 数量比 ) 数量多，可以添加 )
        :param n:
        :return:
        '''
        def backtrace(combine, l_count, r_count):
            if l_count == 0 and r_count == 0:
                result.append(combine)
                return

            # 添加左括号
            if l_count > 0:
                backtrace(combine + '(', l_count - 1, r_count)
            # 添加右括号
            if l_count < r_count:
                backtrace(combine + ')', l_count, r_count - 1)

        if n == 0:
            return []
        result = []
        backtrace('', n, n)
        return result


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(3))
