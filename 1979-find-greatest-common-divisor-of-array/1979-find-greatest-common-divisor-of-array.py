class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        while b!=0:
            temp=b
            b=a%b
            a=temp
        return a