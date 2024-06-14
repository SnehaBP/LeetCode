class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = []
        evenNums = []
        oddNums = []
        for num in nums:
            if num % 2 == 0:
                evenNums.append(num)
            else:
                oddNums.append(num)  
        i = 0
        while i != len(evenNums) and i != len(oddNums):
            res.append(evenNums[i])
            res.append(oddNums[i])
            i += 1
        return res
            
            