class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xorSum=0
        for length in range(1,len(nums)+1):
            for subset in itertools.combinations(nums, length):
                subsetXorSum=0
                for ele in subset:
                    subsetXorSum^=ele
                xorSum+=subsetXorSum
        return xorSum