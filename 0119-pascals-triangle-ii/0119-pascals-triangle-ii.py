class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        res=[1]
        for i in range(1,rowIndex):
            res.append(res[i-1]*(rowIndex-i+1)//i)
        res.append(1)
        return res