class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        slow, fast = 0, 1
        while fast <= len(nums) - 1:
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1
        return slow + 1
