class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        else:
            res = []
            res.append([1])
            for i in range(1, numRows):
                temp = [1] * (i + 1)
                for j in range(1,i):
                    temp[j] = res[-1][j - 1] + res[-1][j]
                res.append(temp)
            #print(res)
            return res