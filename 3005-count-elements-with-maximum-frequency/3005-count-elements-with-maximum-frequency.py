class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqDict={}
        for ele in nums:
            if ele in freqDict:
                freqDict[ele]+=1
            else:
                freqDict[ele]=1
        res=0
        maxVal=max(freqDict.values())
        for val in freqDict.values():
            if val == maxVal:
                res+=val
        return res