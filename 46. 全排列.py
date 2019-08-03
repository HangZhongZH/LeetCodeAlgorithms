class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(nums, temp):
            if not nums:
                res.append(temp)
                return res
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], temp + [nums[i]])
        backtrack(nums, [])
        return res
