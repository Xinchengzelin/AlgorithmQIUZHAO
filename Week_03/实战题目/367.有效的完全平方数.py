#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
# 1、二分法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=0,num
        while left <= right:
            mid=(left+right)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                right=mid-1
            else:
                left=mid+1
        return False


# 2、位运算、动态规划
# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:

# @lc code=end

