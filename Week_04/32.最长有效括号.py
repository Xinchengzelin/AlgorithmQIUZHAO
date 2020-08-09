#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
# 1、DP  52.47%/94.66%
# dp[i] 以s[i]结尾最长子串长度
# s[i]=="("s[i-1]==")":dp[i]=dp[i-2]+2
# s[i]==s[i-1] 且 s[i-dp[i-1]-1]=="(" :dp[i]=dp[i-2]+2+dp[i-dp[i-1]-2](注意i-dp[i-1]-2是否越界)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) == 1: return 0
        m = len(s)
        dp = [0]*m
        for i in range(1,m):
            if i == 1:
                if s[i] == ")" and s[i-1] == "(":
                    dp[i] = 2
            else:
                if s[i] == ")" and s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif s[i] == s[i - 1] == ")" and s[i-dp[i-1] - 1] == "(":
                    if i-dp[i-1]-1== 0: #dp[i-dp[i-1]-2] == dp[-1]
                        dp[i] = dp[i-1] + 2
                    elif i-dp[i-1] - 1 > 0:
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        return max(dp)



# @lc code=end

