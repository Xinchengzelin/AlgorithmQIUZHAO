#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代法
        # prev=None
        # cur=head
        # while cur:
        #     temp=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=temp
        # return prev

        #递归法
        if not head or not head.next:
            return head
        newNode=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newNode

# @lc code=end

