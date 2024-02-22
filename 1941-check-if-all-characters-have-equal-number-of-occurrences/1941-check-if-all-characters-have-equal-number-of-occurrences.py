class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freqDict={}
        uniqCharsIns=set(s)
        for char in s:
            if char in freqDict:
                freqDict[char]+=1
            else:
                freqDict[char]=1
        values=list(freqDict.values())
        return all(value==values[0] for value in values)
            