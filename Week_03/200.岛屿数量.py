#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
# 1、DFS 遍历整个数组，遇到1，把周围都改成0
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def clean_around(i,j):#清除相邻，还要清除相邻的相邻，需要递归
#             if i<0 or j<0 or i>=m or j>=n or grid[i][j]!="1":
#                 return
#             grid[i][j]=0
#             clean_around(i-1,j)
#             clean_around(i+1,j)
#             clean_around(i,j-1)
#             clean_around(i,j+1)
#         m=len(grid)
#         if m==0: return 0
#         n=len(grid[0])
#         res=0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]=="1":
#                     res+=1
#                     clean_around(i,j)
#         return res
# 2、BFS  81.86%
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        import collections
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    res+=1
                    grid[i][j]=='0'
                    deq=collections.deque([(i,j)])
                    while deq:
                        row,col=deq.popleft()#pop()结果也对的
                        for x,y in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y]=="1":
                                grid[x][y]="0"
                                deq.append((x,y))
        return res



# @lc code=end

