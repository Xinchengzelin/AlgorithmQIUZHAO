#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
# 1、递归-构造一个函数去递归 88.98ms
        # def helper(node,lower=float('-inf'),upper=float('inf')):
        #     if not node:
        #         return True
        #     val = node.val
        #     if val <= lower or val >= upper:
        #         return False
        #     if not helper(node.left,lower,val):
        #         return False
        #     if not helper(node.right,val,upper):
        #         return False
        #     return True
        # return helper(root)
# 2、递归-更pythonic   52ms
        # def BFS(node,left,right):
        #     if not node:
        #         return True
        #     if left < node.val < right:
        #         return BFS(node.left,left,node.val) and BFS(node.right,node.val,right)
        #     else:
        #         return False
        # return BFS(root,-float('inf'),float('inf'))
# 3、中序遍历 52ms
class Solution:
    pre=-float('inf')
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:#注意=
            return False
        self.pre=root.val
        return self.isValidBST(root.right)

# @lc code=end

