#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# 1、贪心-用的是贪心的思想 75.38%
# @lc code=start
# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         five,ten=0,0
#         for bill in bills:
#             if bill==5:
#                 five+=1
#             elif bill==10:
#                 if not five:
#                     return False
#                 else:
#                     ten+=1
#                     five-=1
#             elif bill==20:
#                 if five and ten:
#                     five-=1
#                     ten-=1
#                 elif five >=3:
#                     five-=3
#                 else:
#                     return False
#         return True

# 2、贪心-精简代码 94.27%
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=ten=0
        for bill in bills:
            if bill==5: five+=1
            elif bill==10: five,ten=five-1,ten+1
            elif bill==20 and ten: five,ten=five-1,ten-1
            elif bill==20 and not ten: five-=3
            if five<0: return False
        return True
        
# @lc code=end

