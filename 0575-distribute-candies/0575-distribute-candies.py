class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        maxCandy=len(candyType)//2
        uniqueCandy=len(set(candyType))
        return min(maxCandy,uniqueCandy)