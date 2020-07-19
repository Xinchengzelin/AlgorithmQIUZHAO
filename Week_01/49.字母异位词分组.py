#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #直接用哈希表，key为字母按顺序排列的元祖
        dic={}
        for w in strs:
            k=tuple(sorted(w))
            dic[k]=dic.get(k,[])+[w]
        return list(dic.values())#元素顺序不影响结构


# @lc code=end

