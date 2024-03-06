class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum=0
        digitSum=0
        for num in nums:
            elementSum+=num
            while num>0:
                dig=num%10
                digitSum+=dig
                num=num//10
        return abs(elementSum-digitSum)
    