#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start

# 1、堆
# import heapq
# class Ugly:
#     def __init__(self):
#         seen={1,}
#         self.nums=nums=[]
#         heap=[]
#         heapq.heappush(heap,1)
#         for _ in range(1690):
#             cur_ugly=heapq.heappop(heap)
#             nums.append(cur_ugly)
#             for v in [2,3,5]:
#                 new_ugly=cur_ugly * v
#                 if new_ugly not in seen:
#                     seen.add(new_ugly)
#                     heapq.heappush(heap,new_ugly)
# class Solution:
#     u=Ugly()
#     def nthUglyNumber(self, n: int) -> int:
#         return self.u.nums[n - 1]

# 2、 动态规划-三指针
class Ugly:
    def __init__(self):
        self.nums=nums=[1,]
        p2,p3,p5=0,0,0
        for i in range(1,1690):
            ugly=min(2*nums[p2],3*nums[p3],5*nums[p5])
            nums.append(ugly)
            if ugly==2 * nums[p2]:
                p2+=1
            if ugly==3 * nums[p3]:#这里不能用elif，比如6，p2和p3都要+1
                p3+=1                
            if ugly==5 * nums[p5]:
                p5+=1
class Solution:
    u=Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]
# @lc code=end

