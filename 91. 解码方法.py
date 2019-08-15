class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        从第一个数字开始， 若=1，可以自己+与后面数字
                        = 2,若后面数小于等于6，可以自己+后面数字
                            若后面数字大于6，只能自己
                        > 2， 只能自己

                    dp[i] = dp[i -1] + dp[i -2]

        '''
        if not s:
            return 0
        if s[0] == '0' or '00' in s:
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if int(s[i]) == 0 and int(s[i - 1]) > 2:
                return 0
            elif int(s[i]) == 0:
                dp[i + 1] = dp[i - 1]
            elif (int(s[i - 1]) == 1) or (int(s[i]) <= 6 and int(s[i - 1]) == 2):
                dp[i + 1] = dp[i - 1] + dp[i]
            else:
                dp[i + 1] = dp[i]
        return dp[-1]
