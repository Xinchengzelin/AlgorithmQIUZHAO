#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
# 1、利用n&(n-1)直接计数9.19% /58.67%
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         res = []
#         for i in range(0,num+1):
#             cnt = 0
#             while i:
#                 cnt += 1
#                 i = i & (i-1)
#             res.append(cnt)
#         return res
# 2、动态规划 i为奇数：dp[i]=dp[i-1]+1,偶数：dp[i]=dp[i // 2] 74.02% /83.82%
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         dp = [0] * (num+1)
#         for i in range(0,num+1):
#             if i == 0:
#                 dp[i] = 0
#             elif i & 1 == 0: #i为偶数,i和i左移1位的“1”的个数相等
#                 dp[i]=dp[i // 2]
#             elif i & 1 == 1: #i为奇数
#                 dp[i] = dp[i-1] + 1
#         return dp
# 3、动态规划 奇偶整理成1条：dp[i]=dp[i//2]+(i % 2)=dp[i//2]+(i & 1), 74.02% /78.17%
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         dp = [0] * (num+1)
#         for i in range(1,num + 1):
#             dp[i] = dp[i >> 1] + (i & 1)
#         return dp
# 4、国际版（理解不了） 62.51%/79.53%
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        print(res)
        return res[:num+1]



        
# @lc code=end

