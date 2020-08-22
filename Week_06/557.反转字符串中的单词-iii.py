#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
# 1、59.98%/41.43%
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.split()
#         for i,word in enumerate(s):
#             s[i] = word[::-1]
#         return " ".join(s)
# 2、精简代码 78.05%/5.31%
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split()])
        
# @lc code=end

