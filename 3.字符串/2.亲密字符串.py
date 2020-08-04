#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 6:28 PM
# @Author  : liujiatian
# @File    : 2.亲密字符串.py

'''
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false

输入： A = "ab", B = "ba"
输出： true

输入： A = "ab", B = "ab"
输出： false

输入： A = "aa", B = "aa"
输出： true

输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true

输入： A = "", B = "aa"
输出： false
'''


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        '''
        解题思路：
        1. 如果A 或 B为空 或A B长度不一致 return False
        2. 如果A和B相等，只要有一个元素出现的次数大于2即可 A=B='avcea'
        3. 遍历字符串 如果A B的第i个字符不一致，将其存储到一个列表 例如[(A,B),(B,A)]
        4. 列表去重，如果去重后的元素等于2 且两个元素交换位置后结果一致 return True
        :param A:
        :param B:
        :return:
        '''
        if not A or not B or len(A) != len(B):
            return False

        if A == B and len(A) > len(set(A)):
            return True

        s = set([(a, b) for a, b in zip(A, B) if a != b])
        return len(s) == 2 and s[0] == s[1][::-1]


s = Solution()
assert s.buddyStrings("ab", "ba") == True
assert s.buddyStrings("ab", "ab") == False
assert s.buddyStrings("aa", "aa") == True
assert s.buddyStrings("aaaaaaabc", "aaaaaaacb") == True
assert s.buddyStrings("", "aa") == False
assert s.buddyStrings("abab", "abab") == True
