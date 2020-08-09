#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start

# 1、DP 87.81% / 20.11%
# a[i]:前i个房子可以偷到的最大值  1：偷   0：不偷
# a[i][0]=max(a[i-1][1],a[i-1][0]+nums[i])
# a[i][1]=a[i-1][0]+nums[i]
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums: return 0
#         m = len(nums)
#         dp = [[0,0] for _ in range(m)]
#         for i in range(m):
#             if i == 0:
#                 dp[i][0] = 0
#                 dp[i][1] = nums[i]
#             else:
#                 dp[i][0] = max(dp[i-1][1],dp[i-1][0])
#                 dp[i][1] = dp[i-1][0]+nums[i]
#         return max(dp[-1])

# 2、DP 70.17% / 29.11%
# a[i]:前i个房子可偷到的最大值，第i个房子可以偷，可以不偷
# a[i]=max(a[i-1],a[i-2]+nums[i])
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums: return 0
#         m = len(nums)
#         dp=[0]*m
#         for i in range(m):
#             if i == 0:
#                 dp[i] = nums[i]
#             elif i == 1:
#                 dp[i] = max(dp[i-1],nums[i])
#             else:
#                 dp[i] = max(dp[i-1],dp[i-2] + nums[i])
#         return dp[-1]

# 3、DP-优化状态数组长度 70.17% / 20.89%
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        prevmax,curmax=0,0
        for i in range(len(nums)):
            tmp = curmax
            curmax = max(prevmax+nums[i],curmax)
            prevmax = tmp
        return curmax
 
# @lc code=end

