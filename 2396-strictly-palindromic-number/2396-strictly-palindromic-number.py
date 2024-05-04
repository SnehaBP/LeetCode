class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def toBase(num, base):
            digs=[]
            while num>0:
                rem=num%base
                digs.append(rem)
                num=num//base
            return ''.join(str(d) for d in reversed(digs))
        for b in range(2,n-1):
            basebrepre=toBase(n, b)
            if basebrepre!=basebrepre[::-1]:
                return False
        return True