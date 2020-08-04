#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 8:57 PM
# @Author  : liujiatian
# @File    : 2.bfs.py

def bfs(graph, root):
    '''
    广度优先遍历
    1. add root in queue,visited
    2. while True:
        if queue is empty:
            :return queue

        3. pop node as cur_node and get node leaf_list

        for leaf in leaf_list:
            if leaf not in visited:
                add leaf to queue and visited
    :param graph 图
    :param root:根节点
    :target 目标节点
    :return:
    '''
    visited = [root]
    queue = [root]

    while queue:
        cur_node = queue.pop(0)
        leaf_list = graph[cur_node]
        for leaf in leaf_list:
            if leaf not in visited:
                visited.append(leaf)
                queue.append(leaf)
    return visited


def bfs_path(graph, root, target):
    '''
    bfs 获取所有路径
    queue中存储的都是上一次的path，如果leaf==target 将path+leaf加入到path_list中
    :param graph:
    :param root:
    :param target:
    :return:
    '''
    path_list = []
    queue = [root]

    while True:
        if not queue:
            return path_list

        path = queue.pop()
        cur_node = path[-1]

        leaf_list = graph[cur_node]
        for leaf in leaf_list:
            new_path = list(path)
            new_path.append(leaf)
            queue.append(new_path)
            if leaf == target:
                path_list.append(new_path)


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
    print(bfs(graph, 'A'))
    # print(bfs_path(graph, 'A', 'G'))
