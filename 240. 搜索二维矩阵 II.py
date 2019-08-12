class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        rows, cols = len(matrix), len(matrix[0])
        pivot_rows, pivot_cols = 0, cols - 1
        while pivot_rows <= rows - 1 and pivot_cols >= 0:
            if matrix[pivot_rows][pivot_cols] == target:
                return True
            elif matrix[pivot_rows][pivot_cols] > target:
                pivot_cols -= 1
            elif matrix[pivot_rows][pivot_cols] < target:
                pivot_rows += 1
        return False