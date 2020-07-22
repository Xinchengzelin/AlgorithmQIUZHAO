#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        dic={}
        for v in nums:
            dic[v]=dic.get(v,0)+1
        # dic=Counter(nums) #和上面效果一样
        # queue,res=[],[]
        # for i in dic:
        #     heapq.heappush(queue, (-dic[i], i))
        # for i in range(k):
        #     tmp = heapq.heappop(queue)
        #     res.append(tmp[1])
        # return res
        return heapq.nlargest(k,dic.keys(),key=dic.get)#和上面效果一样

# @lc code=end

