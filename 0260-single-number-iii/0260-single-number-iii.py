class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        else:
            res = []
            freq = collections.Counter(nums)
            for num, count in  freq.items():
                if count == 1:
                    res.append(num)
        return res