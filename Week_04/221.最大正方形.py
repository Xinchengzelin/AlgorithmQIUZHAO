#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
# 1、动态规划  70.97%/6.02%
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         m,n=len(matrix),len(matrix[0])
#         dp=[[0]*n for _ in range(m)]
#         for i in range(0,m):
#             for j in range(0,n):
#                 if i==0 or j==0:
#                     dp[i][j]=int(matrix[i][j])#matrix中间是字符，要转换成int
#                 else:
#                     if matrix[i][j]=="0":
#                         dp[i][j]=0
#                     else:
#                         dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
#         print(dp)
#         return max([max(row) for row in dp])**2#二维list求最大值

# 2、动态规划-就地  50.33%/69.05%
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m,n=len(matrix),len(matrix[0])
        # dp=[[0]*n for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 or j==0:
                    matrix[i][j]=int(matrix[i][j])#matrix中间是字符，要转换成int
                else:
                    if matrix[i][j]=="0":
                        matrix[i][j]=0
                    else:
                        matrix[i][j]=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+1
        return max([max(row) for row in matrix])**2#二维list求最大值

# @lc code=end

