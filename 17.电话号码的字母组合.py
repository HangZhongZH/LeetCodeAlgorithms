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