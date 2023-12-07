class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        n=min(nums)
        flag=0
        for i in range(n,m+1):
            if i not in nums:
                flag=i
        if flag!=0:
            return flag
        elif flag==0 and n!=0:
            return 0
        else:
            return m+1