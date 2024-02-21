class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        found=0
        for i in range(len(nums)):
            if i%10 == nums[i]:
                found=1
                break
        if found:
            return i
        else:
            return -1