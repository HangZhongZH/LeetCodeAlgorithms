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
