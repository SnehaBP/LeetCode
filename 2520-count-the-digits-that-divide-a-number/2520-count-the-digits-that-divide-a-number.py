class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        originalNum=num
        while num>0:
            dig=num%10
            if originalNum%dig==0:
                count+=1
            num=num//10
        return count