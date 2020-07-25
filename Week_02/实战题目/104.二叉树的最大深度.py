#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
# 1、直接递归
        # if not root:
        #     return 0
        # else:
        #     left_depth=self.maxDepth(root.left)
        #     right_depth=self.maxDepth(root.right)
        #     return max(left_depth,right_depth)+1
# 2、迭代：国际站代码-好理解
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
        return depth
# @lc code=end

