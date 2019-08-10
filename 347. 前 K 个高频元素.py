import heapq
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        print(count)
        largestvalues = heapq.nlargest(k, count.values())
        ans = []
        for item in largestvalues:
            for key in count:
                if count[key] == item:
                    ans.append(key)
                    count[key] = -1
        return ans