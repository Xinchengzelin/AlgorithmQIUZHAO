#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(","]":"[","}":"{"}
        stack=[]
        for c in s:
            if c in dic.values():
                stack.append(c)
            elif c in dic.keys():
                if stack==[] or stack.pop()!=dic[c]:#or前后条件顺序不能换，可能会有[].pop()而报错
                    return False
            else:
                return False

        return stack==[]
# @lc code=end

