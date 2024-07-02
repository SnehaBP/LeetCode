class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res = []
        while nums:
            minItem = min(nums)
            maxItem = max(nums) 
            res.append((minItem+maxItem)/2)
            nums.remove(minItem)
            nums.remove(maxItem) 
        return min(res)