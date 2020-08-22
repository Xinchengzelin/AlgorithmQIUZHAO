#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
# 1、ascii码  64.23%/83.98%
# class Solution:
#     def toLowerCase(self, str: str) -> str:
#         s = []
#         for ch in list(str):
#             if 65 <= ord(ch) <= 90:
#                 s.append(chr(ord(ch)+32))
#             else:
#                 s.append(ch)
#         return "".join(s)
# 2、字典 85.66%/98.58%
class Solution:
    def toLowerCase(self, str: str) -> str:
        dic = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
               'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
               'M':'m', 'N':'n', 'O':'o','P':'p', 'Q':'q', 'R':'r',
               'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
               'Y':'y', 'Z':'z'}
        # （一）
        # s = []
        # for ch in str:
        #     if ch in dic:
        #         s.append(dic[ch])
        #     else:
        #         s.append(ch)
        # （二）
        # s = [dic.get(ch,ch) for ch in str]
        # （三）
        s = [dic[ch] if ch in dic else ch for ch in str]
        return "".join(s)
# @lc code=end

