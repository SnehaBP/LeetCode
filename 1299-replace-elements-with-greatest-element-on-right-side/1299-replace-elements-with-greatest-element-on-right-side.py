class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=len(arr)
        maxNum=-1
        for i in range(l-1,-1,-1):
            curNum=arr[i]
            arr[i]=maxNum
            maxNum=max(maxNum,curNum)
        return arr