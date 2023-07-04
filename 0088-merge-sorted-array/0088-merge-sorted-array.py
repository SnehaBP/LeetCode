class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        while i<n:
            nums1.remove(nums1[-1])
            i+=1
        i=0
        while i<n:
            nums1.append(nums2[i])
            i+=1
        nums1.sort()
        print(nums1)