#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
# 1、DP  81.78%/59.41
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         if not grid: return 0
#         m,n=len(grid),len(grid[0])
#         for i in range(1,m):
#             grid[i][0]+=grid[i-1][0]
#         for j in range(1,n):
#             grid[0][j]+=grid[0][j-1]
#         for i in range(1,m):
#             for j in range(1,n):
#                 grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
#         # print(grid)
#         return grid[-1][-1]

# 2、DP-优化代码  92.98%/63.17%
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         if not grid: return 0
#         m,n=len(grid),len(grid[0])    
#         for i in range(m):
#             for j in range(n):
#                 if i==j==0: continue
#                 elif i==0: grid[i][j]+=grid[i][j-1] 
#                 elif j==0: grid[i][j]+=grid[i-1][j]
#                 else: grid[i][j]+=min(grid[i-1][j],grid[i][j-1])   
#         return grid[-1][-1]

# 3、DP-优化空间  81.78%/95.93%
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m,n=len(grid),len(grid[0])    
        dp=grid[0][:]
        for i in range(m):
            for j in range(n):
                if i==j==0: continue
                elif i==0: dp[j]+=dp[j-1]
                elif j==0: dp[j]=dp[j]+grid[i][j] 
                else: dp[j]=min(dp[j-1],dp[j])+grid[i][j]   
        return dp[-1]
# @lc code=end

