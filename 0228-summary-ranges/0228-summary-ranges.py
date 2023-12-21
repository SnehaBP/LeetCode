class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res=[]
        start=end=nums[0]
        for n in nums[1:]:
            if n==end+1:
                end=n
            else:
                res.append(formatRange(start,end))
                start=end=n
        res.append(formatRange(start,end))
        return res
def formatRange(a , b):
    if a==b:
        return str(a)
    else:
        return f"{a}->{b}"