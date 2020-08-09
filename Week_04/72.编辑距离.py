#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
# 1、DP  47.69%/36.44%
# dp[i][j] 表示 A 的前 i 个字母和 B 的前 j 个字母之间的编辑距离
# 若 A 和 B 的最后一个字母相同：
# D[i][j]=min(D[i][j−1]+1,D[i−1][j]+1,D[i−1][j−1])
# =1+min(D[i][j−1],D[i−1][j],D[i−1][j−1]−1)
# 若 A 和 B 的最后一个字母不同：
# D[i][j]=1+min(D[i][j−1],D[i−1][j],D[i−1][j−1])
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 :
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]-1) + 1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        return dp[-1][-1]
# @lc code=end

