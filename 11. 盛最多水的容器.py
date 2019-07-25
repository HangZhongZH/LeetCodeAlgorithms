# 11. 盛最多水的容器
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left <= right:
            length = right - left
            if height[left] <= height[right]:
                h = height[left]
                left += 1
            elif height[left] > height[right]:
                h = height[right]
                right -= 1
            maxArea_temp = length * h
            if maxArea_temp >= maxArea:
                maxArea = maxArea_temp
        return maxArea