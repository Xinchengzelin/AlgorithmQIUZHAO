#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
# class Solution:
#     def climbStairs(self, n: int) -> int:
        #1、非递归-
        # if n<=2:
        #     return n
        # dp=[0]*n
        # dp[0]=1
        # dp[1]=2
        # for i in range(2,n):
        #     dp[i]=dp[i-2]+dp[i-1]
        # return dp[n-1]

        # 2、尾递归——直接递归超时
        # def fib(n,a,b):
        #     if n<=1:
        #         return b
        #     return fib(n-1,b,a+b)
        # return fib(n,1,1)

        #3、动态规划
        # f1,f2,f3=0,0,1
        # for i in range(0,n):
        #     f1=f2
        #     f2=f3
        #     f3=f2+f1
        # return f3
# 4、使用对象-类似于非递归
# class Fib():
#     def __init__(self):
#         self.nums=nums=[1,2,]
#         for i in range(2,10000):
#             nums.append(nums[i-1]+nums[i-2])
# class Solution:
#     fib=Fib()
#     def climbStairs(self, n: int) -> int:
#         return self.fib.nums[n-1]
    
        
# @lc code=end

