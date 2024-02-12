class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[nums[0]]
        for i in range(1,n):
            sum=0
            for j in range(0,i+1):
                sum+=nums[j]
            res.append(sum)
        return res