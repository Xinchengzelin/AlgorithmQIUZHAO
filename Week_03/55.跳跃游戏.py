#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# 1、贪心算法 99.26%
# @lc code=start
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if not nums:
#             return False
#         endReachable=len(nums)-1
#         for i in range(len(nums)-1,-1,-1):
#             if nums[i]+i >= endReachable:
#                 endReachable=i
#         return endReachable==0
# 2、每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新 35.42%
class Solution: 
    def canJump(self, nums: List[int]) -> bool:
        farest=0
        for i in range(len(nums)):
            if i > farest: return False#这个必须有
            farest=max(farest,i+nums[i])
        # return farest >= len(nums)-1 #也可以
        return True
# @lc code=end

