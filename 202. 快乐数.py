class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        past = [n]
        sqrsum = n
        while sqrsum != 1:
            sqrsum = 0
            for item in str(past[-1]):
                sqrsum += int(item)**2
            if sqrsum in past:
                #print(sqrsum, past)
                return False
            past.append(sqrsum)
        return True