#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
# 1、暴力法 - 超时
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         cnt = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] > 2*nums[j]:
#                     cnt += 1
#         return cnt
# 2、merge-sort 82.62%/76.92%
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)
    def mergeSort(self,nums,left,right):
        if left >= right: 
            return 0
        mid = left + ((right - left)>>1)
        cnt = self.mergeSort(nums,left,mid) + self.mergeSort(nums,mid+1,right)
        # for i in range(left,mid + 1):
        #     k = 0
        #     for j in range(mid+1,right+1):
        #         if ((nums[i]+1)>>1) > nums[j]:
        #             k += 1
        #     cnt += k  # 这段代码会超时
        i,j = left,mid +1 
        while i <= mid and j <= right:
            if (nums[i]+1)>>1 > nums[j]:
                cnt += mid + 1 - i
                j += 1
            else:
                i += 1
        nums[left:right+1] = sorted(nums[left:right+1])
        return cnt

        
# @lc code=end

