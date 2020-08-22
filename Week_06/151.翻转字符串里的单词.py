#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
# 1、利用函数 97.47%/20.62%
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        return " ".join(s[::-1])
# @lc code=end

