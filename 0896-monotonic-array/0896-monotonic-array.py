class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monoInc=monoDec=True
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                monoDec=False
            if nums[i]<nums[i-1]:
                monoInc=False
        return monoInc or monoDec