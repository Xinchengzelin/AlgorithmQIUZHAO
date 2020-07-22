#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1、暴力法：时间复杂度：O(Nk)——max(nums)是O(k) 空间复杂度：O(N−k+1)-返回结果
        # n=len(nums)
        # if n*k==0:
        #     return []
        # return [max(nums[i:i+k]) for i in range(n-k+1)]
        # 结果：Time Limit Exceeded #

        # 2、双向队列 构建一个index为值得deque
        from collections import deque
        res=[]
        d=deque()
        #确保deque最右边的值最小
        for i,v in enumerate(nums):
            while d and nums[d[-1]]<=v:
                d.pop()
            #增加元素到deque
            d.append(i)
            #确保左边的元素没有超出窗口
            if d[0]<=i-k:
                d.popleft()
            #if i + 1 < k, then we are initializing the deque
            if i+1>=k:
                res.append(nums[d[0]])   
        return res 

        # 3、堆的思想


# @lc code=end

