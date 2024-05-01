class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convertToInt(num):
            n=0
            for dig in num:
                n=n*10+(ord(dig)-ord('0'))
            return n
        num1=convertToInt(num1)
        num2=convertToInt(num2)
        return str(num1*num2)