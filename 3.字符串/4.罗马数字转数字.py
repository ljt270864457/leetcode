#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 7:01 下午
# @Author  : liujiatian
# @File    : 4.罗马数字转数字.py

class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        LeetCode 13 罗马数字转数字
        :param s:
        :return:
        '''
        # 基于辅助栈的做法，如果下一个元素比当前元素小，压栈；否则计算当前逆序的结果
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        stack = []
        for i in s:
            if not stack or mapping[i] <= mapping[stack[-1]]:
                stack.append(i)
                continue

            tmp = 0
            while stack and mapping[i] > mapping[stack[-1]]:
                tmp = mapping[stack.pop()]
            result += (mapping[i] - tmp)

        for _ in stack:
            result += mapping[_]
        return result
    # def romanToInt(self, s: str) -> int:
    #     '''
    #     多看一位，如果下一位比上一位大，那么小的值变成负值
    #     '''
    #     result = 0
    #     mapping = {
    #         'I': 1,
    #         'V': 5,
    #         'X': 10,
    #         'L': 50,
    #         'C': 100,
    #         'D': 500,
    #         'M': 1000
    #     }
    #     for index, value in enumerate(s):
    #         if index == len(s) - 1:
    #             result += mapping[value]
    #             return result
    #         if mapping[value] < mapping[s[index + 1]]:
    #             result -= mapping[value]
    #         else:
    #             result += mapping[value]
    #     return result

if __name__ == '__main__':
    print(Solution().romanToInt('XIII'))