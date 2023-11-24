class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def toReverse(x):
            rev=0
            while x>0:
                digit=x%10
                rev=(rev*10)+digit
                x=x//10
            return rev
        reversed1=toReverse(num)
        reversed2=toReverse(reversed1)
        return reversed2==num
        