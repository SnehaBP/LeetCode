class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l=len(arr)
        specialInt=l//4
        freqDict={}
        for num in arr:
            if num in freqDict:
                freqDict[num]+=1
            else:
                freqDict[num]=1
            if freqDict[num]>specialInt:
                return num