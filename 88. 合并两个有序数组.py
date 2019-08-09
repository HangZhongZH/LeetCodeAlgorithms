class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1
        l2 = n - 1
        p = m + n - 1

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] <= nums2[l2]:
                nums1[p] = nums2[l2]
                p -= 1
                l2 -= 1
            else:
                nums1[p] = nums1[l1]
                l1 -= 1
                p -= 1
        if l2 >= 0:
            nums1[: l2 + 1] = nums2[: l2 + 1]
        return nums1