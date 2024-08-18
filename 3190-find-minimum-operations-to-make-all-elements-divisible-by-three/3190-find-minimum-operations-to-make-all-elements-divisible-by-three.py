class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i % 3 != 0:
                if (i -1) % 3 == 0 or (i + 1) % 3 == 0:
                    count += 1
        return count