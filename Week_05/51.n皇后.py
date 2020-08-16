#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
# 1、简单递归 86.24%/75.25%  不用_generate_res函数93.47%/75.96%
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         self.res = []
#         self.col = set()#存放col能攻击的位置
#         self.pie = set()
#         self.na = set()
#         self.DFS(n,0,[])
#         # print(self.res)
#         return  [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in self.res]
#         # return self._generate_res(n)
#     def DFS(self,n,row,cur_state):
#         if row >= n:
#             self.res.append(cur_state)
#             return
#         for col in range(n):
#             if col in self.col or (row + col) in self.pie or (row - col) in self.na:
#                 continue #go die
#             self.col.add(col)
#             self.pie.add(row + col)
#             self.na.add(row - col)
#             self.DFS(n, row+1 ,cur_state+[col])#cur_state是存放每行把皇后放在第几列

#             self.col.remove(col)
#             self.pie.remove(row + col)
#             self.na.remove(row - col)
#     def _generate_res(self,n):
#         board = []
#         for result in self.res:
#             b = []
#             for i in result:
#                 b.append("."*i + "Q" + "."*(n-i-1) )
#             board.append(b)
#         # 不引入b，可以这么写
#         # return [board[i:n+i] for i in range(1,len(board),n)
#         return board
# 2、国际站简单代码 86.24%/55.19%
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         def DFS(quees,xy_diff,xy_sum):
#             row = len(quees)
#             if row == n:
#                 res.append(quees)
#             for col in range(n):
#                 if col not in quees and row-col not in xy_diff and row+col not in xy_sum:
#                     DFS(quees + [col],xy_diff + [row - col],xy_sum + [row +col])
#         res = []
#         DFS([],[],[])
#         return [["." * i +"Q" + "." * (n-i-1) for i in sol] for sol in res]



# @lc code=end

