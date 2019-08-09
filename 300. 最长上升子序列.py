# Way1 O(N**2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            res = [1]
            for i in range(1, len(nums)):
                ans = 1
                for j in range(i):
                    if nums[i] > nums[j]:
                        ans = max(ans, res[j] + 1)
                res.append(ans)
        return max(res)


# Way2 O(Nlog(N))
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            res = [nums[0]]
            for i in range(1, len(nums)):
                if nums[i] > res[-1]:
                    res.append(nums[i])
                else:
                    for j in range(len(res)):
                        if nums[i] < res[j]:
                            res[j] = nums[i]
                            break
                        elif nums[i] == res[j]:
                            break
        return len(res)