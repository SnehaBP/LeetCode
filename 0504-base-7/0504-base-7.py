class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        sign="" if num>=0 else "-"
        res=""
        num=abs(num)
        while num>0:
            rem=num%7
            res=str(rem)+res
            num//=7
        return sign+res