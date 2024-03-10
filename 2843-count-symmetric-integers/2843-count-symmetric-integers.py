class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for num in range(low,high+1):
            if len(str(num))%2==0:
                sNum=str(num)
                n=len(sNum)//2
                firstHalf=sNum[0:n]
                secondHalf=sNum[n:]
                sumFirstHalf=sum(int(dig) for dig in firstHalf)
                sumSecondHalf=sum(int(dig) for dig in secondHalf)
                if sumFirstHalf == sumSecondHalf:
                    count+=1
        return count
            