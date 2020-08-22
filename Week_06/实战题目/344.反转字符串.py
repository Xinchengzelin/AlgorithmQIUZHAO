#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
# 1、类似于双指针 96.08%/47.76%
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1: return
        n = len(s)
        for i in range(len(s)//2):
            s[i],s[n-i-1] = s[n-i-1],s[i]
# @lc code=end

