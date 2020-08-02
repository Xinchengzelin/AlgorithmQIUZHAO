#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start

# 1、转换成一维矩阵再二分 78.26%
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m=len(matrix)
#         if m==0: return False
#         n= len(matrix[0])

#         lis=[]
#         for l in matrix:
#             lis.extend(l)
        
#         l,r=0,m*n-1
#         while l<=r:
#             mid=(l+r)//2
#             if lis[mid]==target:
#                 return True
#             elif lis[mid] < target:
#                 l=mid+1
#             else:
#                 r=mid-1
#         return False

# 2、直接二分法 100%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        if m==0: return False
        n= len(matrix[0])
        l,r=0,m*n-1
        while l <= r:
            mid=(l+r)//2
            i= mid // n #!!
            j= mid % n
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                r=mid-1
            else:
                l=mid+1
        return False


# @lc code=end

