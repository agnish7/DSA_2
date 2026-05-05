class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:

        if n == 1:
            return x
        elif n == -1:
            return 1 / x
        elif n == 0:
            return 1
        
        le = n // 2
        re = n - le

        return self.myPow(x, le) * self.myPow(x, re)