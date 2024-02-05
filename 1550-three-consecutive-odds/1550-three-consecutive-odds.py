class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd=0
        oddCount=0
        for i in arr:
            if (i%2!=0) and odd==0:
                odd=1
                oddCount+=1
            elif i%2==0:
                odd=0
                oddCount=0
            elif odd==1:
                oddCount+=1
            if oddCount==3:
                return True
        return False
            