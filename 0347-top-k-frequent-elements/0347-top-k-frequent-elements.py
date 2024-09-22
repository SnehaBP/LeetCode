class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        res = [item for item, freq in counter.most_common(k)]
        return res