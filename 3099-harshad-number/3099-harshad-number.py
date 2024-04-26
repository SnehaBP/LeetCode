class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x=str(x)
        sumOfDigits=0
        for i in x:
            sumOfDigits+=int(i)
        if int(x)%sumOfDigits==0:
            return sumOfDigits
        else:
            return -1