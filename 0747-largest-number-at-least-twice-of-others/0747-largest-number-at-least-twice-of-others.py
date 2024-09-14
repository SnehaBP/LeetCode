class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        maxIndex = nums.index(maxNum)
        for i in range(len(nums)):
            if nums[i] == maxNum:
                continue
            elif 2*nums[i] > int(maxNum):
                return -1
        return maxIndex