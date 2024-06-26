class Solution:
    def __init__(self):
        self.memo = {}
    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            res = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
            self.memo[n] = res
        return res