class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in indices and i - indices[num] <= k:
                return True
            indices[num] = i

        return False