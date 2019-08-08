# Way 1, 内置函数
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        nums = nums[::-1]
        return nums[k - 1]


# Way 2, 快速排序
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = self.quicksort(nums, 0, len(nums) - 1)
        nums = nums[::-1]
        return nums[k - 1]

    def partition(self, nums, l, r):
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] > pivot:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            while l < r and nums[l] <= pivot:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
        return l

    def quicksort(self, nums, l, r):
        if l < r:
            pivotidx = self.partition(nums, l, r)
            self.quicksort(nums, l, pivotidx - 1)
            self.quicksort(nums, pivotidx + 1, r)
        return nums
