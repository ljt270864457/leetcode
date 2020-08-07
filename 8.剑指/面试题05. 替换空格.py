#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 5:58 PM
# @Author  : liujiatian
# @File    : 面试题05. 替换空格.py

'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000
'''


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        result = []
        for _ in s:
            if _ != ' ':
                result.append(_)
            else:
                result.append('%20')
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace("We are happy."))
