class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for op in operations:
            if op=='C':
                res.remove(res[-1])
            elif op=='D':
                res.append(2*res[-1])
            elif op=='+':
                res.append(res[-2]+res[-1])
            else:
                res.append(int(op))
        return sum(res)
                
            