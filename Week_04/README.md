学习笔记

dp=[[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]


递归的思路：


对于不好构建形状的状态矩阵，如三角最小路径和，状态矩阵可以用dict

对于需要填第一行和第一列状态数组的DP问题，如最小路径和、最短路径等，不需要循环三次，可以如下写代码（最小路径和）：
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m,n=len(grid),len(grid[0])    
        dp=grid[0][:]
        for i in range(m):
            for j in range(n):
                if i==j==0: continue
                elif i==0: dp[j]+=dp[j-1]
                elif j==0: dp[j]=dp[j]+grid[i][j] 
                else: dp[j]=min(dp[j-1],dp[j])+grid[i][j]   
        return dp[-1]