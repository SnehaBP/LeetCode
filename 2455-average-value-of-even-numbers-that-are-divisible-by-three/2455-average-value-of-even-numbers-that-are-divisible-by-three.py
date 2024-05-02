class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count=0
        totalSum=0
        for num in nums:
            if num%3==0 and num%2==0:
                count+=1
                totalSum+=num
        if totalSum==0:
            return 0
        return totalSum//count