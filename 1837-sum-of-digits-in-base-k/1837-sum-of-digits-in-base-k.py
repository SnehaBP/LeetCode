class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        if n == 0:
            return 0
        while n:
            dig = n % k
            res += dig
            n //= k
        return res