#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 直接暴力法
        # if len(s)==len(t):
        #     list(s).sort()
        #     list(t).sort()
        #     print(s,t)
        #     return s==t
        # else:
        #     return False

        # 直接暴力法2
        # return sorted(s)==sorted(t):

            
        #使用哈希表
        # dic1,dic2={},{}
        
        # for c in s:
        #     dic1[c]=dic1.get(c,0)+1
        # for c in t:
        #     dic2[c]=dic2.get(c,0)+1
        # return dic1==dic2


        #利用ASCII码构建哈希表
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2




    # @lc code=end

