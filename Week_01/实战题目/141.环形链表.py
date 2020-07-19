#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #快慢指针法
        slow,fast=head,head
        while slow and fast.next:#fast.next排除了NoneType类型
            slow=slow.next
            fast=fast.next.next
            if not fast:
                return False
            elif slow==fast:
                return True
        return False #增加这句时间从544ms减少到了80ms

        #哈希表法
        dic={}
        while head:
            dic[head]=1
            head=head.next
            if head in dic.keys():
                return True
        return False

        
# @lc code=end

