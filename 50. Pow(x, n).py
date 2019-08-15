class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        def digui(x, n):
            if n == 0:
                return 1
            res = digui(x, n // 2)
            if n % 2 == 0:
                return res * res
            else:
                return res * res * x

        if n > 0:
            return digui(x, n)
        elif n < 0:
            return 1 / digui(x, -n)