#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1、 分治-快速幂  O(logN)  O(logN)
        # def fastpow(x,n):
        #     if n==0:
        #         return 1
        #     half=fastpow(x,n//2)#重复子问题
        #     return half*half if n%2==0 else half*half*x #分治后的merge
        # return fastpow(x,n) if n>=0 else fastpow(1/x,-n)

        #2、快速幂-迭代-关键是搞清楚与二进制N的关系
        # https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
        
        def fastpow(N):
            ans=1.0
            x_1=x
            while N>0:
                if N%2==1:
                    ans*=x_1
                x_1*=x_1
                N//=2#相当于右移
            return ans
        return fastpow(n) if n>=0 else 1.0/fastpow(-n)    

        # 3、 暴力-会超时
        # if n<0:
        #     x,n=1/x,-n
        # if n==0:
        #     return 1
        # res=1
        # for _ in range(n):
        #     res=x*res
        # return res
            
            
# @lc code=end

