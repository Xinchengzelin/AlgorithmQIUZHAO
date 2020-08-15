#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#
# 二进制颠倒要考虑前导零
# @lc code=start
# 1、利用内置函数int和bin。将n转换为二进制，把0b之后的值（在前面加"0"）反转，再转换为整数。
class Solution: # 80.01%/31.03%
    def reverseBits(self, n: int) -> int:
        return int("0b"+("0"*32+bin(n)[2:])[-32:][::-1], base = 2)
        # "0"*32 前面补32个0，所以取[-32:]才可以

# 2、逐位颠倒 59.32%/64.25%
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         l,r = 0,31 # r是移位的个数
#         while n:
#             l += (n & 1) << r #原来第0位左移r位，相当于*2^r
#             n = n>>1
#             r -= 1
#         return l

# 3、取模求和 16.7%/31.03%
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for _ in range(32):
#             res = (res << 1) + (n & 1)# res << 1相当于res*2
#             n = n >> 1
#         return res
# @lc code=end

