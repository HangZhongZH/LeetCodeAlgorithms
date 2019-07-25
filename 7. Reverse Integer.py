# 7. Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        x_list = list(x_str)
        reverse_list = []
        for i in range(len(x_list)):
            reverse_list.append(x_list.pop())
        listLength = len(reverse_list)
        for i in range(len(reverse_list)):
            if i != listLength - 1:
                if reverse_list[0] == '0':
                    reverse_list = reverse_list[1: ]
            elif i == listLength - 1:
                reverse_list == 0
            else:
                break
        if reverse_list[-1] == '-':
            reverse_list = list('-') + reverse_list[: -1]
        reverse_num = int(''.join(reverse_list))
        if reverse_num < -2**31 or reverse_num > 2**31 - 1:
            reverse_num = 0
        return reverse_num