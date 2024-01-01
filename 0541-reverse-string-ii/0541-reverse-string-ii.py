class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=list(s)
        l=len(res)
        for i in range(0,l,2*k):
            start,end=i,min(i+k-1,l-1)
            while start<end:
                res[start],res[end]=res[end],res[start]
                start+=1
                end-=1
        return "".join(res)