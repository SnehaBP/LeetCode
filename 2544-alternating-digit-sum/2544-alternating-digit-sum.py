class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        even=map(int,tuple(s[0::2]))
        odd=map(int,tuple(s[1::2]))
        return sum(even)-sum(odd)
    