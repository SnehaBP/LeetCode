class Solution:
    def arrangeCoins(self, n: int) -> int:
        completedRow=0
        while completedRow<n:
            completedRow+=1
            n-=completedRow
        return  completedRow