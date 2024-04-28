class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set(nums3)
        intersection12=nums1&nums2
        intersection23=nums3&nums2
        intersection13=nums1&nums3
        res=intersection12|intersection23|intersection13
        return res


        