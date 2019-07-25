# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx1, item1 in enumerate(nums):
            for idx2, item2 in enumerate(nums):
                if idx1 != idx2:
                    if item1 + item2 == target:
                        return [idx1, idx2]
                    # else:
                    #     return 'No answer'