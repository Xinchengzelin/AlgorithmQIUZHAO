#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 1、递归 56ms 94.69%
        # res=[]
        # def back(root):
        #     if root:
        #         for ch in root.children:
        #             back(ch)
        #         res.append(root.val)
        # back(root)
        # return res
        # 2、迭代法 56ms 94.69%
        # 入栈顺序：根节点先入栈，children节点依次入栈，遍历结束后反转结果
        if not root:
            return []
        stack,res=[root],[]
        while stack:
            root=stack.pop()
            res.append(root.val)
            stack.extend(root.children)
        return res[::-1]
# @lc code=end

