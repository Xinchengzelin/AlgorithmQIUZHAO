#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
# 1、递归-其实是DFS，生成括号可以形成一颗状态树
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         ans=[]
#         def generate(left=0,right=0,s=""):
#             if (left==n and right==n):
#                 ans.append(s)
#                 return 
#             if left<n:#加条件就是回溯？
#                 generate(left+1,right,s+'(')
#             if right<left:
#                 generate(left,right+1,s+')')
#         generate(0,0,"")
#         return ans
# 2、自己构造一个栈
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[("(",1,0)]
        res=[]
        while stack:
            s,l,r=stack.pop()
            if r>l or r>n or l>n:
                continue
            if r==n and l==n:
                res.append(s)
                continue
            if l<n:
                stack.append((s+"(",l+1,r))
            if l>r:
                stack.append((s+")",l,r+1))
        return res
# @lc code=end

