class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lr, lc = 0, 0
        rr, rc = len(matrix) - 1, len(matrix) - 1
        while lr < rr:
            self.rotateEdge(matrix, lr, lc, rr, rc)
            lr += 1
            lc += 1
            rr -= 1
            rc -= 1

    def rotateEdge(self, matrix, lr, lc, rr, rc):
        times = rc - lc
        for i in range(times):
            temp = matrix[lr][lc + i]
            matrix[lr][lc + i] = matrix[rr - i][lc]
            matrix[rr - i][lc] = matrix[rr][rc - i]
            matrix[rr][rc - i] = matrix[lr + i][rc]
            matrix[lr + i][rc] = temp

