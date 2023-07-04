class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r=0
        for i in digits:
            r=r*10 + i
        r=r+1
        l=[]
        while r:
            r1=r%10
            l.append(r1)
            r=r/10
        l.reverse()
        return l
        