#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
# 1、横向扫描法 36.31%/36.04%
# class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     # if not strs: return ""
    #     # length =list(map(len,strs))
    #     # for i in range(min(length)):
    #     #     com_ch = strs[0][i]
    #     #     for j in range(1,len(strs)):
    #     #         if strs[j][i] != com_ch:
    #     #             return strs[0][:i] if i > 0 else ""
    #     # return strs[0]  #不通过["aa","a"]
    #     if not strs: return ""
    #     length,count = len(strs[0]),len(strs)
    #     for i in range(length):
    #         com_ch = strs[0][i]
    #         if any(i == len(strs[j]) or strs[j][i] != com_ch for j in range(1,count)):
    #             return strs[0][:i]
    #     return strs[0]
# 1.1、横向扫描法 93.51%/25.18%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        shortest = min(strs,key = len)
        for i,ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
# 2、Trie树
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:                

# @lc code=end

