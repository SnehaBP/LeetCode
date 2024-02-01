class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ncount=0
        for num in nums:
            dcount=0
            while(num>0):
                digit=num%10
                dcount+=1
                num=num//10
            if dcount%2==0:
                ncount+=1
        return ncount