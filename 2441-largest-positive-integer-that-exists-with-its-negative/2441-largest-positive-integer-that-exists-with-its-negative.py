class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positiveNums=[num for num in nums if num>0]
        sortedPositiveNums=sorted(positiveNums)
        for i in range(len(sortedPositiveNums)-1,-1,-1):
            if -sortedPositiveNums[i] in nums:
                return sortedPositiveNums[i]
        return -1