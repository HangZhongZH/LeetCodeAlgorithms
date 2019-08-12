class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = 1
        big = len(nums) - 1

        while small < big:
            mid = (small + big) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                big = mid
            else:
                small = mid + 1
        return small