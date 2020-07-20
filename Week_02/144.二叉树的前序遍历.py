#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法 44 ms
        # def preorder(root):
        #     if root:
        #         res.append(root.val)
        #         preorder(root.left)
        #         preorder(root.right)
        # res=[]
        # preorder(root)
        # return res

        # 迭代法 44 ms
        res=[]
        stack=[]
        cur=root
        while stack or cur:
            while cur:#所有父节点进结果，将左节点压入栈
                res.append(cur.val)
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            cur=cur.right
        return res           
# @lc code=end

