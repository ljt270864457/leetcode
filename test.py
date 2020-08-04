#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 1:18 下午
# @Author  : liujiatian
# @File    : test.py

def func(str1):
    '''
    字符串排序
    :param str1:
    :return:
    '''

    if not str1:
        return
    result = ''
    # 构建词频hash
    tmp_hash = {}
    for _ in str1:
        if _ not in tmp_hash:
            tmp_hash[_] = 1
        else:
            tmp_hash[_] = tmp_hash[_] + 1
    sorted_char_list = sorted(tmp_hash,key=lambda x:x.values)
    print(sorted_char_list)
    for s in sorted_char_list:
        result += s * tmp_hash[s]
    return result


if __name__ == '__main__':
    # print(func('tree'))
    print(func('treet'))
