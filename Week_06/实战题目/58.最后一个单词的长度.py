#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
# 1、倒序计数 96.17%/45.74%
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         for i in range(len(s)-1,0,-1):
#             if s[i] != " ":
#                 cnt = i
#                 j = i
#                 while s[j]!= " " and j >= 0:
#                     j -= 1
#                 return i - j
#         return len(s.rstrip())
# 2、倒序计数 17.48%/68.1%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res,s = 0,s.rstrip()
        while res < len(s) and s[-(res+1)] != " ":
            res += 1
        return res
# 3、split 96.17%/11.4%
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         # s = s.split()
#         # return len(s[-1]) if s else 0    
#         return len(s.rstrip().split(" ")[-1])# strip和split都有参数



# @lc code=end

