class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=len(nums)
        count = 0
        while count < l:
            n = (count+l) // 2
            if nums[n] == target:
                return n
            if nums[n] < target:
                count = n + 1
            else:
                l = n

        return count
