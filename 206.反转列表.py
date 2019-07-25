# 206.反转列表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Way 1
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        past = None
        current = head
        while current:
            nextTemp = current.next
            current.next = past
            past = current
            current = nextTemp
        return past