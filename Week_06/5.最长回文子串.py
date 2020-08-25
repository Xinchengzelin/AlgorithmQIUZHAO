#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
# 1、中间向两边扩张法 为什么maxlen访问有问题？
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expandPalindrome(s,l,r):
#             while l>=0 and r < len(s) and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             if maxlen < r - l - 1: #更新为大的maxlen  #为什么这里会报错？？
#                 maxlen = r - l - 1
#                 lo = l + 1
#         if len(s) < 2 : return s
#         lo = 0
        # maxlen = 0
        # for i in range(len(s)):
        #     expandPalindrome(s,i,i)
        #     expandPalindrome(s,i,i+1)
        # return s[lo:lo+maxlen+1]
# 1、中间向两边扩张法 82.84%/83.18%
# class Solution:
#     def expandPalindrome(self,s,l,r):
#         while l>=0 and r < len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
#         return l+1,r-1
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2 : return s
#         start,end = 0,0
#         for i in range(len(s)):
#             left1,right1 = self.expandPalindrome(s,i,i) #baab这种情况
#             left2,right2 =self.expandPalindrome(s,i,i+1) # bab这种情况
#             if right1 - left1 > end - start:
#                 start,end = left1,right1
#             if right2 - left2 > end - start:
#                 start,end = left2,right2
#         return s[start:end+1]
# 2、动态规划 49.13%/45.09%
# dp[i][j] =1 表示 s[i:j+1]是回文串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        dp = [[False]*n for _ in range(n)]
        for i in range (n-1,-1,-1):
            for j in range(i,n):
                # dp[i][j] = (s[i] == s[j]) and ((j -i < 2) or dp[i+1][j-1])#简单代码
                if s[i] == s[j]:
                    dp[i][j] = (j - i < 2)  or dp[i+1][j-1]#j-i < 2 是考虑a和aa两种情况
                else:
                    dp[i][j] = 0
                if dp[i][j] and  (j - i + 1) > len(res):
                    res = s[i:j+1]
        # print(dp)
        return res


# @lc code=end

