#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 7:10 下午
# @Author  : liujiatian
# @File    : 6.比较含退格的字符串.py

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        '''
        LeetCode844
        给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

        注意：如果对空文本输入退格字符，文本继续为空。

        示例 1：

        输入：S = "ab#c", T = "ad#c"
        输出：true
        解释：S 和 T 都会变成 “ac”。
        示例 2：

        输入：S = "ab##", T = "c#d#"
        输出：true
        解释：S 和 T 都会变成 “”。
        示例 3：

        输入：S = "a##c", T = "#a#c"
        输出：true
        解释：S 和 T 都会变成 “c”。
        示例 4：

        输入：S = "a#c", T = "b"
        输出：false
        解释：S 会变成 “c”，但 T 仍然是 “b”。
        :param S:
        :param T:
        :return:
        '''
        stack1 = []
        stack2 = []
        for _ in S:
            if _ != '#':
                stack1.append(_)
            elif stack1:
                stack1.pop()

        for _ in T:
            if _ != '#':
                stack2.append(_)
            elif stack2:
                stack2.pop()
        return stack1 == stack2
