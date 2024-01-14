class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alicsSum=sum(aliceSizes)
        bobsSum=sum(bobSizes)
        diff=(alicsSum-bobsSum)//2
        bobsSet = set(bobSizes)
        for size in aliceSizes:
            if size-diff in bobsSet:
                return [size,size-diff]