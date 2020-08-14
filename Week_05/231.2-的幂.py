#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
# 1、直接判断 40.21%/62.14%
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return bin(n).count('1') == 1 if n > 0 else False

# 2、利用 n & (n-1) 94.39%/5.04%
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and (n & (n -1)) == 0
# @lc code=end

