import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Way1
        count = collections.Counter(nums)
        for item in nums:
            if count[item] > len(nums) / 2:
                return item

        # Way2
        nums.sort()
        return nums[len(nums) / 2]
