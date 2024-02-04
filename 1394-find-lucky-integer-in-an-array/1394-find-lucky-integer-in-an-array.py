class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqDict={}
        for i in arr:
            if i in freqDict:
                freqDict[i]+=1
            else:
                freqDict[i]=1
        maxLucky=-1
        for i in freqDict:
            if i==freqDict[i]:
                maxLucky=max(maxLucky,i)
        return maxLucky