class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = list(combinations(range(1, n + 1), k))
        return res