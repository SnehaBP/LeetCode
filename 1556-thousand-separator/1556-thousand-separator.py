class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=str(n)
        if len(n)<=3:
            return str(n)
        res=[]
        for i in range(len(n)-1,-1,-1):
            res.insert(0,n[i])
            if (len(n)-i)%3==0 and i!=0:
                res.insert(0,'.')
        return "".join(res)