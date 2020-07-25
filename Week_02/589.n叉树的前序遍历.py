#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        # 1、递归法  64ms 71.89%
        # res=[]
        # def pre(root):
        #     if root:
        #         res.append(root.val)
        #         for i in root.children:
        #             pre(i)
        # pre(root)
        # return(res)
        # 2、迭代法 68ms 50.49%
        # 根节点先入栈，children节点反着入栈，出栈顺序就对了
        if not root:
            return []
        res,stack=[],[root]
        while stack:
            root=stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res
        
# @lc code=end

