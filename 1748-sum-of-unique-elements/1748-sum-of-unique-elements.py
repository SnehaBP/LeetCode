class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freqDict={}
        sumValue=0
        for num in nums:
            if num in freqDict:
                freqDict[num]+=1
            else:
                freqDict[num]=1
        for key in freqDict.keys():
            if freqDict[key]==1:
                sumValue+=key
        return sumValue