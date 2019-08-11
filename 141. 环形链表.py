# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        l = ListNode(0)
        r = ListNode(0)
        l.next = head
        r = head
        while l != r:
            if r != None and r.next != None:
                l = l.next
                r = r.next.next
            else:
                return False
        return True