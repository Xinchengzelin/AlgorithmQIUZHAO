#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1、BFS
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         queue,res=[root],[]
#         while queue:
#             level=[]
#             queue_next=[]#while下一次循环的queue
#             for item in queue:
#                 level.append(item.val)
#                 if item.left:
#                     queue_next.append(item.left)#不是栈，因此left不需要在right后
#                 if item.right:
#                     queue_next.append(item.right)
#             res.append(level)
#             queue=queue_next
#         return res
# 2、DFS
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res=[]
#         def helper(node,level):
#             if not node:
#                 return
#             if len(res)==level:#一层访问完，res中增加一个list，存放下一层的元素
#                 res.append([])
#             res[level].append(node.val)
#             if node.left:
#                 helper(node.left,level+1)
#             if node.right:
#                 helper(node.right,level+1)
#         helper(root,0)    
#         return res
# 3、BFS精简代码-44ms
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res,level=[],[root]#level
        while root and level:
            res.append([node.val for node in level])
            level=[kid for node in level for kid in (node.left,node.right) if kid]
        return res

# @lc code=end

