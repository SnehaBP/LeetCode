class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        boundaryCount = 0
        for move in nums:
            position += move
            if position == 0:
                boundaryCount += 1
        return boundaryCount 