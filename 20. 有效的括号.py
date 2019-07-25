# 20. 有效的括号
# 1st way
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


# 2nd way
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = list(s)
        stack = []
        dic = {'(': ')', '[': ']', '{': '}'}
        if s_list == []:
            return True
        else:
            stack.append(s_list[0])
            for i in range(1, len(s_list)):
                if stack == []:
                    stack.append(s_list[i])
                elif stack[-1] in dic:
                    if dic[stack[-1]] == s_list[i]:
                        stack.pop()
                    elif dic[stack[-1]] != s_list[i]:
                        stack.append(s_list[i])
                elif stack[-1] not in dic:
                    return False
            return stack == []