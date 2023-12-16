class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)[2:]
        c=0
        for i in s:
            if i!='0':
                c = c+1
        return c