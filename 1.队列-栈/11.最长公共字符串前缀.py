#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 7:54 下午
# @Author  : liujiatian
# @File    : 11.最长公共字符串前缀.py


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        '''
        LeetCode14.编写一个函数来查找字符串数组中的最长公共前缀。

        如果不存在公共前缀，返回空字符串 ""。

        示例 1:

        输入: ["flower","flow","flight"]
        输出: "fl"
        示例 2:

        输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀。
        说明:

        解法：之比较最长的和最短的字符串即可
        '''
        if not strs:
            return ""

        min_str = min(strs)
        max_str = max(strs)

        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str


if __name__ == '__main__':
    strs = ['a']
    print(Solution().longestCommonPrefix(strs))
