class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortedArr=sorted(arr)
        d=sortedArr[1]-sortedArr[0]
        for i in range(1,len(sortedArr)-1):
            if d!=sortedArr[i+1]-sortedArr[i]:
                return False
        return True