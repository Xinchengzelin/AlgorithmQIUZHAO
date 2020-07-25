#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def generate(left=0,right=0,s=""):
            if (left==n and right==n):
                ans.append(s)
                return 
            if left<n:
                generate(left+1,right,s+'(')
            if right<left:
                generate(left,right+1,s+')')
        generate(0,0,"")
        return ans

# @lc code=end

