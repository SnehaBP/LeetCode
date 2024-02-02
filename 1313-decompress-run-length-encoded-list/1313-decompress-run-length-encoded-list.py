class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=0
        res=[]
        while i<len(nums):
            res.extend([nums[i+1]]*nums[i])
            i+=2
        return res