class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        longest = 1
        longest_str = s[0]
        for i in range(len(s)):
            longest_odd_str, longest_odd = self.findlongest(s, i, i)
            longest_even_str, longest_even = self.findlongest(s, i, i + 1)
            temp_str = longest_odd_str if longest_odd >= longest_even else longest_even_str
            if len(temp_str) > longest:
                longest_str = temp_str
                longest = len(longest_str)
        return longest_str
    def findlongest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r], r - l - 1