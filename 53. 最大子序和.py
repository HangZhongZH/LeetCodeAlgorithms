# O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = nums[0]
        ans = sums
        for i in range(1, len(nums)):
            if sums <= 0:
                sums = nums[i]
            else:
                sums += nums[i]
            ans = max(ans, sums)
        return ans