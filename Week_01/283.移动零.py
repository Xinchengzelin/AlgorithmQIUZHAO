#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in nums:
            if i != 0:
                nums[j]=nums[i]
                if i != j:
                    nums[i]=0
                j+=1
# @lc code=end

