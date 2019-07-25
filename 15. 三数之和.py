# 15. 三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i >= 1:
                continue
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                break
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while nums[left] == nums[left + 1] and left < right - 1:
                        left += 1
                    while nums[right] == nums[right - 1] and right > left + 1:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans