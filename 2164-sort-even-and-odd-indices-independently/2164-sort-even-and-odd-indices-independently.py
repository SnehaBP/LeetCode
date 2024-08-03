class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oddIndexNums = [nums[i] for i in range(len(nums)) if i % 2 != 0]
        evenIndexNums = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        oddIndexNums.sort(reverse=True)
        evenIndexNums.sort()
        res = nums[:]  
        oddIdx = 0
        evenIdx = 0 
        for i in range(len(nums)):
            if i % 2 == 0:
                res[i] = evenIndexNums[evenIdx]
                evenIdx += 1
            else:
                res[i] = oddIndexNums[oddIdx]
                oddIdx += 1
        
        return res