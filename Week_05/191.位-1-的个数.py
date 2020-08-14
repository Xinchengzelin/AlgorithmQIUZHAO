#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start

# 1、for 循环  91.46%/51.01%
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             if n & 1 == 1:
#                 count += 1
#             n = n >> 1
#         return count
# 2、 x & (x - 1)  99.47%/40.9
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n > 0:
#             count += 1
#             n &= (n - 1)
#         return count

# 3、 调用系统函数  99.47%/40.9
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count("1")
            

        
# @lc code=end

