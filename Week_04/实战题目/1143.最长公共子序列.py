#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
# 1、动态规划 14.85%/61.31%
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if not text1 or not text2:
#             return 0
#         m=len(text1)
#         n=len(text2)
#         dp=[[0]*(n+1) for _ in range(m+1)]
#         for s1 in range(1,m+1):
#             for s2 in range(1,n+1):
#                 if text1[s1-1]==text2[s2-1]:
#                     dp[s1][s2]=dp[s1-1][s2-1]+1
#                 elif text1[s1-1]!=text2[s2-1]:
#                     dp[s1][s2]=max(dp[s1-1][s2],dp[s1][s2-1])
#         return dp[m][n]
# 2、递归-会超时
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if not text1 or not text2:
#             return 0
#         m=len(text1)
#         n=len(text2)
#         def LCS(s1,s2):#从字符串后到前
#             if s1 == -1 or s2 == -1:
#                 return 0
#             if text1[s1] == text2[s2]:
#                 return LCS(s1-1,s2-1)+1
#             else:
#                 return max(LCS(s1-1,s2),LCS(s1,s2-1))
#         return LCS(m-1,n-1)
# 3、记忆化递归 6.88%/5.72
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m,n=len(text1),len(text2)
        memo=[[-1]*n for _ in range(m)]
        def LCS(m,n):
            if m==-1 or n==-1:
                return 0
            if memo[m][n] != -1:#已经计算完了
                return memo[m][n]
            if text1[m]==text2[n]:
                memo[m][n]=LCS(m-1,n-1) + 1
            else:
                memo[m][n]=max(LCS(m-1,n),LCS(m,n-1))
            return memo[m][n]
        return LCS(m-1,n-1)

# @lc code=end

