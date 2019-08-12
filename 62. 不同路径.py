import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Way1
        m*n = (m-1)*n + m*(n-1)
        (m-1)*n = (m-2)*n + (m-1)*(n-1)
        ......行，列>=1
        动态规划
                dp = [[1] * n]
                for i in range(m - 1):
                    dp.append([1] + [0] * (n - 1))

                for i in range(1, m):
                    for j in range(1, n):
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                return dp[m - 1][n - 1]



        # Way2
        # 数学公式做: 一共要走m + n - 2次，其中有m - 1次能走到终点，一共Cm+n-2/m-1
        ans = math.factorial(m + n - 2) / math.factorial(n - 1) / math.factorial(m - 1)
        return ans