class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Way 1, 内置函数
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


