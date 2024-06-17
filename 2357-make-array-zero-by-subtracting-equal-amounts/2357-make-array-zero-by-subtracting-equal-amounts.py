class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return 0
        if len(nums) == 1 and nums[0] != 0:
            return 1
        else:
            count = 0
            numsWithout0 = [n for n in nums if n != 0]
            minNum = float('inf')
            while numsWithout0:
                minNum = min(numsWithout0)
                numsWithout0 = [n - minNum for n in numsWithout0 if n - minNum > 0]
                count += 1
            return count