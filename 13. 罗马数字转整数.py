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
