class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        res = []
        for num, count in counter.items():
            if count > 1:
                res.append(num)
        return res