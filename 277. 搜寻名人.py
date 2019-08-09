# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n):
            if knows(res, i):
                res = i
        # 现在因为res前有人认识他，所有他前面不可能有名人
        # 且， res不认识他后面的所有人， 所以后面也不可能有名人

        # 现在只需要测试res是否认识他前面的人， 若有认识的，则res也不是名人，即没有名人
        # 若res不认识他前面的所有人，则还需测试他前面的所有人及后面的所有人是否都认识他， 若是， 则res是名人， 反之没有名人

        for i in range(res):
            if knows(res, i):
                return -1
            if not knows(i, res):
                return -1
        for i in range(res + 1, n):
            if not knows(i, res):
                return -1
        return res