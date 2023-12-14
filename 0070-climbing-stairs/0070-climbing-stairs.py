class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2: 
            return 2
        s=[0]*(n+1)
        s[1]=1
        s[2]=2
        for i in range(3,n+1):
            s[i]=s[i-1]+s[i-2]
        return s[n]