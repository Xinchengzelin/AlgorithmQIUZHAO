#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start

# 1、贪心
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]
        return res


# 2、动态规划-这类题的最典型的做法

        
# @lc code=end

