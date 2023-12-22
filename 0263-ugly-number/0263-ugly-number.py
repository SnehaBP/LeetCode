class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        for factore in [2,3,5]:
            while n%factore==0:
                n/=factore
        return n==1