#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 6:41 PM
# @Author  : liujiatian
# @File    : 3.翻转字符串.py

'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([a[::-1] for a in s.split()])


if __name__ == '__main__':
    s = Solution()
    assert s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
