#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 7:43 下午
# @Author  : liujiatian
# @File    : 最长回文子串.py

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
#  示例 2：
#
#  输入: "cbbd"
# 输出: "bb"
#
#  Related Topics 字符串 动态规划
#  👍 2541 👎 0


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        使用滑窗解决
        1. 依次设置滑窗大小为window=len(str),len(str)-1...1
        2. 左指针索引为0,右指针索引为w_size-1;如果是回文串,break 否则左右指针分别右移一位，直到右指针直到最后一个元素
        :param s:
        :return:
        '''
        if not s:
            return s
        len_s = len(s)
        window = len_s
        while window > 0:
            left = 0
            right = window - 1
            while right < len_s:
                sub_str = s[left:right + 1]
                if sub_str == sub_str[::-1]:
                    return sub_str
                left += 1
                right += 1
            window -= 1


if __name__ == '__main__':
    s = 'babad'
    print(Solution().longestPalindrome(s))
    s = "cbbd"
    print(Solution().longestPalindrome(s))
