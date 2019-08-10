class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # res = []
        # n = len(nums)
        # def helper(i, tmp):
        #     res.append(tmp)
        #     for j in range(i, n):
        #         helper(j + 1, tmp + [nums[j]])
        # helper(0, [])
        # return res

        tmp = [[]]
        for j in range(len(nums)):
            self.helper(j, tmp, nums)
            # print(tmp)
        return tmp

    def helper(self, i, tmp, nums):  # 现在到了第i个数，现在有的子集为tmp
        for j in range(len(tmp)):
            tmp.append(tmp[j] + [nums[i]])
