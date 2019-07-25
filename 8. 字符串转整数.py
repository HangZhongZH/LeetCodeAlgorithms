# 8. 字符串转整数
    # 参考
    class Solution(object):
        def myAtoi(self, str):
            str = str.strip()  # 去除空格
            if str == "":
                return 0;  # 特殊情况 str="0"
            left = 0
            right = 0
            maxi = 2147483647
            mini = -2147483648  # 用于后面判断是否越界
            if str[0] == '+' or str[0] == '-':
                left = 1  # 判断第一个字符是否为正负号
            if (left == 1 and len(str) == 1) or str[left] < '0' or str[left] > '9':
                return 0  # 注意特殊情况 str="+"
            for i in range(left, len(str)):  # right移动到第一个不是数字的地方
                if str[i] >= '0' and str[i] <= '9':
                    right = i
                else:
                    break
            res = str[left:right + 1].lstrip('0')  # 去除左边的0
            if len(res) == 0:
                return 0  # 清除后可能没数字
            else:
                res = eval(res)  # eval是个非常好用的函数，自行了解
            if left == 1 and str[0] == '-':  # 判断正负
                res = -res
            if res > maxi:
                return maxi
            elif res < mini:
                return mini
            else:
                return res


# 自己编
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        str = str.lstrip()
        left = 0
        right = 0
        if str == '':
            return 0
        elif str[0] in ['+', '-']:
            left = 1
        elif str[0].isdigit():
            left = 0
        else:
            return 0
        # if left == 1 and len(str) == 1:
        #     return 0
        for i in range(left, len(str)):
            if str[i].isdigit():
                right = i
            else:
                break
        num_str = str[left: right + 1]
        num_str = num_str.lstrip('0')
        if len(num_str) == 0:
            return 0
        else:
            num = eval(num_str)
            if left == 1 and str[0] == '-':
                num = -num
            if num < INT_MIN:
                return INT_MIN
            elif num > INT_MAX:
                return INT_MAX
            else:
                return num
