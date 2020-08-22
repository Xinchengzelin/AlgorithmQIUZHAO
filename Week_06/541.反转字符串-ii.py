#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
# 直接法  19.26%/36.67%
# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         if not s or not k: return s
#         s = list(s)
#         n = len(s)
#         for i in range(n//(2*k)+1):
#             l = i*2*k
#             r = min(l+k-1,n-1)
#             while l < r:
#                 s[l],s[r] = s[r],s[l]
#                 l += 1
#                 r -= 1
#         return "".join(s)
# 2、 精简代码 36.32%/70.67%
# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         s = list(s)
#         for i in range(0,len(s),2*k):
#             s[i:i+k] = reversed(s[i:i+k])
#         return "".join(s)
# 3、精简 100%/38.62%
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s= [s[i:i+k] for i in range(0,len(s),k)]
        for i in range(0,len(s),2):
            s[i] = s[i][::-1]
        return "".join(s)
        
# @lc code=end

