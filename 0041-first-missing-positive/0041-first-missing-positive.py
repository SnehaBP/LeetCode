class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positiveNums = [num for num in nums if num > 0]
        positiveNums = set(positiveNums)
        positiveNums = sorted(positiveNums)
        if not positiveNums:
            return 1
        for i in range(0, len(positiveNums)):
            if i+1 != positiveNums[i]:
                return i+1
        return positiveNums[i] + 1