#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 合并后排序
        # nums1[:]=nums1[:m]+nums2
        # nums1[:]=nums1[:m].extend(nums2)#会报错
        # if nums1:
        #     nums1.sort()

        # 快慢指针-从后向前
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if n>0:
            nums1[:n]=nums2[:n]










# @lc code=end

