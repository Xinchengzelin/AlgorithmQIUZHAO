#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
# 1、动态规划-in place 80.43%/69.93%
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        if m==0: return 0
        n=len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]#没这句，结果就不对
        for j in range(1,n):
            obstacleGrid[0][j]=obstacleGrid[0][j-1]*(1-obstacleGrid[0][j])#巧妙的避免了if  else
        for i in range(1,m):
            obstacleGrid[i][0]=obstacleGrid[i-1][0]*(1-obstacleGrid[i][0])
        for i in range(1,m):
            for j in range(1,n):
                obstacleGrid[i][j]=(obstacleGrid[i-1][j]+obstacleGrid[i][j-1])*(1-obstacleGrid[i][j])
        # print(obstacleGrid)
        return obstacleGrid[-1][-1]


# @lc code=end

