class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        rl, cl = 0, 0
        if matrix == []:
            return []
        else:
            rr, cr = len(matrix) - 1, len(matrix[0]) - 1
            while cl <= cr and rl <= rr:
                c1 = cl
                r1 = rl
                c2 = cr
                r2 = rr
                if cl == cr:
                    for i in range(r1, r2+1):
                        res.append(matrix[i][cl])
                elif rl == rr:
                    for i in range(c1, c2+1):
                        res.append(matrix[rl][i])
                else:
                    while c1 != cr:
                        res.append(matrix[rl][c1])
                        c1 += 1
                    while r1 != rr:
                        res.append(matrix[r1][cr])
                        r1 += 1
                    while c2 != cl:
                        res.append(matrix[rr][c2])
                        c2 -= 1
                    while r2 != rl:
                        res.append(matrix[r2][cl])
                        r2 -= 1
                cl += 1
                cr -= 1
                rl += 1
                rr -= 1
            return res