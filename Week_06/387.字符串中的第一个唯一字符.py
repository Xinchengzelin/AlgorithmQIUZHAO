#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
# 1、暴力 10.18%/46.59%
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j and s[j] == s[i]:
                    break
            else:
                return i
        return -1
# 1.1、暴力 10.3%/98.42%
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         flag = False
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 if i != j and s[j] == s[i]:
#                     flag = False
#                     break
#                 else:
#                     flag = True
#             if flag:
#                 return i
#         return -1

# 2、用count函数 5.02%/13.98%
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in range(len(s)):
#             if s.count(s[i])==1:
#                 return i
#         return -1#应对""
# 3、哈希表 26.66%/69.63%
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         dic={}
#         for ch in s:
#             dic[ch] = dic.get(ch,0)+1
#         for i in range(len(s)):
#             if dic[s[i]] == 1:
#                 return i
#         return -1
# 4、精简版 95.57%/59.73%
# import string
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         return min([s.find(ch) for ch in string.ascii_lowercase if s.count(ch)==1] or [-1])
        
# @lc code=end

