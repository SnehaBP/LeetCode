class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        i=num
        while i>0:
            if i%2==0:
                i=i//2
            else:
                i=i-1
            count+=1
        return count