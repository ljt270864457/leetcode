#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 10:00 PM
# @Author  : liujiatian
# @File    : 4.深度优先遍历.py


def dfs(graph, cur):
    '''
    通过递归的方式进行深度优先遍历
    :param graph:
    :param root:
    :return:
    '''
    print(cur)

    neighbors = graph.get(cur)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.append(neighbor)
            dfs(graph, neighbor)


if __name__ == '__main__':
    '''
    图片地址https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/869/
    '''
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': [],
        'F': ['G'],
        'G': []
    }
    visited = []
    dfs(graph, 'A')

