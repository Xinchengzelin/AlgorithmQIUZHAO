#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
# 1、直接递归-超时
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         def helper(i,j):
#             if i==len(triangle):
#                 return 0
#             return min(helper(i+1,j),helper(i+1,j+1))+triangle[i][j]
#         return helper(0,0)
# 2、记忆化递归 50.48%/5.19%
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache=dict()
        def helper(i,j):
            if i==len(triangle):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            res = min(helper(i+1,j),helper(i+1,j+1))+triangle[i][j]
            cache[(i,j)]=res
            return res
        return helper(0,0)

# 3、DP-状态数组是二维  88.6%/21.42%
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         dp=triangle
#         for i in range(len(triangle)-2,-1,-1):#从下到上进行循环，最下面一层无需循环，已经初始化了
#             for j in range(len(triangle[i])):
#                 dp[i][j]+=min(dp[i+1][j],dp[i+1][j+1])
#         # print(dp)
#         # print(triangle)
#         return dp[0][0]
# 4、DP-状态数组是一维  99%/80.95%
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m=len(triangle)
#         dp=triangle[m-1]
#         for i in range(m-2,-1,-1):
#             for j in range(len(triangle[i])):
#                 dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
#         return dp[0]

# @lc code=end

