#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归
        if n<=2:
            return n
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-2]+dp[i-1]
        return dp[n-1]

        #动态规划
        # f1,f2,f3=0,0,1
        # for i in range(0,n):
        #     f1=f2
        #     f2=f3
        #     f3=f2+f1
        # return f3
        
# @lc code=end

