class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ls1=list(s)
        ls2=list(t)
        ls1Count = {}
        for i in ls1:
            if i in ls1Count:
                ls1Count[i]+=1
            else:
                ls1Count[i]=1
        for i in ls2:
            if i not in ls1Count or ls1Count[i]==0:
                return i
            ls1Count[i]-=1