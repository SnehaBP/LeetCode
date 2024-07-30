class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def intersetionCount(nums1, nums2):
            count = 0
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    count +=1
            return count
        val1 = intersetionCount(nums1, nums2)
        val2 = intersetionCount(nums2, nums1)
        res = []
        res.append(val1)
        res.append(val2)
        return res