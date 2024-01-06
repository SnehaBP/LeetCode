class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n = len(s)
        start = 0
        for end in range(1, n):
            if s[end] != s[start]:
                if end - start >= 3:
                    res.append([start, end - 1])
                start = end
        if n - start >= 3:
            res.append([start, n - 1])
        return res
