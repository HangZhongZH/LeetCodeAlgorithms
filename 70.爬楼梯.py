class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:
            s1 = 1
            s2 = 2
            for i in range(n - 2):
                si = s1 + s2
                s1= s2
                s2 = si
            return si