#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
# 1、翻转指针 91.44%/23.18%  
# 直接增加一个数组，会比较方便，不需要list(S)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        import string
        s = list(S)
        r = len(s)-1#右指针
        for i,ch in enumerate(s):
            while ch.isalpha() and r > i:
                if s[r].isalpha():
                    s[i],s[r] = s[r],s[i]
                    r -= 1
                    break
                r -= 1
        return "".join(s)
# 2、字母栈 99.69%/8.65%
# class Solution:
#     def reverseOnlyLetters(self, S: str) -> str:
#         letters = [ch for ch in S if ch.isalpha()]
#         res = []
#         for i,ch in enumerate(S):
#             if ch.isalpha():
#                 res.append(letters.pop())
#             else:
#                 res.append(ch)
#         return "".join(res)


        
# @lc code=end

