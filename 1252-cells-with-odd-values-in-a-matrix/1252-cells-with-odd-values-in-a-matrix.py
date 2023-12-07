class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for index in indices:
            rows[index[0]] += 1
            cols[index[1]] += 1

        odd_count = 0
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 != 0:
                    odd_count += 1

        return odd_count