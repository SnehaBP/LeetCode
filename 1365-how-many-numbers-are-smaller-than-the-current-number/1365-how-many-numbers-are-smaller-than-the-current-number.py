class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def smallNumber(num):
            count=0
            for i in nums:
                if i<num:
                    count+=1
            return count
        res=[]
        for j in nums:
            res.append(smallNumber(j))
        return res