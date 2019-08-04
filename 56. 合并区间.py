class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        if len(intervals) <= 1:
            return intervals
        else:
            temp = intervals[0]
            for i in range(1, len(intervals)):
                if intervals[i][0] <= temp[1]:
                    temp = [temp[0], max(intervals[i][1], temp[1])]
                else:
                    res.append(temp)
                    temp = intervals[i]
            res.append(temp)
        return res
