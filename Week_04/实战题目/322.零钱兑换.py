#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
# 1、动态规划  14.56%/27.26%
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins: return -1
#         dp=[amount+1]*(amount+1) # dp[i] 表示金额为i需要最少的硬币
#         dp[0]=0# amount等于0时，0种兑换方式
#         for i in range(1,amount+1):
#             for j in range(len(coins)):
#                 if i-coins[j] >= 0:
#                     dp[i]=min(dp[i],dp[i-coins[j]]+1)
#         print(dp)
#         return dp[amount] if dp[amount]<=amount else -1# 硬币个数大于amount，即amount+1，返回-1
  
# 2、递归  直接递归-超时  增加lru_cache 74.5%/15.87%
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         import functools
#         @functools.lru_cache(None)
#         def helper(n):
#             if n == 0:
#                 return 0
#             return min((helper(n-c) if c <= n else float('inf') for c in coins))+1
#         res=helper(amount)
#         return res if res != float('inf')  else -1

# 3、BFS 94.82%/19.89%
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         from collections import deque
#         queue=deque([amount])
#         visited=set()# 未兑换的钱
#         level=0#树层数
#         while queue:
#             print(visited,queue)
#             n = len(queue)
#             for _ in range(n):
#                 tmp = queue.pop()
#                 if tmp == 0:
#                     return level
#                 for coin in coins:
#                     if tmp >= coin and (tmp - coin) not in visited:
#                         visited.add(tmp - coin)
#                         queue.appendleft(tmp-coin)#用append结果是不对的,需要先pop出大的未兑换的钱。
#             level+=1
#         return -1

# 4、DFS+贪心法 97.56%/94.68%
# 直接贪心不可行，有些coins不成倍数关系
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = float("inf")
        
        def dfs(i, num, amount):
            if amount == 0:
                self.res = min(self.res, num)
                return 
            for j in range(i, len(coins)):
                # 剩下的最大值都不够凑出来了
                if (self.res - num) * coins[j] < amount:
                    break
                if coins[j] > amount:
                    continue
                dfs(j, num + 1, amount - coins[j])
                
        for i in range(len(coins)):
            dfs(i, 0, amount)
            
        return self.res if self.res != float("inf") else -1
        
# @lc code=end

