class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1

        rows = len(matrix)
        cols = len(matrix[0])

        smallest = matrix[0][0]
        biggest = matrix[rows - 1][cols - 1]

        def countlessmid(mid):
            count = 0
            j = cols - 1
            for i in range(rows):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            return count

        while smallest < biggest:
            mid = (smallest + biggest) // 2
            count = countlessmid(mid)
            if count < k:
                smallest = mid + 1
            else:
                biggest = mid
        return smallest