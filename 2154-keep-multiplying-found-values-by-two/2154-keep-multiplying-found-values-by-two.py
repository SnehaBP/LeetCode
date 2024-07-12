class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        generatedNum = original
        if original in nums:
            generatedNum = original * 2
        found = 1
        while found != 0:
            if generatedNum in nums:
                generatedNum = generatedNum * 2
                found = 1
            else:
                found = 0
        return generatedNum