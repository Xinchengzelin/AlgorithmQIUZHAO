#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 迭代法
        res=ListNode(None)
        prev=res
        res.next=head
        while not head and not head.next:
            #更新firstNode和secondNode
            firstNode=head
            secondNode=head.next
            #交换
            prev.next=secondNode
            firstNode.next=secondNode.next#指向下一组的第1个
            secondNode.next=firstNode
            #初始化prev和head
            prev=firstNode
            head=firstNode.next
        return res.next

            
            


# @lc code=end

