#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
# 1、动态规划  50.76%
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp=[[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        # dp=[[1 for x in range(n)] for x in range(m)]#直接定义全1矩阵也是没问题的
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j]=dp[i-1][j]+dp[i][j-1]
#         return dp[m-1][n-1]

# 2、排列组合法 74.17%
# 只有向右走n-1步，向下走m-1步即可，不同的走法在于第几步向下，第几步向右；C(n-1,m+n-2)或C(m-1,m+n-2)相等
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        return int(math.factorial(n+m-2)/math.factorial(m-1)/math.factorial(n-1))
# @lc code=end

