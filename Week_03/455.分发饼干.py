#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start

# 1、贪心法 64.43%
# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         g.sort()
#         s.sort()
#         i,j,res=0,0,0
#         while i < len(g) and j < len(s):
#             if g[i]<=s[j]:
#                 res+=1
#                 i+=1
#                 j+=1
#             else:
#                 j+=1
#         return res
# 2、贪心法-精简代码  77.23%
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int: 
        g.sort()
        s.sort()
        i,j=0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
            j+=1
        return i

# @lc code=end

