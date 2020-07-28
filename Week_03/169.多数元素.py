#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start

# 1、哈希表统计: 60ms(40.31%)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i,v in enumerate(nums):
            dic[v]=dic.get(v,0)+1
        return max(dic.keys(),key=dic.get)
# 2、排序-排序后下标为n/2的元素（下标从 0 开始）一定是众数
# class Solution: #44ms (92.18%)
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]
# 3、分治-将数组分成左右两部分，分别求出左半部分的众数 a1 以及右半部分的众数 a2，随后在 a1 和 a2 中选出正确的众数
class Solution: # 184ms(5.13%)
    def majorityElement(self, nums: List[int]) -> int:
        def majority_pick(lo,hi):
            if lo==hi:#只有一个元素
                return nums[lo]
            mid=(hi-lo)//2+lo#recurse
            left=majority_pick(lo,mid)
            right=majority_pick(mid+1,hi)
            if left==right:
                return left
            left_count=sum(1 for i in range(lo,hi+1) if nums[i]==left)
            right_count=sum(1 for i in range(lo,hi+1) if nums[i]==right)
            return left if left_count>right_count else right
        return majority_pick(0,len(nums)-1)

# @lc code=end

