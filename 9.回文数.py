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