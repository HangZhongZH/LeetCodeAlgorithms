# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        if head.next != None and head.next.next == None:
            if head.val == head.next.val:
                return True
            else:
                return False
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        pre = None
        curr = slow
        while curr:
            nextTemp = curr.next
            curr.next = pre
            pre = curr
            curr = nextTemp

        while head and pre:
            if head.val == pre.val:
                head = head.next
                pre = pre.next
            else:
                return False
        return True