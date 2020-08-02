#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1、迭代-思路：从空集开始，遍历出任意1个元素，依次加到已产生的
        # 集合中，作为新的返回结果
        # ans=[[]]
        # for i in nums:
        #     new_subsets=[]
        #     for subset in ans:
        #         new_subset=subset+[i]
        #         new_subsets.append(new_subset)
        #     ans.extend(new_subsets)
        # return ans
        # 2、迭代-精简代码
        # ans=[[]]
        # for i in nums:
        #     ans.extend([[i]+sub for sub in ans])#与17电话号码的精简代码对比
        # return ans

        # 3、递归-每个元素，可以选或者不选
        # def helper(lis,index):
        #     if index==len(nums):
        #         ans.append(lis[:])#拷贝一份新的数组，不用共用一份
        #         return #不要漏掉return
        #     helper(lis,index+1)#不选
        #     lis.append(nums[index])
        #     helper(lis,index+1)# 选
        #     # 没有reverse的话，可以helper(lis.copy(),index+1)
        #     # 用copy的方法，改变的lis不会影响上面的层，也不会影响下面的层
        #     #reverse state
        #     lis.pop()# 把最后加在lis中的数去掉
        #     #lis随着递归一直在变动，不是本层的变量
        #     # 别以为函数到末尾就万事大吉了，递归程序中，函数结束后会继续执行父函数
        # if not nums:
        #     return [[]]
        # ans=[]
        # helper([],0)
        # return ans

        # 4、递归-父亲拷贝一份新的给孩子，孩子乱改也不怕
        def helper(lis,index):
            if index==len(nums):
                ans.append(lis)
                return 
            helper(lis[:],index+1)#lis[:]和lis是两个不同的变量
            helper(lis[:]+[nums[index]],index+1)#拷贝一份新的给孩子，不用担心孩子乱改
            # lis.pop()# 不用这句了，孩子不用担心改父亲了
        if not nums:
            return [[]]
        ans=[]
        helper([],0)
        return ans
        # 5、利用itertools 40ms
        # import itertools
        # res=[[],]
        # for i in range(1,len(nums)+1):
        #     for tup in itertools.combinations(nums,i):
        #         res.append(list(tup))
        # return res


# @lc code=end

