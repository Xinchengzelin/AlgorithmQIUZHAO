#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
# 1、count  49.98%/11.21%
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         res = 0
#         for ch in J:
#             res += S.count(ch)
#         return res
# 2、哈希  23.73%/11.21%
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         dic = {}
#         for ch in S:
#             dic[ch] = dic.get(ch,0)+1
#         return sum([dic.get(ch,0) for ch in J])
# 3、精简版
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
        
# @lc code=end

