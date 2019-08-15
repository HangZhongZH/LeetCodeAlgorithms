class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 若> 0，后面的数只要大于0就可以继续往后走，因为此时加上后面的数的乘积一定大于等于前面
        # 若< 0, 前面最小的数到此为最大，最大为最小
        # 若 = 0，除非前面为负数则取，使结果为0，不然在此断开
        if not nums:
            return

        premax = nums[0]
        premin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            curmax = max(premax * nums[i], premin * nums[i], nums[i])
            curmin = min(premax * nums[i], premin * nums[i], nums[i])
            res = max(curmax, res)
            premax = curmax
            premin = curmin
        return res