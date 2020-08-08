#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
# 1、DP-新状态数组 56.31%/32.3%
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp=nums#可以这么赋值的DP题目，都可以在原list修改
#         for i in range(1,len(nums)):
#             dp[i]=max(dp[i-1]+nums[i],nums[i])
#         return max(dp)
    
# 2、DP-就地修改 56.31%/57.45%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)

# 3、暴力法-超时
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum=float('-inf')
#         for i in range(len(nums)):
#             s=0
#             for j in range(i,len(nums)):
#                 s+=nums[j]
#                 if s>max_sum:
#                     max_sum=s
#         return max_sum

# @lc code=end

