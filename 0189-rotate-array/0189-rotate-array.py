class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        steps=k%n
        nums[:]=nums[-steps:]+nums[:-steps]
        return nums