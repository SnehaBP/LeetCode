class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            product = 1
            
            for num in nums:
                product *= num
                
        
        nums = sorted(nums)
        
        return max(nums[0] * nums[1] * nums[2], nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])