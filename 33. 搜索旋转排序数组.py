class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums, target, l, r):
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[r]:  # 右半边有序
            if nums[r] == target:
                return r
            elif nums[mid] < target and target < nums[r]:  # target在右半部分
                return self.helper(nums, target, mid + 1, r)
            else:  # 位于左半部分
                return self.helper(nums, target, l, mid - 1)

        else:  # 左半部分有序
            if nums[l] <= target and target < nums[mid]:
                return self.helper(nums, target, l, mid - 1)
            else:
                return self.helper(nums, target, mid + 1, r)