#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
# 1、位运算法 98.73%/84.69%
# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         if n < 1:
#             return 0
#         self.cnt = 0
#         self.DFS(n,0,0,0,0)
#         return self.cnt
#     def DFS(self,n,row,col,pie,na):
#         if row >= n:
#             self.cnt += 1
#             return
#         bits = (~(col | pie | na)) & ((1 << n) -1) #得到当前所有的空位
#         while bits:
#             p = bits & (-bits) #取到最低位的1
#             bits = bits & (bits-1) #最低位的1清零，表示在p位置上放入皇后
#             self.DFS(n,row + 1,col | p, (pie | p)<<1, (na|p)>>1)

# 2、递归 72.63%/40.48%
# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         if n < 1 : return 0
#         self.cnt = 0
#         self.col = set()
#         self.pie = set()
#         self.na = set()
#         self.DFS(n,0)
#         return self.cnt
#     def DFS(self,n,row):
#         if row >= n:
#             self.cnt += 1
#             return
#         for col in range(n):
#             if col in self.col or (row + col)in self.pie or (row - col) in self.na:
#                 continue
#             self.col.add(col)
#             self.pie.add(row + col)
#             self.na.add(row - col)
#             self.DFS(n,row + 1)

#             self.col.remove(col)
#             self.pie.remove(row + col)
#             self.na.remove(row - col)           
# 3、精简递归 72.63%/35.71%
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1: return 0
        self.cnt = 0
        self.DFS(n,0,[],[],[])
        return self.cnt
    def DFS(self,n,row,cols,pie,na):
        if row >= n:
            self.cnt += 1
            return
        for col in range(n):
            if col not in cols and (row + col) not in pie and (row - col) not in na:
                self.DFS(n,row + 1,cols + [col], pie + [row + col],na + [row -col])

# @lc code=end

