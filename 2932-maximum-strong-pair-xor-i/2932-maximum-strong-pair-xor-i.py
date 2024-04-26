class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res=[]
        for x in nums:
            for y in nums:
                if abs(x-y)<=min(x,y):
                    res.append([x,y])
        maxXor=0
        for [i,j] in res:
            xorRes=i ^ j
            if xorRes>=maxXor:
                maxXor=xorRes
        return maxXor
        