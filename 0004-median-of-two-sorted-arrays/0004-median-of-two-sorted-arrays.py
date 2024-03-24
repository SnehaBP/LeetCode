class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted(nums1+nums2)
        mid=len(nums)/2
        if mid.is_integer():  # Check if mid is an integer
            return (nums[int(mid)] + nums[int(mid) - 1]) / 2
        else:
            return nums[int(mid)]