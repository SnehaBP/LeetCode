class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freqTarget={}
        for i in target:
            if i in freqTarget:
                freqTarget[i]+=1
            else:
                freqTarget[i]=1
        freqArr={}
        for i in arr:
            if i in freqArr:
                freqArr[i]+=1
            else:
                freqArr[i]=1
        for i in target:
            if i not in arr or freqArr[i]!=freqTarget[i]:
                return False
        return True