#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
# 1、递归  -60ms
        if not root:
            return 0
        d=[self.minDepth(root.left),self.minDepth(root.right)]
        return (min(d) or max(d))+1
# 2、递归-精简版 52ms
        # if not root:
        #     return 0
        # d=list(map(self.minDepth,(root.left,root.right)))#递归的另一种方法
        # return 1+(min(d) or max(d))#精妙，正常返回最小值，0的话返回最大值
# @lc code=end

