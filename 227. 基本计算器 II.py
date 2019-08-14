class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s + '+'
        res = 0
        d = 0
        nums = []
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                d = d * 10 + int(s[i])

            if s[i] != ' ' and s[i] in ['+', '-', '*', '/']:
                if sign == '+':
                    nums.append(d)
                elif sign == '-':
                    nums.append(-d)
                elif sign == '*':
                    nums[-1] = nums[-1] * d
                elif sign == '/':
                    nums[-1] = int(nums[-1] / d)
                sign = s[i]
                d = 0
        print(nums)
        res = sum(nums)
        return res