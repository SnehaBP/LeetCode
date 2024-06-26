class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dif1 = [element for element in nums1 if element not in nums2]
        dif2 = [element for element in nums2 if element not in nums1]
        res = []
        res.append(set(dif1))
        res.append(set(dif2))
        return res

        