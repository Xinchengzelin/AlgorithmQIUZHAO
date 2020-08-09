#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
# 1、DP 51.05%/31.47%
# 构造二维状态数组：https://leetcode-cn.com/problems/palindromic-substrings/solution/647-hui-wen-zi-chuan-dong-tai-gui-hua-fang-shi-qiu/
# dp[i][j]==1,表示s[i:j+1]是回文子串，dp[i][j]=dp[i+1][j-1]
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         if not s: return 0
#         m = len(s)
#         dp=[[0]*m for _ in range(m)]
#         for i in range(m):
#             dp[i][i]=1
#         for i in range(m-1,-1,-1):#右下角开始，从左到右
#             for j in range(m-1,i,-1):
#                 if s[i] == s[j]:
#                     if j-i == 1:#’bb'这种测试实例
#                         dp[i][j] = 1
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
#         return sum([sum(row) for row in dp])

# 2、DP  51.77%/36.21%
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        m = len(s)
        dp=[[0]*m for _ in range(m)]
        for i in range(m-1,-1,-1):#右下角开始，从左到右
            for j in range(i,m):
                if s[i] == s[j]:
                    if j-i <= 1:#’bb'这种测试实例
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
        return sum([sum(row) for row in dp])        
# @lc code=end

