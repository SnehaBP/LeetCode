class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if max(nums)==nums[-1]:
            return len(nums)-1
        index=0
        for i in range(1, len(nums)-1):
            if nums[i-1]<nums[i] and nums[i+1]<nums[i]:
                index=i
        return index