#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
# 1、直接计算 92.11%/88.23%
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         if len(str.strip()) == 0: return 0
#         s = list(str.strip())
#         sign = -1 if s[0] == "-" else 1
#         if s[0] in ["+","-"]: del s[0]
#         res,i =0,0
#         while i < len(s) and s[i].isdigit():
#             res = res*10 + ord(s[i]) - ord("0")
#             i += 1
#         # res = sign * res
#         # if res >= 2**31 -1:
#         #     return 2**31 -1
#         # elif res <= -2**31:
#         #     return -2**31
#         # else:
#         #     return res# 上面的if else速度更快
#         return min(2**31-1,max(res * sign,-2**31))
# 2、正则表达式 59.2%/65.52%
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2**31-1#2147483647    
        INT_MIN = -2**31#-2147483648
        str = str.strip()
        num_re = re.compile(r"^[\+\-]?\d+")
        num = num_re.findall(str)
        # print(num)
        num = int(*num)
        return min(INT_MAX,max(INT_MIN,num))
# @lc code=end

