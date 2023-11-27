class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alpha=string.ascii_uppercase
        res=""
        while columnNumber:
            rem=(columnNumber-1)%26
            columnNumber=(columnNumber-1)//26
            res+=alpha[rem]
        return res[::-1]
        