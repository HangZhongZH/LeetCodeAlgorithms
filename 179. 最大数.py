class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if sum(nums) == 0:
            return '0'
        else:
            nums.sort(self.mysort)
        res = ''
        for item in nums:
            item = str(item)
            res += item
        return res

    def mysort(self, x, y):
        if int(str(x) + str(y)) < int(str(y) + str(x)):
            return 1
        else:
            return -1

