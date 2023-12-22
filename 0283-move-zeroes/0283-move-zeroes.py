class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ifIndexIs0=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[ifIndexIs0]=nums[ifIndexIs0],nums[i]
                ifIndexIs0+=1