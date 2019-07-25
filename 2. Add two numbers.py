# 2.Add two numbers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        summ = 0
        times = 1
        while l1 != None or l2 != None:
            if l1 == None:
                x = 0
            else:
                x = l1.val
                l1 = l1.next
            if l2 == None:
                y = 0
            else:
                y = l2.val
                l2 = l2.next
            singlesum = x + y
            if singlesum >= 10:
                singlesum -= 10
                carry = 1
            else:
                carry = 0
            summ += singlesum * times + carry * times * 10
            times *= 10
        summ_str = str(summ)
        summ_list = list(summ_str)
        summ_list.reverse()
        summm = ','.join(summ_list)
        return ListNode(summm)