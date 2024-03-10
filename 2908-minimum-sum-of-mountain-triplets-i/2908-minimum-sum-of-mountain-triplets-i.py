class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        tripletSum=999
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        tripletSum=min(tripletSum,nums[i]+nums[j]+nums[k])
        if tripletSum==999:
            return -1
        else:
            return tripletSum
            