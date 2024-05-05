class Solution:
    def isFascinating(self, n: int) -> bool:
        concatinationStr=str(n)+str(2*n)+str(3*n)
        print(concatinationStr)
        freqDict={}
        for ele in concatinationStr:
            if ele in freqDict:
                freqDict[ele]+=1
            else:
                freqDict[ele]=1
        for digit in "123456789":
            if freqDict.get(digit,0)!=1:
                return False
        return True