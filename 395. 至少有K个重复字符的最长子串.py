class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        for item in set(s):
            if s.count(item) < k:
                return max(self.longestSubstring(t, k) for t in s.split(item))
        return len(s)