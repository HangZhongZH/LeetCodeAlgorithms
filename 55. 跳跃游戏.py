class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastnums = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= lastnums:
                lastnums = i
        if lastnums == 0:
            return True
        else:
            return False