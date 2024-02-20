class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        largestContigious1s=0
        countOf1=0
        largestContigious0s=0
        countOf0=0
        for i in s:
            if i=='1':
                countOf1+=1
                largestContigious1s=max(largestContigious1s,countOf1)
                countOf0=0
            elif i=='0':
                countOf0+=1
                largestContigious0s=max(largestContigious0s,countOf0)
                countOf1=0
        return largestContigious1s>largestContigious0s