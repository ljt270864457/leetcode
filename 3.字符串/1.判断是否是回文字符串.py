#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 10:54 PM
# @Author  : liujiatian
# @File    : 1.判断是否是回文字符串.py

class Solution:
    '''
    判断字符串是否是回文字符串
    正读反读都一样的字符串 忽略大小写及特殊标点
    '''

    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = ''.join([x.lower() for x in s if x.isalnum()])
        return s[::-1] == s


if __name__ == '__main__':
    str1 = "race a car"

    s = Solution()
    print(s.isPalindrome(str1))
