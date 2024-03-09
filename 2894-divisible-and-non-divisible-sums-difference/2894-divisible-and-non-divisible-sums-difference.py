class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisibleSum=0
        nondivisibleSum=0
        for num in range(1,n+1):
            if num%m==0:
                divisibleSum+=num
            else:
                nondivisibleSum+=num
        return nondivisibleSum-divisibleSum