# 19. 删除链表的倒数第N个节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        l1 = temp
        l2 = temp
        for i in range(n):
            l1 = l1.next
        while l1.next != None:
            l1 = l1.next
            l2 = l2.next
        l2.next = l2.next.next
        return temp.next