class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res=0
        found=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j] and nums[j] - nums[i]>res:
                    res=nums[j] - nums[i]
                    found=1
        if found:
            return res
        else:
            return -1