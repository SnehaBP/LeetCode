class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxOfNums=max(nums)
        length=len(nums)
        res=list(range(1,maxOfNums+1))
        res.append(maxOfNums)
        return collections.Counter(res)==collections.Counter(nums)