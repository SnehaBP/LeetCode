class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sFreq={}
        for i in s:
            if i in sFreq:
                sFreq[i]+=1
            else:
                sFreq[i]=1
        tFreq={}
        for i in t:
            if i in tFreq:
                tFreq[i]+=1
            else:
                tFreq[i]=1
        return tFreq==sFreq
        