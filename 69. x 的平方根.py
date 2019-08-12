class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return int(x)
        maxnums = x
        minnums = 0
        while (maxnums - minnums) > 1:
            midnums = (maxnums + minnums) // 2
            if midnums**2 > x:
                maxnums = midnums
            elif midnums**2 < x:
                minnums = midnums
            else:
                maxnums = minnums = midnums
        return minnums
