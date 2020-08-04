#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 4:56 下午
# @Author  : liujiatian
# @File    : 5.有效的括号.py

'''
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        '''
        如果是左括号，入栈;如果是右括号，出栈匹配
        '''
        stack = []
        left = ['{', '(', '[']

        # 记录栈顶元素
        for _ in s:
            if _ in left:
                stack.append(_)
            else:
                if not stack:
                    return False

                # 栈顶元素
                tmp = stack.pop()
                if (tmp == '[' and _ != ']') or (tmp == '{' and _ != '}') or (tmp == '(' and _ != ')'):
                    return False
        return True if not stack else False


if __name__ == '__main__':
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("(]") == False
    assert Solution().isValid("()[]") == True
    assert Solution().isValid("[") == False
