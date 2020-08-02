#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
# 1、袖珍计算器法 52.85%
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x==0:
#             return 0
#         ans=int(math.exp(0.5*math.log(x)))
#         return ans+1 if (ans+1)*(ans+1)<=x else ans
        # 浮点数在计算机存储有误差，很大的数计算时可能有误差，所以结果可能为ans+1


# 2、二分法 52.84%
class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,x
        while left < right:
            mid=(right+left+1)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left=mid
            else:
                right=mid-1
        return right

# 3、二分法 84.33%
# x>=4时，sqrt（x)不会超过x/2
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x==0:
#             return 0
#         l,r=1,x//2+1
#         while l<r:
#             #这里一定取右中位数，如果取左中位数，代码可能会进入死循环
#             mid=(r+l+1)//2
#             if mid*mid > x:
#                 r=mid-1
#             else:
#                 l=mid
#         return int(l)

# 4、牛顿迭代法 84.38%
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         cur=1
#         while True:
#             pre=cur
#             cur=(cur+x/cur)/2
#             if abs(cur-pre)<=1e-6:
#                 return int(cur)


# @lc code=end

