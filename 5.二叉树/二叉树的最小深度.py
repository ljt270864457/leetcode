# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        111. 二叉树的最小深度
        给定一个二叉树，找出其最小深度。

        最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

        说明: 叶子节点是指没有子节点的节点。

        示例:

        给定二叉树 [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回它的最小深度  2.
        '''
        if not root:
            return 0
        # 计算左节点深度
        left_depth = self.minDepth(root.left)
        # 计算右节点深度
        right_depth = self.minDepth(root.right)
        # 三种情况 1.root左右都有节点 那么取左右子树最小的节点 2.如果只有左子树或者只有右子树，那么取左子树或者右子树的深度 3.如果左右都没有 返回0
        root_depth = min(left_depth, right_depth) or left_depth or right_depth
        return root_depth + 1
