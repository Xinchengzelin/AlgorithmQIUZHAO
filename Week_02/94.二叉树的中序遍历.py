#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法  时间复杂度：O(n)，空间复杂度O(h)-树的高度  40 ms
        # res=[]
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         res.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        # return res

        # 迭代法  时间复杂度：O(n) 空间复杂度：O(n) 48 ms
        res=[]
        stack=[]
        cur=root
        while stack or cur:
            while cur:#压入所有左子树的左节点
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res

        # 标记迭代法，需要双倍存储空间
        res=[]
        stack=[(0,root)]
        while stack:
            flag,cur=stack.pop()
            if not cur:
                continue
            if flag==0:
                stack.append((0,right))
                stack.append((1,cur))
                stack.append((0,left))
            else:
                res.append(cur.val)
        return res          
# @lc code=end

