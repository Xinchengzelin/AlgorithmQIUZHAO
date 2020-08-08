#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# s[i] != '0'
# 如果 s[i-1]s[i] <= 26, 则 dp[i] = dp[i-1] + dp[i-2]
# 如果 s[i-1]s[i] > 26, 则 dp[i] = dp[i-1], 这是因为 s[i-1]s[i] 组成的两位数无法翻译
# s[i] == '0'
# 如果 s[i-1]s[i] <= 26, 则 dp[i] = dp[i-2], 这是因为 s[i] 无法翻译
# 还有一些情景直接使得整个序列无法被翻译：
# 相邻的两个 ‘0’
# 以 ‘0’ 结尾的大于 26 的数字
# 以 “0” 开头的数字
# 特例101，

# @lc code=start
# 1、动态规划   83.03%、95.26%
# 每个i都要考虑s[i]是否“0”、s[i-1]是否是“0”和s[i-1:i+1]是否大于26、
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not s or s[0] == "0": return 0
#         m=len(s)
#         if m==1: return 1
#         dp=[0]*m
#         for i in range(1,m):
#             if i == 1:
#                 if s[i] != "0":
#                     if (int(s[:2])) <= 26 :
#                         dp[i],dp[i-1]=2,1
#                     else:
#                         dp[i],dp[i-1]=1,1
#                 elif s[i] == "0":
#                     if int(s[i-1]) >= 3:
#                         return 0
#                     else:
#                         dp[i],dp[i-1]=1,1
#             else:
#                 if s[i] != "0":
#                     if (int(s[i-1:i+1]) <= 26) and s[i-1] != "0":
#                         dp[i]=dp[i-1]+dp[i-2]
#                     else:
#                          dp[i]=dp[i-1]
#                 elif s[i] == "0" :
#                     if s[i-1]  == "0" or int(s[i-1]) >= 3:
#                         return 0
#                     else:
#                         dp[i]=dp[i-2]
#         return dp[m-1]
# 2、动态规划-优化了代码，多构造dp[0]=1   63.55%/77.89%
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        m=len(s)
        dp=[0]*(m+1)
        dp[0]=1
        dp[1]= 0 if s[0]=="0" else 1
        for i in range(2,m+1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i]=dp[i-1]
            if 10 <= int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
        return dp[m]



# @lc code=end

