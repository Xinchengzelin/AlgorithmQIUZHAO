#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 直接解法
        # digit=[str(num) for num in digits]
        # num=int("".join(digit))+1
        # res=[]
        # for c in str(num):
        #     res.append(int(c))
        # return res

        #直接的另一种解法
        # num=0
        # for i in range(len(digits)):
        #     num+=digits[i]*pow(10,len(digits)-1-i)
        # return [int(c) for c in str(num+1)]

        # #进位解法
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                break
        if digits[0]==0:
            digits.insert(0,1)
        return digits


        

# @lc code=end

