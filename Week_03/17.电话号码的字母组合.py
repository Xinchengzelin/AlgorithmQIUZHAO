#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
# 1、递归法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dic={'2':'abc','3':"def",'4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def helper(s,index):
            if index==len(digits):
                res.append(s)
                return
            letters=dic[digits[index]]#当前数字可以使用的字母
            for j in range(len(letters)):
                helper(s+letters[j],index+1)
            # return res
        if digits:
            helper('',0)
        return res
# 2、精简版
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         dic={'2':'abc','3':"def",'4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
#         res=[''] if digits else []
#         for d in digits:
#             res=[p + q for p in res for q in dic[d]]#子集问题这里是res.extend()
#         return res
# @lc code=end

