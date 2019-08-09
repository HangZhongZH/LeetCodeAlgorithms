# 超时
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 2
        count = 0
        #ans = []
        while num < n:
            ifsu = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    ifsu = False
                    break
            if ifsu:
                #ans.append(num)
                count += 1
            num += 1
        return count

# 厄拉多筛选法
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        else:
            lst = [1] * n
            lst[0] = 0
            lst[1] = 0
            ans = 0
            for i in range(2, len(lst)):
                if lst[i] == 1:
                    ans += 1
                    for j in range(i, n, i):
                        lst[j] = 0
            # print(ans)
            return ans