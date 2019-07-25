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