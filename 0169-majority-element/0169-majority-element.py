class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        count = 0
        for num in nums:
            if count == 0:
                n = num
                count += 1
            elif num == n:
                count += 1
            else:
                count -= 1
        return n

        