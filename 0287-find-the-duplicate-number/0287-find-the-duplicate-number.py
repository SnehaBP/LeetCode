class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqDict = {}
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        for key , val in freqDict.items():
            if val > 1:
                return key
        