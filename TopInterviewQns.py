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
    # 参考
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


# 自己编
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        str = str.lstrip()
        left = 0
        right = 0
        if str == '':
            return 0
        elif str[0] in ['+', '-']:
            left = 1
        elif str[0].isdigit():
            left = 0
        else:
            return 0
        # if left == 1 and len(str) == 1:
        #     return 0
        for i in range(left, len(str)):
            if str[i].isdigit():
                right = i
            else:
                break
        num_str = str[left: right + 1]
        num_str = num_str.lstrip('0')
        if len(num_str) == 0:
            return 0
        else:
            num = eval(num_str)
            if left == 1 and str[0] == '-':
                num = -num
            if num < INT_MIN:
                return INT_MIN
            elif num > INT_MAX:
                return INT_MAX
            else:
                return num




# 11. 盛最多水的容器
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left <= right:
            length = right - left
            if height[left] <= height[right]:
                h = height[left]
                left += 1
            elif height[left] > height[right]:
                h = height[right]
                right -= 1
            maxArea_temp = length * h
            if maxArea_temp >= maxArea:
                maxArea = maxArea_temp
        return maxArea




# 13. 罗马数字转整数
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        num = 0
        tiao = False
        for i in range(len(s)):
            if tiao:
                tiao = False
                pass
            elif i != len(s) and s[i: i + 2] in dic2:
                num += dic2[s[i: i + 2]]
                tiao = True
            else:
                num += dic[s[i]]
        return num



# 20. 有效的括号
# 1st way
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


# 2nd way
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = list(s)
        stack = []
        dic = {'(': ')', '[': ']', '{': '}'}
        if s_list == []:
            return True
        else:
            stack.append(s_list[0])
            for i in range(1, len(s_list)):
                if stack == []:
                    stack.append(s_list[i])
                elif stack[-1] in dic:
                    if dic[stack[-1]] == s_list[i]:
                        stack.pop()
                    elif dic[stack[-1]] != s_list[i]:
                        stack.append(s_list[i])
                elif stack[-1] not in dic:
                    return False
            return stack == []




# 9.回文数
# Way 1
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if not x_str[0].isdigit():
            return False
        else:
            if len(x_str) == 1:
                return True
            elif len(x_str) > 1:
                left = 0
                right = len(x_str) - 1
                while left < right:
                    if x_str[left] != x_str[right]:
                        return False
                    else:
                        left += 1
                        right -= 1
                return True

# Way 2
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        y = x_str[:: -1]
        return y == x_str


# 14.最长公共前缀
# Way 1
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        x1 = min(strs)
        x2 = max(strs)
        for idx in range(len(x1)):
            if x1[idx] != x2[idx]:
                return x1[: idx]
        return x1

# Way 2
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for i in range(1, len(strs)):
            temp = strs[i]
            l = 0
            while l < min(len(ans), len(temp)):
                if ans[l] != temp[l]:
                    break
                else:
                    l += 1
            ans = ans[: l]
        return ans




# 15. 三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i >= 1:
                continue
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                break
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while nums[left] == nums[left + 1] and left < right - 1:
                        left += 1
                    while nums[right] == nums[right - 1] and right > left + 1:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans




# 17.电话号码的字母组合
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}
        if not digits:
            return []
        length = len(digits)
        ans = ['']
        for i in range(length):
            ans = [x + y for x in ans for y in dic[digits[i]]]
        return ans



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





# 21. 合并两个有序链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        temp = ans
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 == None:
                temp.next = l2
        elif l2 == None:
                temp.next = l1
        return ans.next



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