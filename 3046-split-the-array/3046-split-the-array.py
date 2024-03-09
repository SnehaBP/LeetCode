class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums1=[]
        nums2=[]
        for i in range(len(nums)):
            if len(nums1)!=len(nums):
                if nums[i] not in nums1:
                    nums1.append(nums[i])
                else:
                    nums2.append(nums[i])
        return len(nums1)==len(set(nums1)) and len(nums2)==len(set(nums2))