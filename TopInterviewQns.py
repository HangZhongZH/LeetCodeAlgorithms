# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx1, item1 in enumerate(nums):
            for idx2, item2 in enumerate(nums):
                if idx1 != idx2:
                    if item1 + item2 == target:
                        return [idx1, idx2]
                    # else:
                    #     return 'No answer'


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




# 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        past = []
        current = []
        for i in s:
            if i not in current:
                current.append(i)
            else:
                if len(past) < len(current):
                    past = current
                current = current[current.index(i) + 1: ] + [i]
        return max(len(past), len(current))


# 4.Median of Two Sorted Arrays




# 5.Longest Palindromic Substring




# 7. Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        x_list = list(x_str)
        reverse_list = []
        for i in range(len(x_list)):
            reverse_list.append(x_list.pop())
        listLength = len(reverse_list)
        for i in range(len(reverse_list)):
            if i != listLength - 1:
                if reverse_list[0] == '0':
                    reverse_list = reverse_list[1: ]
            elif i == listLength - 1:
                reverse_list == 0
            else:
                break
        if reverse_list[-1] == '-':
            reverse_list = list('-') + reverse_list[: -1]
        reverse_num = int(''.join(reverse_list))
        if reverse_num < -2**31 or reverse_num > 2**31 - 1:
            reverse_num = 0
        return reverse_num


# 8. 字符串转整数
    class Solution(object):
        def myAtoi(self, str):
            str = str.strip()  # 去除空格
            if str == "":
                return 0;  # 特殊情况 str="0"
            left = 0
            right = 0
            maxi = 2147483647
            mini = -2147483648  # 用于后面判断是否越界
            if str[0] == '+' or str[0] == '-':
                left = 1  # 判断第一个字符是否为正负号
            if (left == 1 and len(str) == 1) or str[left] < '0' or str[left] > '9':
                return 0  # 注意特殊情况 str="+"
            for i in range(left, len(str)):  # right移动到第一个不是数字的地方
                if str[i] >= '0' and str[i] <= '9':
                    right = i
                else:
                    break
            res = str[left:right + 1].lstrip('0')  # 去除左边的0
            if len(res) == 0:
                return 0  # 清除后可能没数字
            else:
                res = eval(res)  # eval是个非常好用的函数，自行了解
            if left == 1 and str[0] == '-':  # 判断正负
                res = -res
            if res > maxi:
                return maxi
            elif res < mini:
                return mini
            else:
                return res
