class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        sortedNums=sorted(nums)
        res=[i for i in range(len(sortedNums)) if sortedNums[i]==target]
        return res