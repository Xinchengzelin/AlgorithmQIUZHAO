#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
# 1、  66.64%/96.26%
# 计算每个任务出现的次数
# 找出出现次数最多的任务，假设出现次数为 x
# 计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
# 计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1: return length
        dic=dict()
        for k,v in enumerate(tasks):
            dic[v]=dic.get(v,0)+1
        dic_sort=sorted(dic.items(),key = lambda x : x[1],reverse = True)
        max_count= dic_sort[0][1]
        res = (max_count-1) * (n+1) # 至少需要的时间
        # for k in dic_sort: # 也可以
        #     if k[1] == max_count:
        #         res += 1
        for k in dic:
            if dic[k] == max_count:
                res += 1
        # 如果结果比任务数量少，则返回总任务数
        return res if res > length else length

# @lc code=end

