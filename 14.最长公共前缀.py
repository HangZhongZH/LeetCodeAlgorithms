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