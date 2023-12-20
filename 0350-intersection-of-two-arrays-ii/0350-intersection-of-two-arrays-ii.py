class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = {}
        st = []
        for n in nums1:
            if n in nums1_count:
                nums1_count[n]+=1
            else:
                nums1_count[n]=1
        for n in nums2:
            if n in nums1_count and nums1_count[n]>0:
                st.append(n)
                nums1_count[n]-=1
        return st